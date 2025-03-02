from urllib.parse import urlparse
import re
import whois
import datetime
import requests
import math
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import quote
from collections import Counter

# 1 if the URL is Malicious
# -1 if the URL is Legitimate
# 0 if the URL is Suspicious/ Undetermined

class CheckResult:
    def __init__(self):
        self.response = []
        self.errors = []

    def add_response(self, response_message):
        self.response.append(response_message)
        
    def add_error(self, error_message):
        self.errors.append(error_message)
        
def get_whois_info(domain, result):
    try:
        temp = whois.whois(domain)
        result.add_response(temp)
        return temp
    except Exception as e:
        # print(f"An error occurred: {e}")
        result.add_error(e)
        return None
# 1. owner infor    
def check_owner_info(domain_infor):
    if not domain_infor or not domain_infor.registrar or not domain_infor.name:
        return -1  # Không xác định
    elif "privacy" in domain_infor.registrar.lower() or "protected" in domain_infor.registrar.lower() or not domain_infor.name or not isinstance(domain_infor.name,str):
        return 0  # Tạm coi là an toàn (có bảo mật Whois)
    else:
        return 0  # Có thông tin rõ ràng    
# 2. Web Traffic
def requests_retry_session(retries=3, backoff_factor=0.3, session=None):
    session = session or requests.Session()
    retry = requests.packages.urllib3.util.retry.Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=(500, 502, 503, 504),
    )
    adapter = requests.adapters.HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def check_alexa_rank(url):
    try:
        alexadata = BeautifulSoup(requests.get(
            "http://data.alexa.com/data?cli=10&dat=s&url=" + domain, timeout=10).content, 'lxml')
        rank = int(alexadata.find('reach')['rank'])
        if rank < 100000:
            return -1
        else:
            return 1
    except:
        return 1
# -------------
# 3. Creation Date
def check_creation_date(domain_infor):
    if not domain_infor or not hasattr(domain_infor, 'creation_date') or not domain_infor.creation_date:
        return 0  # Không có thông tin ngày đăng ký

    # Xử lý trường hợp creation_date là danh sách
    if isinstance(domain_infor.creation_date, list):
        creation_date = domain_infor.creation_date[0]
    else:
        creation_date = domain_infor.creation_date

    # Kiểm tra và chuyển đổi creation_date sang kiểu datetime nếu cần
    if isinstance(creation_date, str):
        try:
            creation_date = datetime.strptime(creation_date, "%Y-%m-%d")
        except ValueError:
            return 0  # Không thể chuyển đổi chuỗi thành datetime

    # Đảm bảo creation_date là đối tượng datetime trước khi so sánh
    if isinstance(creation_date, datetime):
        now = datetime.now()
        if creation_date > now - timedelta(days=365):
            return 1  # Nguy hiểm (mới đăng ký)
        else:
            return 1
    else:
        return 0  # Dữ liệu không hợp lệ
 
# 4. Expiry Date
def check_expiry_date(domain_infor):
    if not domain_infor or not hasattr(domain_infor, 'expiration_date') or not domain_infor.expiration_date:
        return 0  # Không có thông tin ngày hết hạn

    # Xử lý trường hợp expiration_date là danh sách
    if isinstance(domain_infor.expiration_date, list):
        expiry_date = domain_infor.expiration_date[0]  # Lấy ngày hết hạn đầu tiên nếu là danh sách
    else:
        expiry_date = domain_infor.expiration_date

    # Kiểm tra và chuyển đổi expiration_date sang kiểu datetime nếu cần
    if isinstance(expiry_date, str):
        try:
            # Giả sử định dạng ngày là YYYY-MM-DD, có thể thay đổi tùy theo trường hợp
            expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
        except ValueError:
            return 0  # Không thể chuyển đổi chuỗi thành datetime

    # Đảm bảo expiry_date là đối tượng datetime trước khi so sánh
    if isinstance(expiry_date, datetime):
        now = datetime.now()
        if expiry_date < now + timedelta(days=30):
            return 1  #sắp hết hạn)
        else:
            return -1 
    else:
        return 0  # Dữ liệu không hợp lệ

