# **Distributed vs Central**

## **Central** - Subversion(VCS), CVS, Perfore

There is a single “central” copy of your project somewhere (probably on a server), and programmers will “commit” their changes to this central copy.

**Advantages** - pushing and pulling is faster

## **Distributed**- Git, Mercurian, Bazaar

Every developer “clones” a copy of a repository and has the **full** history of the project on their own hard drive. This copy (or “clone”) has *all* of the metadata of the original. 

**Advantages**

**Git commands I used**

1. To initialise an empty git repository on the system

   ```
   git init
   ```

   

2. To add all the files in the current directory to be commited

   ```
   git add .
   ```

   

3. To check the status of the files added. This shows the added and/or edited or removed files in green or red colour

   ```
   git status
   ```

   

4. Make the changes ready to be commited to the remote server -m to put a message here

   ```
   git commit -m "message here"
   ```

   

5. Push the changes to the remote server i.e., push the changes from the local master branch to the origin or the remote branch

   ```
   git push origin master
   ```

   

6. To pull the changes from the remote, here in case of other branches have to write 2 additional arguments

   ```
   git pull
   ```

   

7. To clone a repository from its url

   ```
   git clone https://www.github.com/WrathTitan/testrepo.git
   ```

8. To set up the name and email globally

   ```
   git config --gloabl user.name "name"
   git config --global user.email "email@id.com"
   ```

9. Creating a branch

   ```
   git branch branchname
   ```

   

10. Switching to a different branch

    ```
    git checkout branchname
    ```

    or

    ```
    git switch branchname
    ```

    

11. Merging branches - to merge branchB to branchA

    ```
    git merge branchA branchB 	
    ```

    

12. Pushing from a branch to the remote

    ```
    git push origin branchname
    ```

    

13. Going through logs

    ```
    git log
    ```

    

14. Going through reflogs

    ```
    git reflog
    ```

    

15. Adding a remote repo url - to add a remote repository with the name/alias as origin and the link which is the url

    ```
    git remove add origin link
    ```

    

16. Seeings all the remote urls set

    ```
    git remote -v
    ```

    

17. Resetting commits that haven't been pushed yet

    ```
    git reset --merge ORIG_HEAD
    ```


---

Some things I tried out:

1. Merging branches and resetting it

```
git merge master readmes	#merged readmes branch with master branch 

#since I did not commit I used
git log

#or
git reflog	#to see the logs

#then did 
git reset --merge ORIG_HEAD			#this reverts it to the previous commit stage
```

2. Directing adding files and commiting in one step - but it won't include newly added files. Only modified files are commited

   ```
   git commit -am "Message"
   ```

   