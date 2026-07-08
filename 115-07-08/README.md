## 【人工智慧工具應用實務班第01期】- 115年07月08日
## （08:00 ~ 12:00）檢索增強生成應用系統開發（徐偉智）
### HTML hyperlink ```<a>``` 會超連結到一個資源 ```(Resource)```，實際上就是發出 ```Request``` ，要求 ```Request``` 所要求資源回到 ```Browser```。
 - 所謂 ```resource``` 可以是 ```html``` 檔，```jpg``` 檔...或任何其他檔。
 - ```resource``` 也可以是 Python Flask 的一個 ```route```，```@app.route("/dynamic")``` 會invoke (觸發)該 route 底下的函式執行。
 - ```<a href="/dynamic">中獎了</a><p>``` 使用者 ```click``` 之後就會觸發 ```@app.route("/dynamic")``` 的函式執行。
 ```python
 @app.route("/dynamic")
 def dynamic(
     # 隨機生成一個0到50的數字 、儲存到 doe 變數
     dog = random.randint(0, 50)
     print(dog)
     return render template()"lucky.html".num = dog)
 ```
 - ```target="_new"``` 會讓 ```response``` 回來的內容呈現(渲染，render) 在名為 ```"_new"``` 的窗格 ,若 ```_new``` 不存在就開啟一個新的。
 ```html
 <a href="/dynamic" target="_new">中獎了</a> <p>
 ```
### API 服務
 - ```Application Progamming Interface (API)``` 是 ```WebService``` 提供服務的窗口・呼叫 ```API Service``` 通常回傳的是 ```JSON``` 格式的資料。我們會在自己的 Application 寫代碼 (Programming) 呼叫第三方的 API 服務・但需要遵照它的規範(Interface)。
 - 目前最常使用的第三方 API 服務是 LLM API。
 - 我們可以讓自己的網站提供 API 服務・例如只要給 ```/api/weather``` 我們網站就回傳高雄的溫度 (temperatture) 與天氣狀況
(condition)。
```python
@app.route("/api/weather")
def weather():
    return jsonify({"city": "Kaoshiung", "temperature": 30, "condition": "Sunny"})

```
### HTTP 協定有2個角色：http server 與 http Client
 - Browser 只是 http Client 的一種。
 - curl.exe 也是一種 http Client ，它是 CLI(CommandLne Interface)，命令列的操作介面。
 - PowerShell CLI 與 cmd CLI，前者是 Developer 在用，cmd是給一般 user。


### LLM API Service 以 Google Gemini API 為例
 - 1. 到 AI Studio 取得 API Key
 - 2. 
   - 1. ```Linux shellscript```
   ```sh
   curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
    -H 'Content-Type: application/json' \
    -H 'X-goog-api-key: ' \
    -X POST \
    -d '{
      "contents": [
        {
             "parts": [
            {
              "text": "請描述 Taiwan 這個國家的特色"
            }
          ]
        }
      ]
    }'
   ``` 
   - 2. ```Windows PowerShell```
     - 1. 中文 Prompt
     ```powershell
     curl.exe "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" `
     -H 'Content-Type: application/json' `
     -H 'X-goog-api-key: ' `
     -X POST `
     -d '{
       \"contents\": [
         {
              \"parts\": [
             {
               \"text\": \"請描述 Taiwan 這個國家的特色\"
             }
           ]
         }
       ]
     }'
     ```
     - 2. 英文 Prompt
     ```powershell
     curl.exe "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" `
     -H 'Content-Type: application/json' `
     -H 'X-goog-api-key: ' `
     -X POST `
     -d '{
       \"contents\": [
         {
              \"parts\": [
             {
               \"text\": \"Please describe Taiwan.\"
             }
           ]
         }
       ]
     }'
     ```
### 將 Powershell顯示符號時・採用 UTF8去解讀,CLI下
```powershell
# [Console]:: $OutputEncoding = [System.Iext.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8
```

### LLM 強大，但是會有 hallicination (幻文・幻覺)，對企業來說 LLM 要落地應用，就必須要能回答企業的相關問題。
- Prompt 時，給內容，並限定它只能從給的內容找答案，如果找不到就說不知道。
- ```Prompt = <user_prompt> + <context> + <specifier>```
- ```<contet>``` 若來自企業特定知識庫，那麼就不會亂回答了。

### RAG (Retrieval Augmented Generation)
 - 生成文本前 (Generation)，參考附加的內容 (Augmented)，附加的內容來自檢索的結果 (Retrieval)。

```sh
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
 -H 'Content-Type: application/json' \
 -H 'X-goog-api-key: ' \
 -X POST \
 -d '{
   "contents": [
     {
          "parts": [
         {
           "text": "<user_prompt>如何美白?</user_prompt>
<context>生成文本前(Generation)，參考附加的內容(Augmented)，附加的內容來自檢索的結果(Retrieval)。檢索的資料來源可以是網站、資料庫、檔案、會其它資訊系統。</context>
<specifier>根據context回答user_prompt，如果找不到答案就說不知道，不要自己衍伸。</specifier>
"
         }
       ]
     }
   ]
 }'
```

### 
## （13:00 ~ 17:00）檢索增強生成應用系統開發（徐偉智）
### 
### 
### 
