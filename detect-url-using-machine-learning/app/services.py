# Xử lý logic ứng dụng
def preprocess_data(data):
    """Tiền xử lý dữ liệu đầu vào trước khi đưa vào model."""
    # Giả sử data là một dict với các feature cần thiết
    return [data.get('feature1', 0), data.get('feature2', 0), data.get('feature3', 0)]
