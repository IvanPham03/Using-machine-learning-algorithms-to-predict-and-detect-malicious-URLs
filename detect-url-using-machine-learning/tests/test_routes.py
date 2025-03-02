import requests

url = "http://127.0.0.1:5000/api/predict" 
# url = "https://backend-detect-url-flask.onrender.com/api/predict" # link api đã deploy lên
# data = {"url": 'https://www.youtube.com/watch?v=X2VNJBBqSUA'}  # Dữ liệu đầu vào
# data = {"url": 'https://gemini.google.com/app/00d64b9ed9cf0b76'}  # Dữ liệu đầu vào (muốn cái nào thì thay cái đó vào)
data = {"url": 'https://docs.google.com/spreadsheets/u/0/'}  # Dữ liệu đầu vào (muốn cái nào thì thay cái đó vào)

response = requests.post(url, json=data)
# Kiểm tra trạng thái của phản hồi
if response.status_code == 200:
    print(response.json())  # In ra kết quả dự đoán
else:
    print(f"Error: {response.status_code}")
    print(response.json())
