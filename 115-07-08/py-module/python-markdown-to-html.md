在 Python 中，將 Markdown 轉換為 HTML 最常見且穩定的做法是使用官方維護的 markdown 函式庫。以下為您整理三种最直接的使用方式： [1, 2, 3] 
## 1. 快速轉換字串
如果只需在程式碼中轉換一小段文字，可以直接調用 markdown.markdown()： [2, 4, 5, 6] 
```python
import markdown
# 定義 Markdown 內容
md_text = """
# 這是主標題
這是一段包含 **粗體** 與 *斜體* 的文字。
- 項目一
- 項目二"""
# 轉換為 HTML 字串html = markdown.markdown(md_text)
print(html)
```
## 2. 轉換 Markdown 檔案
若需要讀取 .md 檔案並輸出成完整的 .html 檔案，請使用以下標準寫法： [2, 7] 
```python
import markdown
# 讀取 Markdown 檔案
with open("input.md", "r", encoding="utf-8") as f:
    md_content = f.read()
# 轉換為 HTML 內容
html_content = markdown.markdown(md_content)
# 寫入 HTML 檔案
with open("output.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("轉換完成！")
```
## 3. 命令列（CLI）直接轉換
如果你不想寫 Python 腳本，該套件安裝後也支援直接在終端機（Terminal）使用命令列轉換檔案： [8, 9] 
```python
# 安裝工具
pip install markdown
# 將 input.md 轉換並輸出至 output.html
python -m markdown input.md > output.html
```
------------------------------
## 💡 進階技巧：啟用表格與程式碼高亮
預設的 Markdown 轉換器不包含「表格」或「GitHub 風格代碼塊」等擴充語法。若需要這些功能，可以啟用內建的 Extensions（擴充功能）： [3, 10, 11] 
```python
import markdown
md_text = """

| 欄位 A | 欄位 B |
| ------ | ------ |
| 資料 1 | 資料 2 |

```python
print("Hello World")
```"""
# 啟用 extra (包含表格、定義列表等) 與 codehilite (代碼高亮) 擴充功能
html = markdown.markdown(md_text, extensions=['extra', 'codehilite'])
print(html)
```
您目前是要處理特定的 Markdown 檔案，還是想將這個轉換功能整合到網頁框架（如 Flask/Django）中呢？ 如果您有特定的需求，我可以為您提供更符合情境的程式碼。

[1] [https://python-markdown.github.io](https://python-markdown.github.io/reference/)
[2] [https://www.runoob.com](https://www.runoob.com/python3/python-markdown2html.html)
[3] [https://github.com](https://github.com/trentm/python-markdown2)
[4] [https://medium.com](https://medium.com/@yadhuh/converting-markdown-documents-into-html-files-using-python-90c8f6e2a22c)
[5] [https://clay-atlas.com](https://clay-atlas.com/blog/2020/12/20/python-cn-package-markdown-module-convert-html/)
[6] [https://jchu.cc](https://jchu.cc/2020/11/21-markdown.html)
[7] [https://www.e-iceblue.com](https://www.e-iceblue.com/Tutorials/Python/Spire.Doc-for-Python/Program-Guide/Conversion/convert-Markdown-to-HTML-in-Python.html)
[8] [https://www.linode.com](https://www.linode.com/docs/guides/how-to-use-python-markdown-to-convert-markdown-to-html/)
[9] [https://dev.to](https://dev.to/stokry/how-to-create-a-simple-markdown-to-html-converter-in-python-14li)
[10] [https://www.easecloud.io](https://www.easecloud.io/tools/web/markdown-to-html/)
[11] [https://www.sitepoint.com](https://www.sitepoint.com/community/t/how-to-i-go-about-displaying-a-mark-down-file-in-a-normal-web-browser/459948)
