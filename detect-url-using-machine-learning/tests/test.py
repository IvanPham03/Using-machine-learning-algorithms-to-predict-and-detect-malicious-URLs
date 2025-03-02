from sklearn.metrics import accuracy_score
import os 
import pandas as pd
# tests/test.py
import sys
import os

# Thêm thư mục gốc vào PYTHONPATH
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from models.build_models.ensemble_model import ensemble_predict
from models.build_models.preprocess import preprocess_data

current_path = os.getcwd()

def test_predict_multiple_row():
    data_path = os.path.join(os.getcwd(), 'tests/extracted_test.csv')
    # Define the desired order of features
    print("Preprocessing data...")
    data, label_encoders, scaler, X, y = preprocess_data(data_path)
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
    X = X[feature_order] # ensure correct order
    ensemble_preds = ensemble_predict(X)
    # print(ensemble_preds)
    accuracy = accuracy_score(y, ensemble_preds)
    print(f"Ensemble Accuracy: {accuracy:.2f}")
    # Hiển thị thông tin chi tiết của LabelEncoder
    # if 'type' in label_encoders:
    #     le = label_encoders['type']
    #     print("Classes của LabelEncoder cho 'type':", le.classes_)
    #     print("Mapping (class -> label):", dict(zip(le.classes_, le.transform(le.classes_))))
    # else:
    #     print("Không tìm thấy LabelEncoder cho cột 'type'")
if __name__ == '__main__':
    test_predict_multiple_row()