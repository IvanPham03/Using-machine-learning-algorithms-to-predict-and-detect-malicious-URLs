import os
import pandas as pd
from URLFeatures import URLFeatures

current_dir = os.getcwd()

# 1 if the URL is Phishing,
# -1 if the URL is Legitimate and
# 0 if the URL is Suspicious

def main():
    data_path = os.path.join(current_dir, 'data/processed/extracted_dataset.csv')
    data = pd.read_csv(data_path)
    
    # -------------------------------------
    # Lấy ngẫu nhiên 10000 dòng từ data
    # random_sample = data.sample(n=10000, random_state=42)
    # for index, row in data.iloc[0:10000].iterrows():
    # Lặp qua từng dòng trong sample ngẫu nhiên
    # for count, (index, row) in enumerate(random_sample.iterrows(), start=1):
    # -------------------------------------
    
    # Lặp qua từng dòng trong data và tạo đối tượng URLFeatures cho từng dòng
    start = 34510
    end = 35000
    for count, (index, row) in enumerate(data.iloc[start:end].iterrows(), start=1):
        # In số thứ tự dòng trong quá trình lặp
        print(f"Processing row {count}/{end} (index: {index})")
        # print(f"Processing row {count}/{len(random_sample)} (index: {index})")
        # Tạo đối tượng URLFeatures cho từng URL
        url_features = URLFeatures(row['url'])
        
        # Lấy tất cả các đặc điểm của URL
        features = url_features.get_all_features()
        # thêm url và type vào để sau này kiểm tra dữ liệu
        features['url'] = row['url']
        features['type'] = row['type'] 
        
        data = []
        data.append(features)
        df = pd.DataFrame(data)
        # Đảm bảo 'url' và 'type' là cột đầu tiên
        cols = ['url', 'type'] + [col for col in df.columns if col not in ['url', 'type']]
        df = df[cols]
        
        # Đường dẫn tới file CSV
        output_path = os.path.join(os.getcwd(), f'data/processed/extracted_features_1_50k.csv')

        # Kiểm tra nếu file đã tồn tại, nếu không thì tạo mới
        if os.path.exists(output_path):
            # Thêm dữ liệu vào file mà không ghi đè (mode='a') và không ghi tiêu đề cột (header=False)
            df.to_csv(output_path, mode='a', header=False, index=False)
        else:
            # Nếu file không tồn tại, tạo mới và ghi tiêu đề cột
            df.to_csv(output_path, mode='w', header=True, index=False)
if __name__ == "__main__":
    main()    