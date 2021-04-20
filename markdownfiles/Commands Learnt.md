#Terminal Info - name@nameofmachine: ~$ 
The tilde ~ is for the directory you are in and the $ to show if you are a user a # to show if you are the super user or root user

Directories in blue colour; files in white colour

Commands Learnt:

pwd - path of the current working directory is shown



cd - to change directory Ex: cd .. -> To go back to the previous directory level and cd . -> to remain in the current directory.

mkdir -> To make a directory

whoami - to see the name of the user logged in

date

time

clear - to clear the terminal

help - to display help about terminal commands Ex: help time - to display help about the time command

ls - to list all the files in the directory

ls -l  -> to display additional information about all files in the directiory, i.e., author name, group, size in bytes and last modification date

ls -R .   ->To display all files in the directory and subdirectory

drwxr-xr-x 3 rishabh rishabh 4096 Jan  9 14:37 Documents

-rw-rw-r-- 1 rishabh rishabh 701 Jan  9 14:47 'Commands Learnt.md'

The first letter identifies whether it is a directory or a file (d for directory and - for a file)

Next group of 3 characters - first one is author permission, second one is group permissions, and the third one for any external user outside the specified the group. 

The permission are r-> reading, w-> writing, and x->execution

Ex: $ chmod u-x exec.sh -> This removes the execution access from the author user u. Whereas u+wx 

touch -> To create a file

touch ./Documents/'Markdown Files'/myfile -> This creates a file in Documents->Markdown Files-> myfile.txt

mv -> To move a file from one place to another without changing its content

Ex: file.txt moved from Downloads to Markdown Files folder

touch file.txt
ls => file.txt  'Markdown Files'
mv ./file.txt ./'Markdown Files'/
ls =>'Markdown Files'
cd Markdown\ Files/
ls =>'Commands Learnt.md'   file.txt   myfile

mv -> Can also be used to move and rename files

mv ./myfile ../myfilenew
ls => 'Commands Learnt.md'   file.txt
cd ..
ls =>'Markdown Files'   myfilenew

cp-> To create a copy of a file

cp -r ./Green ./White => Copies the content of an entire folder into another folder

cp -r ../newfolder ./

rm-> To remove/delete a file won't work on folders

rm -R -> To remove a folder and all its contents

cat -> to show the contents of a file in the terminal

history -> To show all the commands executed in order

To execute an file example a Bash script called 'exec.sh'  => ./exec.sh

To use a symbolic shortcut to run a file instead of using its entire path we can create a symbolic shortcut by the command => ln -s ./Downloads/exec.sh ==> This will make exec.sh turn into a different colour.

Then we can execute it anywhere using ./exec.sh command

find -> To search for a file

find *.pdf

vim
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







