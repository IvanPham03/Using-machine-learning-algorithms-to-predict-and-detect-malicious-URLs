# Định nghĩa các route API
from flask import Blueprint, jsonify, request
import pandas as pd
from extract_features.featureExtraction import featureExtraction
from models.build_models.ensemble_model import ensemble_predict
from extract_features.GoogleSafe import check_url
# Tạo blueprint
api = Blueprint('api', __name__)

@api.route('/api/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'url' not in data:
            return jsonify({"error": "Missing 'url' field in request"}), 400 

        input_url = data['url'] 
        
        # extract feature from input url
        # Now you can access the results:
        result_extract = featureExtraction(input_url) 
        handle_request = result_extract['handle_request'] 
        feature_extracted = result_extract['feature_extracted'] 
        # print(feature_extracted)
        df_input_url = pd.DataFrame([feature_extracted]) 
        predict = ensemble_predict(df_input_url)
        print("ensemble_predict:::", predict)
        print("feature:::", feature_extracted)
        
        response_domain = handle_request['response_domain']
        print("response_domain:::", response_domain)
        # print("handle_request:::", handle_request)
        # in ra xem kết quả dự đoán
        label_mapping = {
            0: "Benign",
            1: "defacement",
            2: "malware",
            3: "phishing"
        }
        if predict is not None:
            return jsonify({"Prediction": label_mapping.get(predict[0], "Unknown"), 'response_domain': handle_request['response_domain']})
        else:
            return jsonify({"error": "Prediction failed, no model output."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route('/api/google-safe-browsing', methods=['POST'])
def handle_data():
    try:
        data = request.json

        # Ensure 'url' is present in the JSON payload
        if not data or 'url' not in data:
            return jsonify({"error": "Invalid request. 'url' field is required."}), 400

        url = data['url']

        # Check the URL using Google Safe Browsing API
        result = check_url(url)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
