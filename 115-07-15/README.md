## （08:00 ~ 12:00）Python Flask 框架（徐偉智）
### 

### ```Latge Language Model``` 在學習完 ```Knowledge``` 後知識就 ```frozen``` 了。
### ```LLM``` 不等於 ```ChatGPT```，後者有 ```RAG``` 元素
### ```RAG (Retrieval Augmented Generation)```
 - Retrieval的來源是特定知識庫(Specific Knowledge)，Retrieval的根據是user_prompt
 - 從context找出user_prompt的答案，如果找不到就說不知道。
### 實現RAG系統，通常會安裝 Open Source LLM
 - TAIDE，TAIDE LX-13B (學研用版本)模型，基於Llama2  Open Source 再Model Finetune(模型微調)-> 具臺灣特色與繁體中文的可信任生成式AI對話引擎(Trustworthy AI Dialogue Engine, TAIDE)
### RAG的Retrieval可以從
 - (1) ```File```
 - (2) 關聯式資料庫
 - (3) ```Vector Database (向量資料庫)```
 - (4) 其他資訊系統，例如：ERP
 - (5) 第三方API
 - (6) 網路爬蟲

### 假設有一個知識庫是 {關鍵字, 描述}的結構，儲存在純文字檔 knowledge.txt 。描述是以"與"包含起來，儲存內容舉例如下：
```txt
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
```
```prompt
編寫一個Python 函式，給定 User_Prompt，函式會比對 User_Prompt是否有{AI, IoT, Blockchain}等關鍵字，如果有就return，若沒有比對到就return 空list。使用Python re Module，也就是 Regualr Expression Module。關鍵字如果是英文vocabulary的一部分視為未比對到，如果出現在非英文詞後就當做比對到。 
```

```prompt
編寫一個Python 函式，給定關鍵字可以到純文字檔 knowledge.txt找出對應的內容。
純文字檔 knowledge.txt 是 {關鍵字, 描述}的結構，每一行儲存一筆關鍵字資訊，每一個關鍵字包含多個描述內容。描述是以"與"包含起來，儲存內容舉例如下：
AI, "Artificial Intelligent, 主要分鑑別式AI與生成式AI"
IoT,"Internet of Things, 全面感知、數據處理、決策控制"
AI, "資料探勘有時也被稱為AI"
IoT,"各類感測器是蒐集數據的IoT終端裝置"
AI, "基因演算法這一類的最佳解搜尋也被稱為AI"
```

### 
### 
## （13:00 ~ 17:00）Python Flask 框架（徐偉智）
### 
### 
###