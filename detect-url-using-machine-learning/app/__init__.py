# File khởi tạo ứng dụng Flask
from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    # Cấu hình cơ bản
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['DEBUG'] = True

    # Kích hoạt CORS
    CORS(app)

    # Đăng ký route
    from .routes import api
    app.register_blueprint(api)

    return app
