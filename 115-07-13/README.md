## （08:00 ~ 10:00）資訊與通訊技術（徐偉智）
### 
### 
### 

### Communication,通訊
 - 5G,5th Generation,第五代行動通訊
 - Internet 網際網路協定
### 5G
1. 頻寬大,但對手機來說,跟4G差不多,因為最吃頻寬的大戶就是Video,而手機Monitor不大,不需要高解析度,自然就不需要5G。
2. 低延遲(同一個基地台涵蓋範圍內)
(1)實況轉播
(2)遠端手術
(3)智能工廠遠端控制
(4)無線VR
 - 5G的系統架構就跟 WiFi 一樣,有基地台,但範圍涵蓋比較廣;WiFi 500公尺,5G約20公里。
 - 5G專網,專門為某一群體,可以小到一家公司,例如台積電,也可以是為一個園區提供服務,不對一般大眾開放。
### 5G 實際上包含多種通訊技術,統稱而已,例如 NB-IoT、毫米波。
 - NB-IoT 主要用在連結低頻寬需求的IoT(Internet of Things)裝置,通常是大範圍的,例如監測土石流,智能電表。
 - 毫米波 用在光達(liDar),建立3D場景;在醫療照護上,毫米波可以用來感測病人的生理狀況,例如脈搏。
### Internet 的網路層(Internet Layer)是整個 Internet運作的核心,將全世界的子網路 (subnet)以Router連起來就構成Internet。
 - C:\Users\user>ipconfig
IPv4 位址 . . . . . . . . . . . . : ```192.168.104.10```
子網路遮罩 . . . . . . . . . . . .: ```255.255.255.0```
; subnet mask
預設閘道 . . . . . . . . . . . . .: ```192.168.104.1```
### 子網路都有一個唯一的subnet ID (子網路ID)
 - ```Subnet_ID``` = ```IP_Address``` AND ```subnet_Mask```
 - ```192.168.104.10``` AND ```255.255.255.0``` = ```192.168.104.0```
 - ```IP Address``` 是 ```32 bits```,分4個欄位,每一個欄位```8bits```,轉成10進位,再加 . 就變成 ```192.168.104.1``` 這種樣子。
### 預設閘道(Default Gateway)就是子網路接的那個Router的接口(Interface),也是子網路一部分。
 - 子網路的封包 (packet)要往外,都由 Default Gateway轉出。
 - Router 會把給子網路某一個IP的封包,也透過預設閘道轉入。
### Router 會彼此學習到各自接的子網路ID,然後互通訊息,最後就可以直接或間接認識整個Internet。
 - 一個封包最少有3個欄位:(1)目的端IP (2)傳送端IP (3)DATA 。
 - Router 檢視目的端IP 可以查出該封包去處,會進行轉送(routing),轉送再轉送,最終就會到達目的端IP_Address所在的電腦。
### IP Address 的格式就是32 bits,為什麼有真IP與 假IP?
 - IP 就是IP,沒有真假,實際上是公開IP(Public IP Address)與私用IP (Private IPAddress),前者可以被Internet上的電腦直接找到,後者沒有辦法被Internet上的電腦直接找到。
 - NAT (Network Address Translation)設備之內的電腦所用的 IP 就是Private IPAddress。通常會是 192.X.X.X 的樣子。
 - NAT 之內的網路就被稱為內部網路。-> 192.168.104.10 可以設定給許多不同內部網路的電腦而不互相衝突。
### 還有一種IP Address,做為測試用 (local
loop test),只有在local 電腦本身可以連,子網路的其他電腦都連不到。
 - 在開發時,可以避免干擾。
 - 127.0.0.1 就是
### Python Flask Web Application如何開放外部可以連進來?
```pyhton
app.run(debug=True) 改
app.run(host="0.0.0.0",debug=True)
```
 - http://192.168.104.10:5000/
 - 因為是Private IP,所以只有同一個子網路才能互連。
 - ngrok 代理(proxy),可以讓Internet上所有電腦連到Private IP的 Server。
 - 5000叫 port number。為什麼要有Port Number? 每一部電腦只有一個IP Address,
但有許多網路應用程式都會用到IP Address,也就是共享,為了不錯亂,所以每一個網路應用程式就多編一個Port Number,以示區別。就像一棟大樓有許多房間,大樓地址一樣,但房間號碼都不一樣,信件就不會寄錯。
### 練習: Set Up RAG002.zip executable。


## （10:00 ~ 12:00）AI 代理人進階應用（曾士桓）
### 
### 
### 
## （13:00 ~ 17:00）AI 代理人進階應用（曾士桓）
### 
### 
###