# 5. DNS Servers
def check_dns_servers(domain_infor):
  if not domain_infor or not domain_infor.name_servers:
    return 0  # Không xác định (không có thông tin hoặc không có name_servers)

  if not isinstance(domain_infor.name_servers, list):
    return 0  # Dữ liệu name_servers không phải là danh sách

  if len(domain_infor.name_servers) < 2:
    return 1  # Ít hơn 2 DNS servers thường không tốt

  return -1  # Có ít nhất 2 DNS servers

# 6. DNSSEC
def check_dnssec(domain_infor):
    if not domain_infor or not hasattr(domain_infor, 'dnssec'):  # Kiểm tra domain_infor và sự tồn tại của thuộc tính dnssec
        return 0  # Không xác định (thông tin không có)
    dnssec_status = domain_infor.dnssec

    if dnssec_status is None: # trường hợp dnssec trả về None
        return 0

    if isinstance(dnssec_status, list): # xử lý trường hợp dnssec là list
        dnssec_status=dnssec_status[0]

    if isinstance(dnssec_status,str):
        dnssec_status=dnssec_status.lower()
        if "unsigned" in dnssec_status or "inactive" in dnssec_status:
            return 1  # Nguy hiểm (DNSSEC không được kích hoạt)
        elif "signed" in dnssec_status or "active" in dnssec_status:
            return -1  # An toàn (DNSSEC được kích hoạt)
        else:
            return 0 # không xác định
    else:
        return 0 # không xác định
    
#7. Entropy of Domain Name string
def calculate_entropy(string):
    if not string:
        return 0

    # Count the occurrences of each character in the string
    counts = Counter(string)
    total_length = len(string)

    # Calculate the entropy
    entropy = -sum((count / total_length) * math.log2(count / total_length) for count in counts.values())
    return entropy

def classify_entropy_of_domain(domain):

    # Remove "www." prefix if present
    if domain.startswith("www."):
        domain = domain[4:]

    entropy = calculate_entropy(domain)

    # Define thresholds for classification
    if entropy < 3.5:
        return -1  # Legitimate
    elif 3.5 <= entropy <= 4.5:
        return 0  # Suspicious
    else:
        return 1  # Malicious
#------------------------------------------------------------------------------- 
# 1.Domain of the URL (Domain)
def getDomain(url):
    try:
        # Bổ sung scheme nếu thiếu
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        parsed_url = urlparse(url)
        netloc = parsed_url.netloc
        # print(netloc)
        # Xử lý trường hợp IP address
        if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", netloc):
            return netloc

        # Xử lý các trường hợp khác
        domain_parts = netloc.split('.')
        if len(domain_parts) >= 2:
            # Loại bỏ 'www' nếu có
            if domain_parts[0] == 'www':
                domain_parts.pop(0)
            # Trả về domain
            return '.'.join(domain_parts[-2:])
        else:
            return None
    except Exception as e:
        # print(f"Domain of the URL::: Error extracting domain from {url}: {e}")
        return None
  
def domain(url):
    result = CheckResult()
    try:
        domain = getDomain(url)
        domain_infor = get_whois_info(domain, result)
        # print("domain_infor:::", domain_infor)
    except Exception as e:  # Catch all exceptions and print the error message
        # print(f"An error occurred: {e}")
        domain_infor = None
    return {
        'owner_infor': 0 if domain_infor is None else check_owner_info(domain_infor),
        'web_traffic': 0 if domain_infor is None else check_alexa_rank(domain),
        'create_date': 0 if domain_infor is None else check_creation_date(domain_infor),
        'expiry_date': 0 if domain_infor is None else check_expiry_date(domain_infor),
        'dns_servers': 0 if domain_infor is None else check_dns_servers(domain_infor),
        'dnssec': 0 if domain_infor is None else check_dnssec(domain_infor),
        'entropy': 0 if domain_infor is None else classify_entropy_of_domain(domain),
        'response_domain': result.response, 
        'errors_domain': result.errors
    }   
    
if __name__ == "__main__":
    url = "https://chatgpt.com/"  # test
    result = domain(url)
    # Lặp qua từng cặp khóa-giá trị và in
    for key, value in result.items():
        print(f"{key}: {value}")