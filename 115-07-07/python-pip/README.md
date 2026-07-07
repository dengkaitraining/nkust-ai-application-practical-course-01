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

 - ```error: externally-managed-environment``` 或者「外部管理的環境」的錯誤見於新版的 ```Ubuntu 24.04``` 、 ```Debian 12``` 、 ```Arch Linux``` 、Fedora、openSUSE、Raspberry Pi OS 12等系統，macOS的Homebrew用戶可能也會遇到。