## 【人工智慧工具應用實務班第01期】- 115年07月07日
## （08:00 ~ 12:00）工作自動化流程（趙伯元）
### [Google Search AI - Local n8n Configuration](https://www.google.com/search?q=%E9%8C%AF%E8%AA%A4+400%EF%BC%9Aredirect_uri_mismatch+%E9%80%99%E5%80%8B%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E4%B8%8D%E7%AC%A6%E5%90%88+Google+%E7%9A%84+OAuth+2.0+%E6%94%BF%E7%AD%96%E8%A6%8F%E5%AE%9A%EF%BC%8C%E5%9B%A0%E6%AD%A4%E6%82%A8%E7%84%A1%E6%B3%95%E7%99%BB%E5%85%A5%E3%80%82+%E5%A6%82%E6%9E%9C%E6%82%A8%E6%98%AF%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E9%96%8B%E7%99%BC%E4%BA%BA%E5%93%A1%EF%BC%8C%E8%AB%8B%E5%89%8D%E5%BE%80+Google+Cloud+Console+%E8%A8%BB%E5%86%8A%E9%87%8D%E6%96%B0%E5%B0%8E%E5%90%91+URI%E3%80%82+%E8%A6%81%E6%B1%82%E8%A9%B3%E6%83%85%EF%BC%9A+redirect_uri%3Dhttps%3A%2F%2Flocalhost%3A5678%2Frest%2Foauth2-credential%2Fcallback+flowName%3DGeneralOAuthFlow+%E7%9B%B8%E9%97%9C%E9%96%8B%E7%99%BC%E4%BA%BA%E5%93%A1%E8%AA%AA%E6%98%8E%E6%96%87%E4%BB%B6&sca_esv=be347a12b1877155&sxsrf=APpeQnsoEj__CO8a8o112OSNFfMru1BgVw%3A1783393158135&source=chrome.ob&fbs=ABfTbFUhNGvvPEUFOvrsPMHwBXgOBaujescnqPHvnnJ8fnHu17PbcurfovuKKjl7m0lU4CiLSYQPEkTlW_XHD51KmT6Zu02gdc-s8eQZrGdycu9M6BNkpSbOedJtWzwQK_avfWU3EuHq0quUIliKjFeRaT2z0ZN6EWJs01gGUplekX34Nr9f2iN1B2r6zBnPRJLMR61jhXuQ&aep=1&ntc=1&sa=X&ved=2ahUKEwjjv72dyb-VAxXtkq8BHYyxA9QQ2J8OegQIExAD&biw=1920&bih=890&dpr=1&mstk=AUtExfDsMz6yeFBToam2t6IWYtCPvg6toT97KiIgp_UUOM6uMGnwXo-s8P_52kqLU-bHnb7Q1J1Hrgu2suLxKnfoJp2lff_zepamMEmKa8rZCdsuIZXmaAoqk3gohPC1JrHeFKJaq1-MG8kJjLL5AtFSXP2ly2HgBo85UDGsWRskY6zHLBcLPwmqyqJP62ddmjojUrxjefaONvnCRLsViH5dRsJjeZIQ--fq-EhBEaB1vCPrYJASaCtMowHpEPTep_ExBLryMZWuQC2X2MaDoD-6hi5Gyvdtf_xZSTGED34lxiFiI7CtJeaWNjlKof5Kq3F0i2QdhuzDoWw2MA&csuir=1&mtid=jmtMarv0BNKTvr0PoNyk2Qs&udm=50)
### [課程資料](n8n-docs/README.md) 
###
## （13:00 ~ 17:00）Python Flask 框架（徐偉智）
### 
### 在開發階段 將偵錯（Debug）模式啟動
```python
app.run(debug=True)
```
### URL 由設定・http:/IP address:portNumber/myimg 就會執行 def image() function
```python
@app.route("/my_img")
def image():
    return send file("test.jpg", mimetype= 'image/jpeg")
```
### 動態（dynamnic）與靜（（static） 資源
 - html 檔在Browser發出Request後 其所呈現的內容都不變就是靜態。
 - ttml檔檔在Browser發出Request後・其所呈現的內容會變・就是動態，會有 Jinja2 語法。
 - jpg` CSS、js....等檔案 、不會因Request而改變內容 、所以是static。
### Python Flask Web Framework 的慣例
 - 靜態資源會儲存在 static 資料夾下。
 - 動態 html 檔會儲存在 templates 下。
 - 當 index.html是靜態網頁時 、在 ```app.py``` 內使用 ```send_file(..)``` 將靜態資源response回 Browser 、 專案目錄結構是這樣
```sh
mypro i
    app.py
    index.html
    static/     # 靜態資源
    templates/  # 動態資源
```
 - 比較正規的作法 : 將 index.html 也儲存在 static 內 ,並將 ```send_file()``` 改用 ```send_static_file()```。
 ```python
 @app.rounte("/")
 def home():
    return app.send_static_file("index.html") #將 static 下的 index.html 傳送至 Brower
 ```
 - 1. app 物件有一個函式 send_static_file()
 - 2. 物件.函式
### 動熊網頁範例
```python
@app.route("/dynamic")
def dynamic():
    # 隨機生成一個 0 到 50 的數字，儲存到 dog 的變數中
    dog = random.randint(0, 50)
    print(dog)
    return render_template("locky.html", num = dog) # 將 dog 變數傳給 locky.html
```