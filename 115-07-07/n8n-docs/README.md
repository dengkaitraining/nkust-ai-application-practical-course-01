### 1. 至 n8n 官網註冊 14 天免費帳號。[https://n8n.io/](https://n8n.io/)
### Prompt
```prompt
請協助產生以下網頁資訊：
114學年度期末考成績
姓名：{{ $json['姓名'] }}
國文：{{ $json['國文'] }}
英文：{{ $json['英文'] }}
```
### 回覆
好的，以下是為您整理好的網頁資訊格式。這裡提供兩種常見的呈現方式：**區塊樣式**（適合手機或卡片式排版）以及**表格樣式**（適合傳統成績單排版）。您可以直接複製使用：

### 1. 卡片式排版（適合 RWD 行動裝置）

```html
<div style="font-family: Arial, sans-serif; max-width: 400px; margin: 20px auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
  <h2 style="text-align: center; color: #333; margin-top: 0; border-bottom: 2px solid #4CAF50; padding-bottom: 10px;">114學年度期末考成績</h2>
  <div style="margin-top: 15px; font-size: 16px; line-height: 2;">
    <p style="margin: 5px 0;"><strong>姓名：</strong><span style="color: #555;">{{ $json['姓名'] }}</span></p>
    <p style="margin: 5px 0;"><strong>國文：</strong><span style="color: #4CAF50; font-weight: bold;">{{ $json['國文'] }}</span> 分</p>
    <p style="margin: 5px 0;"><strong>英文：</strong><span style="color: #2196F3; font-weight: bold;">{{ $json['英文'] }}</span> 分</p>
  </div>
</div>

```

---

### 2. 表格化排版（適合後台或報表呈現）

```html
<div style="font-family: Arial, sans-serif; max-width: 500px; margin: 20px auto;">
  <table style="width: 100%; border-collapse: collapse; text-align: left; box-shadow: 0 2px 3px rgba(0,0,0,0.1);">
    <thead>
      <tr style="background-color: #4CAF50; color: white;">
        <th colspan="2" style="padding: 12px; text-align: center; font-size: 18px;">114學年度期末考成績單</th>
      </tr>
    </thead>
    <tbody>
      <tr style="background-color: #f9f9f9;">
        <td style="padding: 12px; border: 1px solid #ddd; font-weight: bold; width: 30%;">學生姓名</td>
        <td style="padding: 12px; border: 1px solid #ddd;">{{ $json['姓名'] }}</td>
      </tr>
      <tr>
        <td style="padding: 12px; border: 1px solid #ddd; font-weight: bold;">國文成績</td>
        <td style="padding: 12px; border: 1px solid #ddd;">{{ $json['國文'] }} 分</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="padding: 12px; border: 1px solid #ddd; font-weight: bold;">英文成績</td>
        <td style="padding: 12px; border: 1px solid #ddd;">{{ $json['英文'] }} 分</td>
      </tr>
    </tbody>
  </table>
</div>

```

**提示：** 這裡保留了您的 n8n / 變數語法 `{{ $json['欄位名稱'] }}`，您可以直接將這段 HTML 貼進您的網頁原始碼或自動化寄信工具（如 Gmail/SMTP 節點的 HTML 欄位）中，系統會自動帶入對應的資料。

### Prompt
```
請協助產生以下網頁資訊，並以html格式呈現：
恭喜獲得五星好評獎品 Switch 2 一台
姓名：{{ $json['姓名'] }}
評分：{{ $json['5星評分'] }}
評語：{{ $json['評語'] }}
```

### 回覆

```python
import base64

html_content = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>恭喜獲得五星好評獎品！</title>
    <style>
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft JhengHei", sans-serif;
            background-color: #f4f7f6;
            color: #333333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #ffffff;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
            max-width: 600px;
            width: 90%;
            padding: 40px;
            margin: 20px auto;
            text-align: center;
            border-top: 8px solid #e60012; /* Nintendo Switch Red theme */
        }
        .congrats-title {
            color: #e60012;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .prize-banner {
            background-color: #fff0f1;
            border: 1px dashed #e60012;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        .prize-name {
            font-size: 24px;
            color: #e60012;
            font-weight: bold;
            display: block;
            margin-top: 5px;
        }
        .info-section {
            text-align: left;
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 25px;
        }
        .info-title {
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 0;
            margin-bottom: 15px;
            border-left: 4px solid #e60012;
            padding-left: 10px;
        }
        .info-item {
            margin-bottom: 12px;
            font-size: 16px;
            line-height: 1.6;
        }
        .info-label {
            font-weight: bold;
            color: #666666;
            display: inline-block;
            width: 90px;
        }
        .comment-box {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 12px 15px;
            margin-top: 8px;
            font-style: italic;
            color: #4a5568;
            position: relative;
        }
        .notice-section {
            text-align: left;
            font-size: 14px;
            color: #666666;
            line-height: 1.6;
            border-top: 1px solid #eaeaea;
            padding-top: 20px;
        }
        .notice-title {
            font-weight: bold;
            color: #333333;
            margin-bottom: 8px;
        }
        .notice-list {
            padding-left: 20px;
            margin: 0;
        }
        .notice-list li {
            margin-bottom: 5px;
        }
        .footer {
            margin-top: 30px;
            font-size: 13px;
            color: #999999;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="congrats-title">🎉 恭喜您得獎了！ 🎉</div>
    <p style="font-size: 16px; color: #555555; line-height: 1.5;">
        親愛的會員您好，感謝您的熱烈支持與好評分享！<br>恭喜您獲得本次五星好評抽獎活動的特獎：
    </p>

    <div class="prize-banner">
        <span style="font-size: 16px; color: #555555;">活動大獎</span>
        <span class="prize-name">Nintendo Switch 2 一台</span>
    </div>

    <div class="info-section">
        <div class="info-title">您的評價與中獎資訊</div>
        <div class="info-item">
            <span class="info-label">真實姓名：</span>
            <span>{{ $json['姓名'] }}</span>
        </div>
        <div class="info-item">
            <span class="info-label">評分星級：</span>
            <span style="color: #ffb100; font-weight: bold;">{{ $json['5星評分'] }}</span>
        </div>
        <div class="info-item" style="margin-bottom: 0;">
            <span class="info-label">心得評語：</span>
            <div class="comment-box">
                「 {{ $json['評語'] }} 」
            </div>
        </div>
    </div>

    <div class="notice-section">
        <div class="notice-title">🎁 領獎須知：</div>
        <ul class="notice-list">
            <li>系統已發送中獎確認信至您的會員信箱，請於 <strong>7 個工作天內</strong> 回填收件資料。</li>
            <li>獎品將於收件資料確認無誤後，依序安排寄出（寄送範圍僅限台澎金馬地區）。</li>
            <li>若有任何領獎問題，歡迎隨時聯繫線上客服。</li>
        </ul>
    </div>

    <div class="footer">
        祝您遊戲愉快！再次感謝您的優質好評。
    </div>
</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file generated successfully.")



```

