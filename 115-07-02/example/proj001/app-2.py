from flask import Flask, redirect, url_for

# 建立 Flask 應用程式
app = Flask(__name__)

# 設定首頁路由
@app.route("/")
def home():
    # Flask 內建 static 路由，只要指定 filename 參數即可
    return redirect(url_for('static', filename='index.html'))
# 啟動伺服器
if __name__ == "__main__":
    app.run(debug=True)