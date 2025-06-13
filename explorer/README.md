EXPLORER
A terminal-based file explorer that simulates a virtual file system (VFS) with support for CRUD operations, searching, sorting and ranking. Designed for speed and extensibility, EXPLORER is driven entirely through the terminal

🧠 Internal Architecture

Parses flags and options (e.g., -a, -d)
Commands for directories recursively work on all subdirectories on all files
Commands that do not print will return text if successful or not successful
Commands will work on files by default with -d flag for directories 
cr, creates files or directories, cr notes.txt or create notes -d.  
dl, deletes files or directories, dl notes.txt or delete notes -d. 
lc, prints current working directory 
cd, changes current working directory, change to parent directory by default, optional path argument, cd logs or cd 
rd, prints all contents of a file by default, optional argument to read n lines,  rd logs/data.txt or rd data.txt 4
wr, overwrites a files content by default, -a to append. wr logs/data.txt "text", wr logs/data.txt "new text" -a
fd, searches for files or directories by name from current directory and prints path, fd data.txt or fd logs -d for directories 
tp, prints list of paths of top-n,1 by default,  size by default -d for created date, tp or tp 3 or tp 4 -d
bt, prints list of paths of bottom-n, 1 by default files, size by default, -d for created date, bt or bt 6 or bt 2 -d
ls, prints list of files and directories in current working directory by default, optional path argument,  ls /logs
tr, prints tree structure from current working directory by default, optional path argument, tr ../data 
hp, prints help manual by default, optional argument to print for specific command, hp or hp tp, manual is dict of dicts
ex, exits program and saves state to json by default, optional argument to not save, ex or ex !


Attemplts to load a previous state and initializes new state if it fails
You'll be placed in the root (`/`) directory and prompted to enter commands:
Terminal-based  loop (>> prompt)
>>
