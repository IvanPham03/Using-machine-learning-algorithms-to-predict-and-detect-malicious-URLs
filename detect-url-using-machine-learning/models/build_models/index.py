#chạy toàn bộ pipeline (preprocess, train models, và ensemble)
# import 
import os
from preprocess import preprocess_data
from train_models import train
from ensemble_model import ensemble_predict
from sklearn.metrics import accuracy_score

def main():
    data_path = os.path.join(os.getcwd(), 'data/processed/extracted_features150k.csv')
    
    print("Preprocessing data...")
    data, label_encoders, scaler, X, y = preprocess_data(data_path)
    print("Data preprocessing completed.")

    print("Training models...")
    train(X, y)
    print("Model training completed.")
    
    print("Ensembling models...")
    ensemble_preds = ensemble_predict(X)
    accuracy = accuracy_score(y, ensemble_preds)
    print(f"Ensemble Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()