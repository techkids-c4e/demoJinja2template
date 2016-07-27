from flask import Flask

app = Flask(__name__) # khởi tạo flask

# cấu hình đường dẫn ở trang chủ
@app.route('/')
def index():
    return "Hello world"

# bắt đầu chạy chương trình
if __name__ == "__main__":
    app.run()

