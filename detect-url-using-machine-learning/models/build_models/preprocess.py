import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(file_path):
    # Load dữ liệu
    # print(file_path)
    data = pd.read_csv(file_path)

    data = data.drop(['url'], axis=1)
    # Đếm số lượng hàng trùng lặp
    print("Count duplicate rows:", data.duplicated().sum())
    # Loại bỏ các hàng trùng lặp
    data = data.drop_duplicates()
    # Đếm số lượng hàng trùng lặp sau drop
    print("Count the number of duplicate rows after drop:", data.duplicated().sum())
    path = os.path.join(os.getcwd(), 'preprocessed.csv')
    data.to_csv(path, index=False)

    # # Danh sách các cột cần xử lý
    # columns_to_convert = [
    #     'url_length', 'ip_in_hostname', 'query_length', 'token_count',
    #     'entropy', 'tinyURL', 'httpDomain', 'depth', 'double_slash_redirecting', 'dots',
    #     'hyphens', 'underscores', 'equals', 'forward_slashes', 'question_marks', 
    #     'semicolons', 'open_parentheses', 'close_parentheses', 'mod_signs', 'ampersands',
    #     'at_the_rate', 'digits', 'has_www', 'has_exe', 'has_confirm', 'has_login', 
    #     'has_account', 'has_zip', 'has_rar', 'has_link', 'has_plugins', 'has_js', 'has_jar',
    #     'has_verification', 'has_bin', 'has_php', 'owner_infor', 'web_traffic', 'create_date',
    #     'expiry_date', 'dns_servers', 'dnssec', 'credit_card_present', 'log_present', 
    #     'pay_present', 'free_present', 'bonus_present', 'click_present', 'num_hidden_elements', 
    #     'num_js', 'num_external_js_files', 'num_iframes', 'num_embed', 'num_object', 'num_form', 
    #     'num_links', 'num_external_links', 'num_internal_links',
    # ]

    # # Chuyển đổi tất cả các giá trị trong cột thành chuỗi
    # for col in columns_to_convert:
    #     data[col] = data[col].apply(str)

    # # Tạo đối tượng LabelEncoder
    # label_encoder = LabelEncoder()

    # # Thực hiện Label Encoding cho các cột
    # for col in columns_to_convert:
    #     data[col] = label_encoder.fit_transform(data[col])

    # # In ra DataFrame sau khi đã Label Encoding
    # print(data.head())

    # Xác định loại dữ liệu
    object_cols = data.select_dtypes(include=['object']).columns
    numeric_cols = data.select_dtypes(include=['number']).columns
    unique_values = data['pay_present'].unique()
    print("Các giá trị trong cột 'pay_present':", unique_values)
    print(data['pay_present'].value_counts(dropna=False))
    # Label Encoding cho object columns
    label_encoders = {}
    for col in object_cols:
        # Điền giá trị thiếu trước khi Label Encoding
        if data[col].isnull().any():
            print(f"Xử lý giá trị thiếu trong cột '{col}'...")
            data[col].fillna("missing", inplace=True)  # Điền giá trị mặc định cho NaN

        # Tiếp tục xử lý như trên
        if not data[col].map(type).nunique() == 1:
            print(f"Cột '{col}' chứa dữ liệu không đồng nhất. Chuyển đổi tất cả về chuỗi.")
            data[col] = data[col].astype(str)
            
        print(f"Label Encoding cho cột '{col}'...")
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le

    # Standard Scaling cho numeric columns
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

    # Xử lý giá trị thiếu
    for col in data.columns:
        if data[col].isnull().any():
            if pd.api.types.is_numeric_dtype(data[col]):
                data[col].fillna(data[col].mean(), inplace=True)
            else:
                data[col].fillna(data[col].mode()[0], inplace=True)

    X = data.drop(['type'], axis=1) 
    y = data['type']  # target 'type'
    print("------------------------")
    print(y)
    
    return data, label_encoders, scaler, X, y

def preprocess_test(file_path):
    # Load dữ liệu
    # print(file_path)
    data = pd.read_csv(file_path)

    data = data.drop(['url'], axis = 1)
    # Đếm số lượng hàng trùng lặp
    print("Count duplicate rows:", data.duplicated().sum())
    # Loại bỏ các hàng trùng lặp
    data = data.drop_duplicates()
    # Đếm số lượng hàng trùng lặp sau drop
    print("Count the number of duplicate rows after drop:", data.duplicated().sum())
    # Xác định loại dữ liệu
    object_cols = data.select_dtypes(include=['object']).columns
    numeric_cols = data.select_dtypes(include=['number']).columns

    # Label Encoding cho object columns
    label_encoders = {}
    for col in object_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le
    
    # Standard Scaling cho numeric columns
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

    # Xử lý giá trị thiếu
    for col in data.columns:
        if data[col].isnull().any():
            if pd.api.types.is_numeric_dtype(data[col]):
                data[col].fillna(data[col].mean(), inplace=True)
            else:
                data[col].fillna(data[col].mode()[0], inplace=True)

    X = data.drop(['type'], axis=1)  # feature 'url' bằng cột không dùng để huấn luyện
    y = data['type']  # target 'type'
    # Hiển thị thông tin chi tiết của LabelEncoder
    if 'type' in label_encoders:
        le = label_encoders['type']
        print("Classes của LabelEncoder cho 'type':", le.classes_)
        print("Mapping (class -> label):", dict(zip(le.classes_, le.transform(le.classes_))))
    else:
        print("Không tìm thấy LabelEncoder cho cột 'type'")
    return data, label_encoders, scaler, X, y

