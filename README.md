
-Status : Deprecated

Program to sort given folder. (Horribly innefient needs refactoring) 

- The program searches through the files and selects the different file types and sorts them into their respective folders of the same type if no folder exists it will make a new folder.

- custom flags and commands can be set.

- flags:

(-h) help command and displays how to use and the commands and flags 

(-c) custom file type (WIP)

(-f) from (sorts from a given website) and puts the rest in other folder (-dep-)

(-o) used with -f (ie -f -o) sorts only from the given website (-dep-)




Entry example

file_sorter.py "file location" -flag 

example

"/Downloads"

"/Downloads" -c ".pdf"

will sort only .pdf files in the folder "/Downloads"

"/Downloads" -c ".pdf" -f "umn.instructure"

will sort only .pdf files from the site umn.instructure (this program was designed with this website in mind and will sort between the classes umn.instructure.com/courses/213213/files/ from the courses it will recognize that all .pdf files from the same /courses/"number" are from the same class and will save it to different folder for each class) the other .pdf will be sorted into another folder unless specified by the -f -o flag 


