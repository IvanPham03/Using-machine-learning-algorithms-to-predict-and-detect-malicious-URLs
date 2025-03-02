import joblib
import numpy as np
import os

# Đảm bảo lấy đường dẫn tuyệt đối đến thư mục chứa mô hình
current_path = os.path.dirname(os.path.abspath(__file__))  # Đường dẫn đến thư mục hiện tại của script

# Đặt đường dẫn đến thư mục chứa mô hình của bạn (có thể chỉnh sửa lại tùy theo dự án)
def ensemble_predict(url):
    models = [
        "saved_models/random_forest_model.pkl",
        "saved_models/gradient_boosting_model.pkl",
        "saved_models/k-nearest_neighbors_model.pkl",
        "saved_models/logistic_regression_model.pkl",
        "saved_models/decision_tree_model.pkl",
        "saved_models/svm_model.pkl",
    ]
    
    predictions = []
    for model_path in models:
        model_file_path = os.path.join(current_path, model_path)
        print("model_file_path:::", model_file_path)
        if not os.path.exists(model_file_path):  # Kiểm tra sự tồn tại của mô hình
            print(f"Model file not found: {model_file_path}")
            continue  # Bỏ qua nếu mô hình không tồn tại
        try:
            model = joblib.load(model_file_path)  # Load model .pkl
            predictions.append(model.predict(url))
        except Exception as e:
            print(f"Error loading model {model_file_path}: {e}")
            continue  # Bỏ qua nếu có lỗi khi load mô hình

    if not predictions:  # Nếu không có dự đoán nào
        return None
    # Lấy biểu quyết đa số
    ensemble_preds = np.array(predictions).T
    final_predictions = [np.bincount(row).argmax() for row in ensemble_preds]

    return final_predictions
