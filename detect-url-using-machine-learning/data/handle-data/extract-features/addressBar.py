import re
import requests
import math
from collections import Counter
from urllib.parse import urlparse

# Functions to assess URL features for potential suspicious or malicious behavior

def check_url_length(url):
    url_length = len(url)
    if url_length > 75:
        return 1  # Long URL => suspicious/malicious
    elif url_length < 54:
        return -1  # Short URL => likely legitimate
    else:
        return 0  # Medium-length URL => suspicious

def check_ip_in_hostname(url):
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
    try:
        hostname = re.findall(r"https?://([^/]+)/?", url)
        if not hostname:
            return 0  # Improperly formatted URL => suspicious
        hostname = hostname[0]
        if re.match(ip_pattern, hostname):
            return 1  # IP address in hostname => suspicious/malicious
        else:
            return -1  # Valid hostname
    except Exception:
        return 0  # Treat errors as suspicious

def check_query_length(url):
    try:
        query = re.findall(r"\?(.*)$", url)
        if not query:
            return -1  # No query string => legitimate
        query_length = len(query[0])
        if query_length > 50:
            return 1  # Long query string => suspicious
        else:
            return 0  # Medium-length query string => suspicious
    except Exception:
        return 0  # Treat errors as suspicious

def check_token_count(url):
    try:
        tokens = re.split(r"[\./?=&]", url)
        token_count = len([token for token in tokens if token])
        if token_count > 10:
            return 1  # High number of tokens => suspicious/malicious
        elif token_count <= 5:
            return -1  # Few tokens => likely legitimate
        else:
            return 0  # Medium number of tokens => suspicious
    except Exception:
        return 0  # Treat errors as suspicious

def check_entropy(url):
    char_count = Counter(url)
    entropy = -sum((count / len(url)) * math.log2(count / len(url)) for count in char_count.values())
    # Làm tròn lên (ceil)
    return math.ceil(entropy)

shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"

def check_tinyURL(url):
    try:
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        response = requests.get(url, allow_redirects=True, timeout=1)
        final_url = response.url
        match = re.search(shortening_services, final_url)
        return 1 if match else 0
    except requests.exceptions.RequestException:
        return -1  # Treat errors as suspicious

def check_httpDomain(url):
    try:
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        response = requests.get(url, allow_redirects=True, timeout=1)
        final_url = response.url
        parsed_url = urlparse(final_url)
        return 1 if parsed_url.scheme == "https" else 0
    except requests.exceptions.RequestException:
        return -1

def check_depth(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        depth = path.count("/") - 1 if path.startswith("//") else path.count("/")
        return depth
    except Exception:
        return -1

def check_double_slash_redirecting(url):
    return 1 if re.search(r"https?://[^\s]*//", url) else -1

def addressBar(url):
    return {
        'url_length': check_url_length(url),
        'ip_in_hostname': check_ip_in_hostname(url),
        'query_length': check_query_length(url),
        'token_count': check_token_count(url),
        'entropy': check_entropy(url),
        'tinyURL': check_tinyURL(url),
        'httpDomain': check_httpDomain(url),
        'depth': check_depth(url),
        'double_slash_redirecting': check_double_slash_redirecting(url),
        'dots': url.count('.'),
        'hyphens': url.count('-'),
        'underscores': url.count('_'),
        'equals': url.count('='),
        'forward_slashes': url.count('/'),
        'question_marks': url.count('?'),
        'semicolons': url.count(';'),
        'open_parentheses': url.count('('),
        'close_parentheses': url.count(')'),
        'mod_signs': url.count('%'),
        'ampersands': url.count('&'),
        'at_the_rate': url.count('@'),
        'digits': sum(c.isdigit() for c in url),
        'has_www': 'www.' in url,
        'has_exe': '.exe' in url,
        'has_confirm': 'confirm' in url,
        'has_login': 'login' in url,
        'has_account': 'account' in url,
        'has_zip': '.zip' in url,
        'has_rar': '.rar' in url,
        'has_link': 'link=' in url,
        'has_plugins': 'plugins' in url,
        'has_js': '.js' in url,
        'has_jar': '.jar' in url,
        'has_verification': 'verification' in url,
        'has_bin': '.bin' in url,
        'has_php': 'php' in url
    }
if __name__ == "__main__":
    url = "https://chatgpt.com/"  # test
    result = addressBar(url)
    # Lặp qua từng cặp khóa-giá trị và in
    for key, value in result.items():
        print(f"{key}: {value}")