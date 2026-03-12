# master
master change

master と0a2ed76を同期したい
一旦0a2ed76背後に戻ってないとpullできない

*   a865af7 (HEAD -> master, origin/master) Merge branch 'master' 
|\  
| * 0a2ed76 (origin/release-st, release-st) master
* | 7b5346c git check
|/  
* 66c9713 test
*   2cc2e78 Merge branch 'master' of https://github.com/ycntokyo/master into release-st

git checkout master
git reset --hard 66c9713
git push origin master -f

* 0a2ed76 (origin/release-st, release-st) master
* 66c9713 (HEAD -> master, origin/master) test
*   2cc2e78 Merge branch 'master' of https://github.com/ycntokyo/master into release-st
|\  
| * 6f0167e ignore
* | 7ab72f4 gitignore
|/  
* 5013a80 add

git pull origin release-st

* 0a2ed76 (HEAD -> master, origin/release-st, release-st) master
* 66c9713 (origin/master) test
*   2cc2e78 Merge branch 'master' of https://github.com/ycntokyo/master into release-st
|\  
| * 6f0167e ignore
* | 7ab72f4 gitignore
|/  
* 5013a80 add

 git push

 * 0a2ed76 (HEAD -> master, origin/release-st, origin/master, release-st) master
* 66c9713 test
*   2cc2e78 Merge branch 'master' of https://github.com/ycntokyo/master into release-st
|\  
| * 6f0167e ignore
* | 7ab72f4 gitignore
|/  
* 5013a80 add

別のブランチにpushはできないようだ
別のブランチに切り替えてpullしたらよい


