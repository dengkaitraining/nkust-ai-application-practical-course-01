from flask import Flask, send_from_directory

# 建立 Flask 應用程式
app = Flask(__name__)
app.static_folder = 'static'  # 指定靜態檔案資料夾名稱
app.template_folder = 'templates'  # 指定模板資料夾名稱
app.template_auto_reload = True  # 啟用模板自動重新載入
app.static_url_path = '/static'  # 指定靜態檔案 URL 路徑

# 首頁
@app.route('/')
def home():
    # static_folder 預設就是 'static'，直接指定檔案名稱即可
    # 將 index.html 送到 Browser
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/my_img')
def my_img():
    return send_from_directory(app.static_folder, '1-web-app-1.png', mimetype='image/jpeg')

@app.route('/my_page')
def my_page():
    return send_from_directory(app.static_folder, 'my_page.html')

@app.route('/my_doc')
def my_doc():
    return send_from_directory(app.static_folder, 'my_doc.docx', mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

@app.route('/about')
def about():
    return send_from_directory(app.static_folder, 'about.html')

if __name__ == "__main__":
    app.run(debug=True, port=5010)