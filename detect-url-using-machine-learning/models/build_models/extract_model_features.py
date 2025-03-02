import joblib
import numpy as np
import os
import pandas as pd
from sklearn.metrics import f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from preprocess import preprocess_data

# Đảm bảo lấy đường dẫn tuyệt đối đến thư mục chứa mô hình
current_path = os.path.dirname(os.path.abspath(__file__))  # Đường dẫn đến thư mục hiện tại của script

# Hàm load model và trích xuất top 20 feature quan trọng
def extract_model_features_and_evaluate(model_paths, X_test, y_test, feature_names=None, top_n=20):
    result = []

    # Chuyển X_test thành numpy.ndarray và reshape nếu cần
    if isinstance(X_test, pd.DataFrame):  # Kiểm tra nếu X_test là DataFrame
        X_test = X_test.to_numpy()  # Chuyển đổi DataFrame sang numpy.ndarray

    if len(X_test.shape) == 1:  # Kiểm tra nếu X_test là mảng 1D
        X_test = X_test.reshape(-1, 1)  # Chuyển thành mảng 2D nếu cần

    for model_path in model_paths:
        if not os.path.exists(model_path):  # Kiểm tra nếu file tồn tại
            print(f"Model file not found: {model_path}")
            continue

        try:
            model = joblib.load(model_path)  # Load mô hình từ file .pkl
            model_info = {"model_path": model_path}

            y_pred = model.predict(X_test)
            y_pred_prob = model.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

            # Tính toán các chỉ số đánh giá
            model_info["f1_score"] = f1_score(y_test, y_pred, average='weighted')  # Đối với multiclass
            model_info["roc_auc"] = roc_auc_score(y_test, y_pred_prob, multi_class='ovr') if y_pred_prob is not None else "N/A"

            result.append(model_info)

        except Exception as e:
            print(f"Error loading or processing model {model_path}: {e}")
            continue

    return result


# Ví dụ cách sử dụng hàm
if __name__ == "__main__":
    # Đường dẫn đến các mô hình đã lưu
    model_paths = [
        os.path.join(current_path, "saved_models/random_forest_model.pkl"),
        os.path.join(current_path, "saved_models/gradient_boosting_model.pkl"),
        os.path.join(current_path, "saved_models/k-nearest_neighbors_model.pkl"),
        os.path.join(current_path, "saved_models/logistic_regression_model.pkl"),
        os.path.join(current_path, "saved_models/decision_tree_model.pkl"),
        os.path.join(current_path, "saved_models/svm_model.pkl"),
    ]

    # Đọc X_test, y_test từ dữ liệu của bạn (cần thay thế bằng tập dữ liệu thực tế)
    # Ví dụ: X_test, y_test = load_test_data() 
    # Thay thế dòng dưới đây bằng cách tải dữ liệu thực tế
    data_path = os.path.join(os.getcwd(), 'data/processed/extracted_features630k.csv')
    data, label_encoders, scaler, X, y = preprocess_data(data_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)
    feature_names = [f"Feature_{i}" for i in range(X_test.shape[1])]

    # Gọi hàm
    results = extract_model_features_and_evaluate(model_paths, X_test, y_test, feature_names)

    # In kết quả
    for res in results:
        print(f"Model: {res['model_path']}")
        print(f"F1-Score: {res['f1_score']}")
        print(f"ROC-AUC: {res['roc_auc']}")
        print("Top Features:")
        # for name, value in res["top_features"]:
        #     print(f"  {name}: {value}")
        print("-" * 50)