```text
HTML file generated successfully.


```

您的網頁資訊 HTML 檔案已成功產生。

為方便您直接複製或嵌入系統，以下提供完整的 HTML 與 CSS 原始碼。此版本特別加入了適合 **Switch 主題** 的紅白時尚配色，並具備自適應（RWD）設計與優雅的區塊視覺排版：

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>恭喜獲得五星好評獎品！</title>
    <style>
        *, *::before, *::after {
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Microsoft JhengHei", sans-serif;
            background-color: #f4f7f6;
            color: #333333;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: #ffffff;
            border-radius: 16px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
            max-width: 600px;
            width: 90%;
            padding: 40px;
            margin: 20px auto;
            text-align: center;
            border-top: 8px solid #e60012; /* Nintendo Switch 主題紅 */
        }
        .congrats-title {
            color: #e60012;
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .prize-banner {
            background-color: #fff0f1;
            border: 1px dashed #e60012;
            border-radius: 8px;
            padding: 20px;
            margin: 25px 0;
        }
        .prize-name {
            font-size: 24px;
            color: #e60012;
            font-weight: bold;
            display: block;
            margin-top: 5px;
        }
        .info-section {
            text-align: left;
            background-color: #f8f9fa;
            border-radius: 8px;
            padding: 25px;
            margin-bottom: 25px;
        }
        .info-title {
            font-size: 18px;
            font-weight: bold;
            color: #2c3e50;
            margin-top: 0;
            margin-bottom: 15px;
            border-left: 4px solid #e60012;
            padding-left: 10px;
        }
        .info-item {
            margin-bottom: 12px;
            font-size: 16px;
            line-height: 1.6;
        }
        .info-label {
            font-weight: bold;
            color: #666666;
            display: inline-block;
            width: 90px;
        }
        .comment-box {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 12px 15px;
            margin-top: 8px;
            font-style: italic;
            color: #4a5568;
            position: relative;
        }
        .notice-section {
            text-align: left;
            font-size: 14px;
            color: #666666;
            line-height: 1.6;
            border-top: 1px solid #eaeaea;
            padding-top: 20px;
        }
        .notice-title {
            font-weight: bold;
            color: #333333;
            margin-bottom: 8px;
        }
        .notice-list {
            padding-left: 20px;
            margin: 0;
        }
        .notice-list li {
            margin-bottom: 5px;
        }
        .footer {
            margin-top: 30px;
            font-size: 13px;
            color: #999999;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="congrats-title">🎉 恭喜您得獎了！ 🎉</div>
    <p style="font-size: 16px; color: #555555; line-height: 1.5;">
        親愛的會員您好，感謝您的熱烈支持與好評分享！<br>恭喜您獲得本次五星好評抽獎活動的特獎：
    </p>

    <div class="prize-banner">
        <span style="font-size: 16px; color: #555555;">活動大獎</span>
        <span class="prize-name">Nintendo Switch 2 一台</span>
    </div>

    <div class="info-section">
        <div class="info-title">您的評價與中獎資訊</div>
        <div class="info-item">
            <span class="info-label">真實姓名：</span>
            <span>{{ $json['姓名'] }}</span>
        </div>
        <div class="info-item">
            <span class="info-label">評分星級：</span>
            <span style="color: #ffb100; font-weight: bold;">{{ $json['5星評分'] }}</span>
        </div>
        <div class="info-item" style="margin-bottom: 0;">
            <span class="info-label">心得評語：</span>
            <div class="comment-box">
                「 {{ $json['評語'] }} 」
            </div>
        </div>
    </div>

    <div class="notice-section">
        <div class="notice-title">🎁 領獎須知：</div>
        <ul class="notice-list">
            <li>系統已發送中獎確認信至您的會員信箱，請於 <strong>7 個工作天內</strong> 回填收件資料。</li>
            <li>獎品將於收件資料確認無誤後，依序安排寄出（寄送範圍僅限台澎金馬地區）。</li>
            <li>若有任何領獎問題，歡迎隨時聯繫線上客服。</li>
        </ul>
    </div>

    <div class="footer">
        祝您遊戲愉快！再次感謝您的優質好評。
    </div>
</div>

</body>
</html>

```

### 💡 設計特點：

* **自適應（RWD）設計**：不論在手機版、平板、桌機版，網頁皆能完美置中並調整寬度。
* **參數保留**：原有的自動變數欄位 `{{ $json['...'] }}` 已幫您保留，可以直接放進自動化流程（例如 n8n、Make 等自動發信或網頁渲染系統）中使用。