import pandas as pd
import os

path_data = os.path.join(os.getcwd(), 'data/processed/extracted_features630k.csv')
# Đọc file CSV
data = pd.read_csv(path_data)
# Điền giá trị NaN bằng False trước khi ép kiểu
data.fillna(False, inplace=True)

# Sau đó thực hiện chuyển đổi
data[[
    'has_www', 'has_exe', 'has_confirm', 'has_login', 'has_account', 
    'has_zip', 'has_rar', 'has_link', 'has_plugins', 'has_js', 'has_jar', 
    'has_verification', 'has_bin', 'has_php', 'credit_card_present', 
    'log_present', 'pay_present', 'free_present', 'bonus_present', 'click_present'
]] = data[[
    'has_www', 'has_exe', 'has_confirm', 'has_login', 'has_account', 
    'has_zip', 'has_rar', 'has_link', 'has_plugins', 'has_js', 'has_jar', 
    'has_verification', 'has_bin', 'has_php', 'credit_card_present', 
    'log_present', 'pay_present', 'free_present', 'bonus_present', 'click_present'
]].applymap(lambda x: 1 if x else 0)
# Danh sách các cột cần giữ nguyên
columns_to_exclude = ['url', 'type']
# Lấy danh sách các cột cần chuyển đổi
columns_to_convert = [col for col in data.columns if col not in columns_to_exclude]
# Chuyển đổi các cột sang kiểu số
for col in columns_to_convert:
    data[col] = pd.to_numeric(data[col], errors='coerce')  # Chuyển đổi giá trị không hợp lệ thành NaN

# Điền giá trị NaN (nếu có) bằng giá trị trung bình
data.fillna(data.mean(numeric_only=True), inplace=True)

# Lưu lại file CSV sau khi chuyển đổi
data.to_csv(os.path.join(os.getcwd(), 'data/processed/extracted_features630k.csv'), index=False)