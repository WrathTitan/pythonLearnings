# Linux Learnings

#Terminal Info - name@nameofmachine: ~$ 
The tilde ~ is for the directory you are in and the $ to show if you are a user a # to show if you are the super user or root user

Directories in blue colour; files in white colour

### Commands Learnt:

1. **pwd** - path of the current working directory is shown

2. **cd**- to change directories
   `cd ..`  To go back to the previous directory level and
   `cd .` To remain in the current directory.
   `cd directory/path/` To go to a particular directory



3. `mkdir`-> To make a directory
   `mkdir directoryname` To create a folder/directory with the name directoryname

4. `whoami` - to see the name of the user logged in

5. `date`

6. `time`

7. `clear `- to clear the terminal

8. `help `- to display help about terminal commands Ex: help time - to display help about the time command

9. `ls` - to list all the files in the directory

10. `ls -l  `-> to display additional information about all files in the directiory, i.e., author name, group, size in bytes and last modification date 
    `ls -a` -> to display the hidden files in a directory

11. `ls -R .  ` ->To display all files in the directory and subdirectory

    ```
    drwxr-xr-x 3 rishabh rishabh 4096 Jan  9 14:37 Documents
    -rw-rw-r-- 1 rishabh rishabh 701 Jan  9 14:47 'Commands Learnt.md'
    ```

    The first letter identifies whether it is a directory or a file (d for directory and - for a file)Next group of 3 characters - first one is author permission, second one is group permissions, and the third one for any external user outside the specified the group. The permission are r-> reading, w-> writing, and x->execution

12. `$ chmod u-x exec.sh ` This removes the execution access from the author user u. 
    Whereas u+wx will give write and execution access to user u.

13. `touch `-> To create a file
    `touch ./Documents/'Markdown Files'/myfile `  This creates a file in Documents->Markdown Files-> myfile.txt

14. `mv `-> To move a file from one place to another without changing its content
    Ex: file.txt moved from Downloads to Markdown Files folder

    ```
    touch file.txt
    ls => file.txt  'Markdown Files'
    mv ./file.txt ./'Markdown Files'/
    ls =>'Markdown Files'
    cd Markdown\ Files/
    ls =>'Commands Learnt.md'   file.txt   myfile
    ```

15. `mv `-> Can also be used to move and rename files

    ```
    mv ./myfile ../myfilenew
    ls => 'Commands Learnt.md'   file.txt
    cd ..
    ls =>'Markdown Files'   myfilenew
    ```

16. `cp` -> To create a copy of a file

    ```
    cp -r ./Green ./White => Copies the content of an entire folder into another folder
    
    cp -r ../newfolder ./
    ```

17. `rm` -> To remove/delete a file won't work on folders

    ```
    rm -R -> To remove a folder and all its contents
    rm -rf -> To delete all the files in a folder including the hidden and non writeable files (examples while deleting a .git repo folder)
    ```

18. `cat ` -> to show the contents of a file in the terminal

19. `history` -> To show all the commands executed in order

20. To execute an file example a Bash script called 'exec.sh'  type ` ./exec.sh` 

21. To use a symbolic shortcut to run a file instead of using its entire path we can create a symbolic shortcut by the command => `ln -s ./Downloads/exec.sh `==> This will make exec.sh turn into a different colour. Then we can execute it anywhere using `./exec.sh `command

22. `find `-> To search for a file

23. `find *.pdf` -> To search for any pdf file

24. vim
    vi filename -> to open the file in the vim editor
    to save :w
    to quit :q
    yy to copy entire line
    p to paste the entire line
    U to undo

 df -> command to view the status of the system disks
df -h -> To check in an easier way

ps aux -> Shows all the applications in progress launched by the users and the superusers

sudo apt-get install
sudo apt-get update

Aptitude -> By default is not there so to install it use 
sudo apt-get install aptitude
sudo aptitude update
sudo aptitude upgrade
sudo aptitude search xx

nan -> To get tips on any command and the u to exit it. Ex: nan ls
or --help  to get help on a command. Ex ls --help

---

* Ctrl+C is used to kill a process 

* Ctrl+Z is used to suspend a process - but it runs in the background
  We can use `fg` to run the process again in the foreground. or `bg` in the background

* `jobs` command can be used to see the currently active processes. It gives output like this:

  ```
  [1]- Stopped cat
  [2]+ Stopped vi
  ```

  We can use the `kill` command to kill a suspended process in the background

* ```
  kill %n
  ```

  The above command can be used to kill a suspended process in the background using the number `n` shown by the `jobs` command.







