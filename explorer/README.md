
EXPLORER is a terminal-based file explorer that simulates a virtual file system (VFS) with support for CRUD operations, searching, sorting and ranking. Designed for speed and extensibility, EXPLORER is driven entirely through the terminal

🧠 Internal Architecture

⚙️ MODULARITY
📂 FILESYSTEM (filesystem.py)
Core VFS Management
Defines data models:
FileNode for files
DirectoryNode for directories
Each node tracks: name, path, type, created_time and  size
Maintains metadata (e.g., size, timestamps, paths)
FileSystem as the root container and manager
Tree (N-ary) For directory hierarchy
Initialization & State
Creates new or loads existing file system from state.json
Maintains and updates persistent state
State is auto-saved to `data/state.json`
Implements all CRUD operations on files and directories

🧰 UTILS (utils.py)
Output & Errors
Pretty-printing for trees, paths, results
Centralized error formatting and messaging
Help Manual
Structured dictionary-based help guide with usage examples
Helpers & Algorithms
Search (DFS/BFS)
DFS/BFS For search and structure traversal
Cache Reuse expensive traversal results, Caching frequently used traversal results
Sorting & ranking logic for top/bottom-N queries
Heap For top/bottom-N ranking

🧾 COMMANDS (commands.py)
Command Validation
Ensures command names, arguments, and paths are valid
Argument Handling
Path validation and resolution
Parses flags and options (e.g., -a, -d)
Transforms user input into actionable parameters
Function Dispatch
Maps user commands to appropriate FILESYSTEM or UTILS methods
Catches Errors & Handles Output
Acts as a middle layer between I/O (user) and core logic
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


💻 EXPLORER (explorer.py)
Main Interface
Attemplts to load a previous state and initializes new state if it fails
You'll be placed in the root (`/`) directory and prompted to enter commands:
Terminal-based REPL loop (>> prompt)
>>
Input Parsing
Tokenizes input into command and argument list
Orchestration
Routes parsed input to COMMANDS
Handles program lifecycle: launch, run, exit
Use `ex` to save and exit (keyboard interrupt is disabled)
HashMap Fast lookup by path and help dictionary
