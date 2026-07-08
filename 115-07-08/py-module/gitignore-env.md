在 .gitignore 檔案中加入 .env，可以防止機密金鑰、資料庫密碼等敏感資料被上傳到 GitHub 等 Git 版本控制庫中。 [1, 2] 
以下為您整理常用的設定方法與情境解法：
## 1. 標準設定（推薦）
在專案根目錄的 .gitignore 檔案中，直接加入以下內容： [2, 3] 
```sh
# 忽略所有環境變數檔案

.env
.env.local
.env.*.local
dist/env/

# 允許追蹤範例檔（用來提醒團隊有哪些變數需要設定）
!.env.example
```
------------------------------
## 2. 如果 .env 已經被 Git 追蹤了怎麼辦？
如果您在加入 .gitignore 之前就已經執行過 git commit，Git 會持續追蹤該檔案。請依照以下步驟解除追蹤，但保留本地檔案： [2, 4, 5] 

   1. 從快取中刪除檔案（此指令不會刪除您電腦上的實體檔案）：
```sh
git rm --cached .env
```
   2. 提交此變更：
```sh
git commit -m "Removes .env from tracking"
```
   3. 推送到遠端：
```sh
git push
```
   [2, 4] 

⚠️ 安全性警告： 即使執行上述步驟，.env 的歷史內容依然留在過去的 Commit 紀錄中。如果已經推送到公開的 GitHub 庫，請務必立即更換該 .env 檔案內的所有密碼與 API Key！ [6, 7] 

------------------------------
## 3. 最佳實踐：使用 .env.example
為了讓團隊成員或部署環境知道專案需要哪些環境變數，通常會建立一個 .env.example 檔案（此檔案不要寫入真正的密碼），並將其提交給 Git 追蹤： [8, 9, 10, 11, 12] 
```ini
# .env.example 範例內容
PORT=3000
DATABASE_URL=your_database_url_here
API_KEY=your_api_key_here
```
其他人在複製（Clone）專案後，只需複製該檔案並改名為 .env，再填入他們自己的本地密碼即可。 [9, 13, 14, 15] 
您目前是在建立新專案，還是遇到了 .env 已經不小心推送到 GitHub 的問題呢？需要的話，我可以提供清除 Git 歷史紀錄中機密資料的完整指令。 [16] 

[1] [https://stackoverflow.com](https://stackoverflow.com/questions/43664565/why-do-people-put-the-env-into-gitignore)
[2] [https://github.com](https://github.com/orgs/community/discussions/189770)
[3] [https://stackoverflow.com](https://stackoverflow.com/questions/38983153/git-is-not-respecting-gitignore-instruction-to-ignore-env-files)
[4] [https://www.freecodecamp.org](https://www.freecodecamp.org/chinese/news/gitignore-file-how-to-ignore-files-and-folders-in-git/)
[5] [https://forum.freecodecamp.org](https://forum.freecodecamp.org/t/gitignore-of-env-file/550639)
[6] [https://github.com](https://github.com/orgs/community/discussions/126569)
[7] [https://engineersmeetai.substack.com](https://engineersmeetai.substack.com/p/how-to-completely-remove-a-env-file)
[8] [https://ithelp.ithome.com.tw](https://ithelp.ithome.com.tw/m/articles/10241730)
[9] [https://laracasts.com](https://laracasts.com/discuss/channels/laravel/gitignore-for-env)
[10] [https://gist.github.com](https://gist.github.com/subfuzion/db7f57fff2fb6998a16c)
[11] [https://www.reddit.com](https://www.reddit.com/r/learnpython/comments/1hnivqd/local_environment_variables_with_venv/)
[12] [https://stackoverflow.com](https://stackoverflow.com/questions/56765051/do-i-need-to-commit-env-files-into-the-repository/56765084)
[13] [https://www.gitguardian.com](https://www.gitguardian.com/videos/creating-a-gitignore-file)
[14] [https://www.reddit.com](https://www.reddit.com/r/django/comments/mpbv8s/what_is_the_best_way_of_storing_secret_keys_of/)
[15] [https://www.twilio.com](https://www.twilio.com/en-us/blog/working-with-environment-variables-in-node-js-html)
[16] [https://calmcode.io](https://calmcode.io/course/env-variables/gitignore)
