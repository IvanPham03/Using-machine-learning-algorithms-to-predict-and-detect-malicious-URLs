from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

class Result:
    def __init__(self):
        self.response = []
        self.errors = []

    def add_response(self, response_message):
        self.response.append(response_message)
        
    def add_error(self, error_message):
        self.errors.append(error_message)
def dom(url):
    result = Result()
    features = {
        'credit_card_present': False,
        'log_present': False,
        'pay_present': False,
        'free_present': False,
        'bonus_present': False,
        'click_present': False,
        'num_hidden_elements': 0,
        'num_js': 0,
        'num_external_js_files': 0,
        'num_iframes': 0,
        'num_embed': 0,
        'num_object': 0,
        'num_form': 0,
        'num_links': 0,
        'num_external_links': 0,
        'num_internal_links': 0,
        'page_size': 0,
    }
    try:
        response = requests.get(url, timeout=1, allow_redirects=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
        response.raise_for_status()  # Kiểm tra trạng thái HTTP
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        result.add_response(soup)
        # Features related to content
        credit_card_present = 'credit card' in text.lower()
        log_present = 'log' in text.lower()
        pay_present = 'pay' in text.lower()
        free_present = 'free' in text.lower()
        bonus_present = 'bonus' in text.lower()
        click_present = 'click' in text.lower()

        # Features related to HTML structure
        num_hidden_elements = len(soup.find_all(style=lambda value: value and 'display:none' in value))
        num_js = len(soup.find_all('script'))
        num_external_js_files = len([script for script in soup.find_all('script') if script.get('src')])
        num_iframes = len(soup.find_all('iframe'))
        num_embed = len(soup.find_all('embed'))
        num_object = len(soup.find_all('object'))
        num_form = len(soup.find_all('form'))

        # Features related to links
        num_links = len(soup.find_all('a'))
        num_external_links = len([a for a in soup.find_all('a', href=True) if urlparse(a['href']).netloc != ''])
        num_internal_links = len([a for a in soup.find_all('a', href=True) if urlparse(a['href']).netloc == ''])

        # General features
        page_size = len(response.content)
        features.update({
                'credit_card_present': credit_card_present,
                'log_present': log_present,
                'pay_present': pay_present,
                'free_present': free_present,
                'bonus_present': bonus_present,
                'click_present': click_present,
                'num_hidden_elements': num_hidden_elements,
                'num_js': num_js,
                'num_external_js_files': num_external_js_files,
                'num_iframes': num_iframes,
                'num_embed': num_embed,
                'num_object': num_object,
                'num_form': num_form,
                'num_links': num_links,
                'num_external_links': num_external_links,
                'num_internal_links': num_internal_links,
                'page_size': page_size,
                
            })
    except requests.exceptions.RequestException as e:
        result.add_error(e)
        # print(f"Error fetching URL: {e}")
    features.update({
        'response_DOM': result.response, 
        'errors_DOM': result.errors 
    })
    return features
if __name__ == "__main__":
    url = "https://www.kaggle.com/code/"  # test
    result = dom(url)
    # Lặp qua từng cặp khóa-giá trị và in
    for key, value in result.items():
        print(f"{key}: {value}")
        