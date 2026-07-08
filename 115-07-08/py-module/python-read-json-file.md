在 Python 中，讀取 JSON 檔案最標準且推薦的方法是使用內建的 json 模組，並搭配 json.load() 函式。 [1, 2] 
## 🚀 快速程式碼範例
請使用 with open() 語法來開啟檔案，這能確保檔案在讀取完畢後會自動關閉，避免佔用記憶體。 [1, 3, 4] 
```python
import json
# 開啟並讀取 JSON 檔案with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# 讀取後的資料會自動轉換為 Python 的字典 (dict) 或列表 (list)
print(data)
print(type(data))
```
------------------------------
## 💡 核心要點與進階技巧

* 
* json.load() vs json.loads()：
* json.load()：用來讀取 JSON 檔案（如上例，傳入的是檔案物件）。
   * json.loads()：用來解析 JSON 字串（底部的 s 代表 string）。 [1, 5, 6] 
* 指定編碼 (encoding='utf-8')：如果你的 JSON 檔案中包含中文、日文等非英文語系，請務必在 open() 中加上 encoding='utf-8'，以防止出現亂碼或 UnicodeDecodeError。 [7, 8, 9] 
* 安全性與異常處理：實務上建議加入 try-except 機制，預防檔案不存在或 JSON 格式損壞： [2, 10, 11, 12, 13] 
* 
```python
import json
try:
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except FileNotFoundError:
    print("錯誤：找不到指定的 JSON 檔案。")
except json.JSONDecodeError:
    print("錯誤：JSON 檔案格式不正確，無法解析。")
```
如果你後續需要處理這份 JSON 資料，可以告訴我你想提取特定欄位還是將資料轉存為 Excel/CSV，我能為你提供對應的程式碼！ [6, 14, 15, 16] 

[1] [https://stackoverflow.com](https://stackoverflow.com/questions/20199126/reading-json-from-a-file)
[2] [https://leapcell.io](https://leapcell.io/blog/how-to-read-json-in-python)
[3] [https://oneuptime.com](https://oneuptime.com/blog/post/2026-01-25-read-write-json-files-python/view)
[4] [https://medium.com](https://medium.com/@AlexanderObregon/how-to-work-with-json-in-python-aef62d28eac4)
[5] [https://python.plainenglish.io](https://python.plainenglish.io/how-to-read-json-files-in-python-aec189287cfe)
[6] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/)
[7] [https://reqbin.com](https://reqbin.com/req/python/abghm4zf/json-content-type)
[8] [https://believemy.com](https://believemy.com/en/glossaries/python/json)
[9] [https://python.plainenglish.io](https://python.plainenglish.io/how-to-read-json-file-in-python-with-examples-in-2026-9877d0cdca71)
[10] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/python/read-json-file-using-python/)
[11] [https://www.upgrad.com](https://www.upgrad.com/tutorials/software-engineering/python-tutorial/json-python/)
[12] [https://www.upgrad.com](https://www.upgrad.com/blog/how-to-open-json-file/)
[13] [https://johnche88.medium.com](https://johnche88.medium.com/comparing-serde-modules-in-python-1455e6713d4d)
[14] [https://steam.oxxostudio.tw](https://steam.oxxostudio.tw/category/python/library/json.html)
[15] [https://codesignal.com](https://codesignal.com/learn/courses/hierarchical-and-structured-data-formats/lessons/parsing-json-files-in-python)
[16] [https://www.reddit.com](https://www.reddit.com/r/learnprogramming/comments/6zxb9h/what_happens_when_a_file_is_read_by_python/)
