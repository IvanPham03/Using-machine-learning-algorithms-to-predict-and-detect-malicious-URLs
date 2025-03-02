from .URLFeatures import URLFeatures

# 1 if the URL is Phishing,
# -1 if the URL is Legitimate and
# 0 if the URL is Suspicious

def featureExtraction(url):
    url_features = URLFeatures(url)
    
    # Lấy tất cả các đặc điểm của URL
    result = url_features.get_all_features()
    
    # Define the desired order of features
    feature_order = [
        'url_length', 'ip_in_hostname', 'query_length', 'token_count', 'entropy', 'tinyURL', 'httpDomain', 'depth', 
        'double_slash_redirecting', 'dots', 'hyphens', 'underscores', 'equals', 'forward_slashes', 'question_marks', 
        'semicolons', 'open_parentheses', 'close_parentheses', 'mod_signs', 'ampersands', 'at_the_rate', 'digits', 
        'has_www', 'has_exe', 'has_confirm', 'has_login', 'has_account', 'has_zip', 'has_rar', 'has_link', 'has_plugins', 
        'has_js', 'has_jar', 'has_verification', 'has_bin', 'has_php', 'owner_infor', 'web_traffic', 'create_date', 
        'expiry_date', 'dns_servers', 'dnssec', 'credit_card_present', 'log_present', 'pay_present', 'free_present', 
        'bonus_present', 'click_present', 'num_hidden_elements', 'num_js', 'num_external_js_files', 'num_iframes', 
        'num_embed', 'num_object', 'num_form', 'num_links', 'num_external_links', 'num_internal_links', 'page_size'
    ]
    # Extract features while maintaining the desired order
    feature_extracted = {k: result[k] for k in feature_order if k in result}
    # Tạo object mới với 2 thuộc tính
    # Tạo một dictionary mới để chứa giá trị của handle_request
    # còn lại feature_extracted
    new_object = {
        'handle_request': {k:v for k, v in result.items() if k in ['response_DOM', 'errors_DOM', 'response_domain', 'errors_domain']},
        'feature_extracted': feature_extracted
    }
    return new_object


if __name__ == '__main__':
    featureExtraction('https://translate.google.com/?sl=en')