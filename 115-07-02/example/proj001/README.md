在 ```Flask``` 中，如果你不使用 ```templates``` 樣版資料夾，而是想讓首頁直接去讀取並回傳靜態資料夾內（```static/```）的 ```index.html```，主要有兩種寫法。
最推薦的是做法 1（使用 ```send_from_directory```），因為它的網址最乾淨；如果你希望瀏覽器網址列自動跳轉變成 ```/static/index.html```，則可以使用做法 2。
## 做法 1：直接讀取並回傳（推薦，網址保持 /）
使用 ```Flask``` 的 ```send_from_directory``` 函數。當使用者訪問首頁 http://localhost:5000/ 時，後端直接去 ```static``` 資料夾把 ```index.html``` 撈出來塞給瀏覽器，瀏覽器的網址列不會改變。

```python
# Python 程式碼 (app.py)：

from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
    # static_folder 預設就是 'static'，直接指定檔案名稱即可
    return send_from_directory(app.static_folder, 'index.html')
```
------------------------------
## 做法 2：重新導向（網址會變成 /static/index.html）
使用 ```redirect``` 搭配 ```url_for```。當使用者訪問首頁時，伺服器會告訴瀏覽器：「請改去 ```/static/index.html```」，這時瀏覽器網址列會發生變化。
```python
# Python 程式碼 (app.py)：

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    # Flask 內建 static 路由，只要指定 filename 參數即可
    return redirect(url_for('static', filename='index.html'))
```
------------------------------
## ⚠️ 注意：確保你的目錄結構正確
不論用哪種做法，你的專案目錄結構必須長這樣：
```sh
proj001/
├── app.py
└── static/         # <-- 必須是這個名字
    └── index.html  # <-- 你的首頁檔案
```
請問你目前嘗試後網頁有成功顯示嗎？如果你在 index.html 裡面還有引入其他 css 或圖片檔案，遇到路徑問題的話可以隨時告訴我！

