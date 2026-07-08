在 Python 中讀取 .env 檔案，最標準且常用的做法是使用 python-dotenv 套件。它可以將 .env 檔案中的設定值載入到系統環境變數中，再透過內建的 os 模組讀取。 [1] 
以下是完整的操作步驟：
## 1. 安裝套件
請先在終端機（Terminal）執行以下指令安裝套件： [1, 2] 
```python
pip install python-dotenv
```
## 2. 建立 .env 檔案
在專案的根目錄下建立一個名為 .env 的檔案，並寫入鍵值對（注意：等號兩邊不要留空格）： [1, 3, 4, 5] 
```ini
DATABASE_URL=postgres://user:password@localhost/dbname
API_KEY=your_secret_api_key_here
DEBUG=True
```
## 3. 在 Python 中讀取
在你的 Python 腳本中，使用 load_dotenv() 載入檔案，並透過 os.getenv() 讀取數值： [1, 6, 7, 8, 9] 
```python
import osfrom dotenv import load_dotenv
# 載入同目錄下的 .env 檔案
load_dotenv()
# 讀取特定環境變數db_url = os.getenv("DATABASE_URL")api_key = os.getenv("API_KEY")# 也可以設定當變數不存在時的預設值debug_mode = os.getenv("DEBUG", "False") 

print(f"Database URL: {db_url}")
print(f"API Key: {api_key}")
print(f"Debug Mode: {debug_mode}")
```
## 💡 進階小技巧

* 
* 指定特定路徑：如果你的 .env 檔案不在根目錄，可以手動指定路徑：
```python
from pathlib import Pathenv_path = Path('.') / 'config' / '.env'
load_dotenv(dotenv_path=env_path)
````
* 安全性提醒：.env 檔案通常包含敏感金鑰，千萬不要把它推上 GitHub。請務必在 .gitignore 檔案中加入 .env。 [3, 4, 10, 11, 12] 
* 

如果你需要更進階的變數型態檢查（例如自動把 "True" 轉成布林值 True），我可以為您介紹如何結合 Pydantic 來管理設定。需要為您示範嗎？ [4, 5, 11, 13] 

[1] [https://dev.to](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1)
[2] [https://dev.to](https://dev.to/sleibrock/environment-variables-with-python-3be4)
[3] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/)
[4] [https://dagster.io](https://dagster.io/blog/python-environment-variables)
[5] [https://medium.com](https://medium.com/art-of-data-engineering/learn-with-me-using-env-file-in-python-a82fa4365e4e)
[6] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/read-environment-variables-with-python-dotenv/)
[7] [https://medium.com](https://medium.com/@c17hawke/unlock-secrets-to-managing-your-credentials-with-python-dotenv-quickstart-guide-5e0e34cd5c9a)
[8] [https://corinfaife.co](https://corinfaife.co/Bytes/store-secrets-dotenv)
[9] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/how-to-create-and-use-env-files-in-python/)
[10] [https://pypi.org](https://pypi.org/project/python-dotenv/)
[11] [https://medium.com](https://medium.com/the-pythonworld/do-you-know-python-can-read-environment-variables-without-extra-packages-1a96f9045d8f)
[12] [https://gist.github.com](https://gist.github.com/plembo/2289ef51b6c00f00b547e78a43fafcb6)
[13] [https://www.youtube.com](https://www.youtube.com/watch?v=A1OA0Y9vwJY)
