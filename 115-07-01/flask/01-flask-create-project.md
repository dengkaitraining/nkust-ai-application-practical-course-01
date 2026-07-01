### 1. 安裝 Flask
透過終端機執行以下指令來安裝套件：
#### windows 環境安裝 Flask
```sh
pip install flask
```
#### ubuntu 環境安裝 Flask
```sh
sudo pip install flask --break-system-packages
```
### 2. 建立應用程式
新增一個名為 app.py 的檔案，並寫入以下程式碼：
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```
### 3. 動伺服器
在終端機輸入執行指令：
```sh
python app.py
```
 ### 核心特色與架構
  - WSGI 基底：基於 Werkzeug WSGI 工具箱處理請求與響應。
  - Jinja2 模板：內建強大的 Jinja 模板引擎，能將後端資料直接渲染至 HTML 頁面。
  - 高度擴展性：核心僅提供 URL 路由與頁面轉譯，進階功能（如資料庫 ORM、表單驗證等）皆可透過擴充套件 (Extensions) 靈活組裝。

### 學習資源與文件
想了解更多進階功能（如路由設定、請求處理、資料庫整合等），建議直接參考官方釋出的指南與教學：
 - 官方網站與完整文件：請參閱 [Flask Documentation](https://flask.palletsprojects.com/)。
 - 官方入門教學與實作：請參考 [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)。 

#### 參考資料
 - [Google AI Search](https://www.google.com/search?q=python+flask&oq=python+flask&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDg1MDdqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8)
 - [Flask Documentation](https://flask.palletsprojects.com/)
 - [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/)
 - [Flask 維基百科](https://zh.wikipedia.org/zh-tw/Flask)
 - [使用 Flask 製作網站](https://pythonbook.cc/chapters/flask/hello-flask)
 - [教學課程：在Visual Studio中使用 Flask Web 架構](https://learn.microsoft.com/zh-tw/visualstudio/python/learn-flask-visual-studio-step-01-project-solution?view=visualstudio)