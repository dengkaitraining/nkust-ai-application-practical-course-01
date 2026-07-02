# 封面

## Antigravity 2.0 與 Antigravity IDE 架構差異及使用模式之比較研究：從 AI 輔助開發到 Agent-First 開發平台之轉型分析

作者：XXX
系所：XXX研究所
課程：XXX
日期：2026年7月2日

---

# 摘要

近年來生成式人工智慧（Generative Artificial Intelligence）與大型語言模型（Large Language Models, LLMs）快速進入軟體開發流程，從傳統程式碼補全工具逐漸演進至具備自主執行能力之 Agent 型開發系統。Google 推出的 Antigravity 系列產品代表此趨勢的重要案例。然而在產品演化過程中，Antigravity IDE 與 Antigravity 2.0 出現定位與架構上的重大差異，也引起開發社群對於功能理解與版本命名之混亂。

本研究採用比較分析法（Comparative Analysis Method），針對產品定位、核心介面、操作邏輯、目標使用者、程式碼修改模式、運作模式、使用者體驗以及社群評價等面向進行比較研究。研究結果顯示，Antigravity IDE 強調「人在編輯器中心（Human-centered IDE）」之工作模式；Antigravity 2.0 則傾向「AI Agent 中心（Agent-first）」的工作架構。此差異反映 AI 開發工具已逐步由程式編輯工具轉向工作流程管理平台。

關鍵字：Generative AI、AI Agent、Antigravity IDE、Antigravity 2.0、Agentic Development

---

# 第一章 緒論

## 1.1 研究背景

傳統 IDE（Integrated Development Environment）主要支援程式碼編輯、除錯與編譯。然而大型語言模型技術成熟後，程式設計輔助開始由自動補全逐步轉變成自主決策模式。

Antigravity 系列產品被設計成 Agent-first 開發架構，其核心目標不再只是提供程式碼建議，而是將完整任務委派給 AI 代理完成。此發展方向改變了程式開發者角色，由程式撰寫者逐步轉變為工作流程監督者。

## 1.2 研究目的

本研究目的如下：

(一) 分析 Antigravity IDE 與 Antigravity 2.0 之架構差異。

(二) 比較兩者之使用模式。

(三) 探討使用者對於新型 Agent 開發模式之接受程度。

---

# 第二章 文獻探討

## 2.1 AI 輔助程式開發工具演進

早期 AI 編程工具主要提供：

1. 自動補全
2. 錯誤提示
3. 文件生成

然而近年研究指出，新世代 AI 系統逐漸向自主代理模式發展。開發者由程式輸入者逐步變成決策者。

研究指出：

「未來 IDE 不應只處理靜態程式碼，而應管理 AI 產生程式碼之演化流程。」

## 2.2 Agent 型開發環境

Agent 開發環境具備：

(1) 自主執行
(2) 多代理協作
(3) 工作流程管理
(4) 結果驗證能力

Antigravity 即採用此架構。

---

# 第三章 研究方法

本研究採比較分析法（Comparative Analysis）進行。

比較構面如下：

1. 定位
2. 核心介面
3. 操作邏輯
4. 目標用戶
5. 程式碼修改模式
6. 運作模式
7. 使用者體驗
8. 社群評價
9. 版本混亂問題

研究資料來源包括：

(1) 官方文件
(2) 技術新聞
(3) Reddit 社群討論
(4) 學術研究

---

# 第四章 研究結果

## 4.1 功能比較分析

| 比較項目       | Antigravity IDE | Antigravity 2.0 |
| ---------- | --------------: | --------------: |
| 產品定位       |          AI IDE |      Agent 工作平台 |
| 核心介面       |        程式編輯器為中心 |      Agent 管理中心 |
| 操作邏輯       |       人主導 AI 輔助 |       AI 主導 人監督 |
| 目標用戶       |           程式開發者 |        開發團隊、研究者 |
| 程式碼修改      |         直接編輯程式碼 |      Agent 自動修改 |
| 運作模式       |            同步互動 |        同步＋背景非同步 |
| 工作模式       |            單工作區 |     多 Agent 工作區 |
| 瀏覽器整合      |              有限 |            完整整合 |
| CLI支援      |              較少 |            完整支援 |
| Artifact管理 |              有限 |            完整管理 |
| 學習曲線       |               低 |               高 |

