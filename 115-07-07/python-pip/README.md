### 解決 Ubuntu 系統 pip install的externally-managed-environment 錯誤
在 Python 3.12 版本以上的Linux系統，執行 ```pip install`` 指令，可能會遇到以下錯誤：
```sh
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.14/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
```

 - ```error: externally-managed-environment``` 或者「外部管理的環境」的錯誤見於新版的 ```Ubuntu 24.04``` 、 ```Debian 12``` 、 ```Arch Linux``` 、 ```Fedora``` 、 ```openSUSE``` 、 ```Raspberry Pi OS 12``` 等系統，```macOS``` 的 ```Homebrew``` 用戶可能也會遇到。

 #### 1. 暫時的解決方法：允許pip變更系統
 允許pip在系統安裝套件，該方法可能造成 ```Python``` 破壞 ```Linux``` 系統的 ```dependency```，請小心操作。

  - 1. 確認系統Python版本，撰文當下是3.12
  ```sh
  sudo python3 --version
  ```

  - 2. 將 ```/usr/lib/python``` 版本 ```/EXTERNALLY-MANAGED``` 檔案重新命名，這樣就不會觸發 ```error: externally-managed-environment``` 警告了。
  ```sh
  sudo mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED.old
  ```

  - 3. 另一個作法是加上 ```--break-system-packages``` 引數，強制 ```pip``` 安裝：
  ```sh
  sudo pip install <套件名稱> --break-system-packages
  ```

  - 儘管用 ```pip install <套件名稱> --use``` r指令也可以，不過這是將 Pyhton 套件安裝到使用者目前的家目錄，只有目前使用者執行的Python程式能夠import模組。假若Python程式需要使用sudo執行，則又會遇到ModuleNotFoundError: No module named找不到套件的問題。

#### 2. 改用Linux套件管理器安裝Python套件
 - pip 不能變更系統，那就透過 Linux 發行版套件管理員代勞吧。仔細看文章一開頭提到的 ```error: externally-managed-environment``` 訊息，它也建議你使用 ```apt install``` 的方式安裝 Python 套件。
 - 有些受歡迎的Python套件，Linux發行版會將之打包為套件，通常這些套件會以 **python-套件名稱** 開頭。
 - 譬如Cython，Ubuntu有將其打包，可以透過APT套件庫安裝，不需要透過pip：
 ```sh
 sudo apt install cython
 ```
 - 安裝後全系統可用，Python指令稿裡面就能直接 ```import cython``` 模組了。
 - 因為這些套件是Linux發行版管理員維護的，穩定性有保障，能夠確保裝下去不會破壞系統依賴。但Linux發行版收錄的Python套件可能會偏舊，無法任意切換版本。

#### 3. 改用 ```Python``` 虛擬環境安裝 ```pip``` 套件 (建議方式)
 - 使用 [Python 官方文件](https://docs.python.org/3/library/venv.html)提及的虛擬環境 (virtual environment) 功能，也就是安裝 Python 套件前都先用 venv 建立一個虛擬環境，讓 Python 的套件跟 Linux 系統套件隔離，再於裡面使用 pip 安裝想要的套件。如此一來系統就不怕被 pip 弄壞，還可以防止不同專案的 Python 套件互相衝突。
 - Python 虛擬環境跟 pip 直接安裝套件到 Linux 系統有什麼差？請看下圖分解，以使用 cython 為例：如果你用 apt install 安裝 cython，屬於系統全域安裝，不論是哪一個使用者執行 Python 程式，都可以 import cython。但若是在 venv 虛擬環境裡面 pip install，就只有進入虛擬環境裡面才能 import cython。
 ![](../images/python-env.png)
 - 註：此處使用最簡單的Python venv建立虛擬環境，依賴Linux系統所安裝的Python，不能任意切換Python版本。若要切換多重Python版本，請裝其他 Python 環境管理工具，例如 [uv]() 、 [Conda]() 、 [Pipx]() 、 [Poetry]() 等等。
 - 1. 從Linux發行版套件庫安裝Python虛擬環境工具
 ```sh
 sudo apt install python3-venv
 ```
 - 2. 使用 **python3 -m venv** 指令，在家目錄建立一個叫做venv的虛擬環境，實際上就是一個新目錄：
 ```sh
 cd ~ # project path
 sudo python3 -m venv venv
 ```
 - 註解：如果你使用的Python專案來自Github，那麼也可以在git clone之後，於git儲存庫的目錄直接建立venv虛擬環境。
 - 3. 然後用source指令，讀取venv目錄下的activate指令，進入虛擬環境，終端機的提示符前方應該會變成(venv)
 ```sh
 source venv/bin/activate
 ```
 - 4. 查看Python路徑為何，這裡顯示的應該是venv開頭的路徑，也就是虛擬環境裡面的Python，而非Linux系統目錄的/usr/bin/python3
 ```sh
 which python3
 ```
 - 5. 然後就可以用pip install安裝套件了，例如這裡我安裝yt-dlp。所有pip install安裝的套件都會跑到venv這個虛擬環境的目錄下。
 ```sh
pip install yt-dlp
 ```
 - 6. 日後要執行虛擬環境裡面的程式，建議進入虛擬環境裡面操作：
 ```sh
 source venv/bin/activate
 yt-dlp --version
 ```
 - 7. 需要執行.py程式的場合，直接用python3指令就可以了。
 ```sh
 python3 main.py
 ```
 - 8. 或者直接填寫絕對路徑，呼叫虛擬環境裡面的Python執行.py程式，就不需要使用source指令啟動虛擬環境了：
 ```sh
 ./venv/bin/python3 main.py
 ```

 #### 參考資料
  - [解決Ubuntu系統pip install的externally-managed-environment錯誤，改用虛擬環境安裝套件](https://ivonblog.com/posts/linux-solve-externally-managed-environment-error/)