在 Python 中，將「字串」轉換為 JSON 物件（在 Python 中對應為字典 dict 或列表 list），主要使用內建 json 模組的 json.loads() 函式。 [1, 2] 
以下為您整理兩種最常見的轉換情境與程式碼範例：
## 1. 將 JSON 格式的字串轉為 Python 字典/列表
如果你的字串本身就是符合標準 JSON 規範的文字，直接使用 json.loads() 即可： [2, 3, 4] 
```python
import json
# 這是符合 JSON 規範的字串（注意：JSON 規定必須使用雙引號 ""）
json_string = '{"name": "John", "age": 30, "city": "Taipei"}'
# 使用 json.loads() 進行轉換
data = json.loads(json_string)
# 輸出結果
print(type(data))  # <class 'dict'>
print(data)        # {'name': 'John', 'age': 30, 'city': 'Taipei'}
print(data["name"]) # John
```
------------------------------
## 2. 將 Python 的物件（如字典）轉回 JSON 字串
如果你原本手裡是 Python 的字典或列表，想要把它打包成 JSON 格式的字串（例如準備用來傳遞 API），請使用 json.dumps()： [1, 5] 
```python
import json
# 這是一個 Python 字典
my_dict = {"name": "Mary", "age": 25, "is_student": True}
# 使用 json.dumps() 轉為 JSON 字串# ensure_ascii=False 可以讓中文不被強制編碼，indent=4 可以讓排版變漂亮
json_str = json.dumps(my_dict, ensure_ascii=False, indent=4)

print(type(json_str))  # <class 'str'>
print(json_str)
```
------------------------------
## ⚠️ 常見錯誤與注意事項

* 
* 引號問題：JSON 官方標準強制規定鍵（Key）與字串型別的值（Value）必須使用雙引號 "。如果你的字串包裹著單引號（例如 '{'name': 'John'}'），json.loads() 會直接拋出 json.decoder.JSONDecodeError 錯誤。
* 檔案操作：如果要直接從「JSON 檔案」讀取，請改用 json.load(f)（少一個 s，代表 load file）；若要寫入檔案，則用 json.dump(data, f)。 [5, 6, 7, 8] 
* 

若您在轉換過程中遇到了特定的錯誤訊息，或您的原始字串格式比較特殊（例如帶有單引號或特殊編碼），可以提供字串樣本與報錯內容，我能為您提供更精準的解決方案！

[1] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/articles/10220160)
[2] [https://www.w3schools.com](https://www.w3schools.com/python/python_json.asp)
[3] [https://www.freecodecamp.org](https://www.freecodecamp.org/news/python-json-how-to-convert-a-string-to-json/)
[4] [https://reqbin.com](https://reqbin.com/code/python/0l6wsqxp/python-pretty-print-json-example)
[5] [https://blog.csdn.net](https://blog.csdn.net/qdPython/article/details/128099724)
[6] [https://stackoverflow.com](https://stackoverflow.com/questions/34600003/converting-json-to-string-in-python)
[7] [https://iproyal.com](https://iproyal.com/blog/python-string-to-json/)
[8] [https://codesignal.com](https://codesignal.com/learn/courses/hierarchical-and-structured-data-formats/lessons/constructing-objects-and-writing-to-json-files)
