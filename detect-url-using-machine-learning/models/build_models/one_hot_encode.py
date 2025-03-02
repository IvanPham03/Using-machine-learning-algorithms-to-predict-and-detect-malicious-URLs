import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os

data_path = os.path.join(os.getcwd(), 'backend-detect-url-flask/data/processed/extracted_features.csv')

def one_hot_encode(file_path):
    # Load dữ liệu
    data = pd.read_csv(file_path)
    
    # Tách cột 'url'
    url_df = data[['url']]
    
    # Thực hiện One-Hot Encoding
    encoder = OneHotEncoder(sparse=False)
    url_encoded = encoder.fit_transform(url_df)
    url_encoded = pd.DataFrame(url_encoded, columns=encoder.get_feature_names_out(['url']))

    # Gom tất cả các cột One-Hot Encoding thành 1 cột duy nhất 'vector_one_hot'
    url_encoded['vector_one_hot'] = url_encoded.apply(lambda row: row.values.tolist(), axis=1)
    url_encoded = url_encoded[['vector_one_hot']]  # Chỉ giữ cột vector_one_hot

    # Kết hợp lại với cột 'url'
    result_data = pd.concat([url_df, url_encoded], axis=1)

    # Xuất file one-hot encoding kèm theo vector_one_hot
    data_export = os.path.join(os.getcwd(), 'backend-detect-url-flask/models/build_models/url_encoded_with_vector_one_hot.csv')
    result_data.to_csv(data_export, index=False) 

    print("Saved One-Hot Encoding with vector_one_hot and url")

if __name__ == '__main__':
    one_hot_encode(data_path)
