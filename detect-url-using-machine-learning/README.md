# Phát hiện URLs độc hại bằng thuật toán học máy và học sâu / Using machine learning algorithms to predict and detect malicious URLs
Nghiên cứu này tập trung vào việc xây dựng mô hình học máy để phát hiện URL độc hại, sử dụng tập dữ liệu từ Kaggle. Các URL được tiền xử lý và trích xuất đặc trưng (độ dài, ký tự đặc biệt, domain). Mô hình Random Forest cho kết quả tốt nhất trên 651,191 URL, và Ensemble Learning cũng cho độ chính xác cao (97%). Kết quả này ứng dụng để xây dựng website phát hiện URL độc hại, link dự án đã triển khai: https://unity-demo-detect-url.vercel.app

# Cấu trúc & cài đặt dự án
Cấu trúc dự án gồm 2 phần: 
## Backend (folder : backend_detect_url_flask-main)
### Cấu trúc
- folder app: Ứng dụng Flask chính, bao gồm các route API để nhận yêu cầu và trả về kết quả dự đoán.
- folder data: Chứa dữ liệu huấn luyện, dữ liệu đã qua xử lý, và các script tiền xử lý dữ liệu.
- folder models: Chứa các model đã được huấn luyện và script huấn luyện model.
- folder extract_features: Chứa các hàm và script để trích xuất đặc trưng từ URL, phục vụ cho việc dự đoán.
- file requirements.txt: liệt kê các package và phiên bản của dự án.
### Cài đặt
- Tạo môi trường ảo tên venv: 
``` python -m venv venv ```
- Kích hoạt môi trường ảo: 
source venv/bin/activate (Linux/Mac) / venv\Scripts\activate (Windows): 
- Cài các package từ file requirements.txt vào môi trường ảo: 
``` pip install -r requirements.txt ```
- Chạy dự án (Ứng dụng sẽ chạy tại địa chỉ http://127.0.0.1:5000. Bạn có thể sử dụng Postman hoặc curl để test các API endpoints): 
``` python run.py ```

## UI/Frontend (folder: unity-demo-detect-url-main)
### Cấu trúc
- folder api: Xử lý logic giao tiếp với backend API.
- folder assets: Tài nguyên tĩnh (hình ảnh, icon, font).
- folder components: Các component UI có thể tái sử dụng(Alert, Spinner..).
- folder pages: Các trang của ứng dụng.
- folder redux-toolkit: Quản lý trạng thái của ứng dụng.
- package.json: Liệt kê các dependencies và phiên bản "cho phép" của chúng.
- package-lock.json: Ghi lại phiên bản chính xác của tất cả các dependencies.
### Cài đặt
- Tạo file .env: Tạo file .env trong thư mục gốc của dự án và thêm REACT_APP_API_DETECT_URL=http://127.0.0.1:5000 (hoặc URL API khi đã deploy).

- Cài đặt các thư viện (sẽ tạo folder node_modules): 
``` npm i ```

- Chạy dự án (để mở ứng dụng trong trình duyệt, thường là http://localhost:3000): 
``` npm start ```

## Kết quả

Cách nhập URL để kiểm tra (Lưu ý: Khi dùng thử, URL được nhập vào kiểm tra nên có đầy đủ thành phần http:// hoặc https://)
### Hiển thị kết quả.
1. Kết quả dự đoán của dự án
2. Kết quả dự đoán của Google Safe Browsing (https://developers.google.com/safe-browsing)
 
### Hiển thị kết quả phân tích đặc trưng
1. dnssec
2. creation_date
3. expiration_date
...Một số feature được trích xuất từ url (domain details).

p/s: Giao diện UI có giới thiệu demo bằng video


Tác giả: Phạm Đăng Trường và Nguyễn Hoàng Khoa.
Liên hệ: dangtruongphamvn@gmail.com để được hỗ trợ.