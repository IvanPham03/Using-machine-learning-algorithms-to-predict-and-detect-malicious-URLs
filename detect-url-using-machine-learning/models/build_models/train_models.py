import os
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, confusion_matrix, classification_report
import numpy as np
# Load và xử lý dữ liệu
def train(X, y):
    # Tách tập dữ liệu
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # Danh sách các mô hình
    classifiers = {
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42),
        "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
        "SVM": SVC(random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(),
        "Decision Tree": DecisionTreeClassifier(random_state=42)
    }

    # Huấn luyện và lưu model
    for name, clf in classifiers.items():
        # Huấn luyện mô hình
        clf.fit(X_train, y_train)
        
        # Dự đoán nhãn và xác suất
        y_pred = clf.predict(X_test)
        # Dự đoán xác suất, nếu có
        y_pred_prob = clf.predict_proba(X_test) if hasattr(clf, 'predict_proba') else None
        
        # Tính toán các chỉ số đánh giá
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')  # Sử dụng 'weighted' để tính F1-Score cho multi-class
        # Tính ROC-AUC
        if y_pred_prob is not None:
            n_classes = len(np.unique(y_test))  # Số lớp trong y_test
            if y_pred_prob.shape[1] == n_classes:
                # Nếu số lớp trong y_true khớp với số cột trong y_pred_prob
                if n_classes == 2:  # Binary classification
                    roc_auc = roc_auc_score(y_test, y_pred_prob[:, 1])  # Chỉ chọn cột thứ 2 cho AUC
                else:  # Multiclass classification
                    roc_auc = roc_auc_score(y_test, y_pred_prob, multi_class='ovr')
            else:
                roc_auc = "N/A"
        else:
            roc_auc = "N/A"
        
        # In kết quả
        print(f"{name} Accuracy: {accuracy}")
        print(f"{name} F1-Score: {f1}")
        print(f"{name} ROC-AUC: {roc_auc}")
        # In ma trận nhầm lẫn
        print(f"{name} Confusion Matrix:")
        cm = confusion_matrix(y_test, y_pred)
        print(cm)
        print(classification_report(y_test, y_pred))
        # Lưu model
        model_path = os.path.join(os.getcwd(), f"models/build_models/saved_models/{name.replace(' ', '_').lower()}_model.pkl")
        joblib.dump(clf, model_path)
        print(f"{name} model saved to {model_path}")
