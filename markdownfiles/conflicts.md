git merge master readmes 

CONFLICT (rename/delete): README deleted in readmes and renamed to README.md in HEAD. Version HEAD of README.md left in tree.
Automatic merge failed; fix conflicts and then commit the result.

---



git checkout readmes 

README.md: needs merge
error: you need to resolve your current index first

---

git pull origin readmes 

error: Pulling is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.

---



git merge master readmes 
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.
rishabh@rishabh:~/githubrepos/test1$ git add .
rishabh@rishabh:~/githubrepos/test1$ git push origin master

---

git checkout readmes 
error: Your local changes to the following files would be overwritten by checkout:
	README.md
Please commit your changes or stash them before you switch branches.
Aborting

---

git checkout master 
D	README.md
A	gitLearning.md
A	linuxLearnings.md
A	typoraLearnings.md
Already on 'master'

---

What I did

Switch to master branch - git checkout master

git add .

git commit -m "resolving merge conflicts"

git push origin master

Switch to readmes - git checkout readmes

README.md file was there

git add .

git commit -m ""

git push

git merge 

It showed up in a new window asking why merge is necessary and I simply quit it by pressing ctrl+x and then it was successful





