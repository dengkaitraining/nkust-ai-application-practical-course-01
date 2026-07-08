import subprocess
import os
from dotenv import load_dotenv

# 載入同目錄下的 .env 檔案
load_dotenv()

# 讀取特定環境變數
kyle_api_key = os.getenv("kyle_api_key", "default_value_if_not_set")
training_api_key = os.getenv("training_api_key", "default_value_if_not_set")

# 也可以設定當變數不存在時的預設值
debug_mode = os.getenv("DEBUG", "False") 


print(f"kyle_api_key : {kyle_api_key}")
print(f"training_api_key : {training_api_key}")
print(f"Debug Mode: {debug_mode}")

transfer_data = """{
   "contents": [
     {
          "parts": [
         {
           "text": "<user_prompt>如何美白?</user_prompt><context>生成文本前(Generation)，參考附加的內容(Augmented)，附加的內容來自檢索的結果(Retrieval)。檢索的資料來源可以是網站、資料庫、檔案、會其它資訊系統。</context><specifier>根據context回答user_prompt，如果找不到答案就說不知道，不要自己衍伸。</specifier>"
         }
       ]
     }
   ]
 }"""


def run_curl_command():
    command = [
        "curl",
        "-X",
        "POST",
        "-H",
        "Content-Type: application/json",
        "-H",
        f"X-goog-api-key: {kyle_api_key}",
        "-d",
        transfer_data,
        "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"
    ]
    #result = command
    #return result
    result = subprocess.run(command, capture_output = True, text = True)
    return result.stdout

print(run_curl_command())