from flask import Flask, send_from_directory

# 建立 Flask 應用程式
app = Flask(__name__)

# 首頁
@app.route('/')
def home():
    # static_folder 預設就是 'static'，直接指定檔案名稱即可
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/my_page')
def my_page():
    return send_from_directory(app.static_folder, 'my_page.html')

@app.route('/about')
def about():
    return send_from_directory(app.static_folder, 'about.html')

if __name__ == "__main__":
    app.run(debug=True)