### (一) 定位差異

Antigravity IDE 本質仍屬 IDE，強調編輯器功能。使用者可直接檢視程式碼、修改內容及使用 AI 建議。

Antigravity 2.0 已轉變成獨立 Agent 平台。其目的不是提供程式編輯，而是管理 AI 執行流程。

### (二) 核心介面差異

IDE：

* 編輯器
* 檔案樹
* Terminal
* AI側欄

Antigravity 2.0：

* Agent Dashboard
* Artifact Panel
* Workflow Manager
* Browser Agent

官方稱其為 Agent Command Center。

### (三) 操作邏輯差異

IDE：

使用者 → 指令 → AI → 程式碼

Antigravity 2.0：

使用者 → 任務 → Agent → 子代理 → 執行結果

Antigravity 2.0 引入多代理協作模式。

### (四) 程式碼修改模式

IDE：

使用者可直接控制修改內容。

Antigravity 2.0：

Agent 可：

* 建立程式碼
* 執行測試
* 修改檔案
* 執行 Terminal 指令

因此可能出現自動行為風險。

### (五) 使用者體驗差異

初學者：

Antigravity IDE 較容易理解。

專業團隊：

Antigravity 2.0 在大型專案與多任務處理具明顯優勢。

---

## 4.2 社群評價與版本混亂問題

社群出現大量爭議主要原因如下：

### (1) 版本命名誤解

許多使用者誤認：

Antigravity IDE → Antigravity 2.0

屬於一般版本更新。

實際上：

Antigravity IDE ≠ Antigravity 2.0

而是產品架構重新定義。

### (2) 使用者工作流程被改變

Reddit 討論指出：

部分使用者認為 2.0 將原有 IDE 工作流程移除，導致傳統開發習慣遭到破壞。

### (3) 安全性疑慮

自主 Agent 雖提高效率，但也可能產生：

1. Prompt Injection
2. 自動命令誤執行
3. 資料洩漏風險

研究與媒體均指出其風險需進一步控制。

---

# 第五章 討論與結論

本研究發現 Antigravity 系列的演化並非單純功能升級，而是軟體開發模式的轉移。

傳統 IDE 模式：

「人控制 AI」

逐步轉向：

「AI 執行，人監督」

此變化具有以下意義：

第一，開發者角色將由程式撰寫者轉型成流程管理者。

第二，AI Agent 可提升大型專案效率。

第三，自主能力提高也增加安全風險。

因此未來 Agent 系統發展應加入：

(一) 更高透明度
(二) 更細緻權限控制
(三) 可追蹤驗證機制

若上述問題獲得改善，Agent-first 開發模式可能成為未來主流。

---

# 參考文獻

Google Antigravity Documentation. Antigravity IDE Overview.

Google Antigravity Documentation. Antigravity 2.0 Overview.

Perez, S. (2026). Google launches Antigravity 2.0 with an updated desktop app and CLI tool at IO 2026.

The Verge. Google Antigravity is an agent-first coding tool built for Gemini 3.

TechRadar. Google's AI-powered Antigravity IDE already has some worrying security issues.

Kula, R., Treude, C. (2025). The Shift from Writing to Pruning Software: A Bonsai-Inspired IDE for Reshaping AI Generated Code.

Nghiem, K., Nguyen, A., Bui, N.D.Q. (2024). Envisioning the Next-Generation AI Coding Assistants: Insights & Proposals.

Reddit Community Discussions on Antigravity Ecosystem.
