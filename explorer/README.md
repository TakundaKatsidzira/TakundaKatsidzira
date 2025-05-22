🧭 EXPLORER: Terminal-Based Virtual File System
# (OOP: Encapsulation, Abstraction) The explorer class encapsulates all file/folder logic and exposes only necessary operations, hiding internal state and implementation details from the user. This abstraction allows users to interact with a simple interface while the complexity is managed internally.

EXPLORER is a terminal-based file explorer that simulates a virtual file system with robust functionality for file and folder management, access control, undo/redo, and analytics. It supports two user roles—Owner and User—each with distinct permissions, providing a secure and controlled environment for file operations.
# (OOP: Inheritance, Polymorphism) The Owner and User roles can be implemented as subclasses of a User base class. Inheritance allows shared logic (e.g., navigation) while polymorphism enables method overriding for permission checks and command access, so Owner and User behave differently for the same command.
# (Data Structures: Trees, Hash Maps) The file system is best modeled as a tree, where each node is a file or folder. Hash maps (dictionaries) are used for fast lookup of files/folders by name or path, and to map users to their permissions.
# (Algorithms: Traversal, Search) Tree traversal algorithms (DFS for recursive operations like tree display, BFS for breadth-wise listing) are used for commands like ls (list), tr (tree), and fd (find/search).

🚀 Getting Started
To start the application, run EXPLORER with the path to an empty directory:
# (OOP: Abstraction) The user interacts with a simple command-line interface, while the underlying implementation (file system, permissions, etc.) is abstracted away.

bash
Copy
Edit
./explorer /path/to/empty/directory
Upon launching:

Enter a 4-digit Owner Key.
# (OOP: Encapsulation) The Owner key is stored as a private attribute, ensuring only the Owner can access privileged commands. Encapsulation protects sensitive data from unauthorized access.

Choose to continue as either:

Owner Profile: Full permissions including setting user permissions.
User Profile: Limited to existing permissions (default: rw for created files/folders).
# (OOP: Inheritance/Polymorphism) The system uses inheritance to share common user logic, and polymorphism to allow Owner and User to override methods (e.g., permission checks, command execution).

📁 Core Features
✅ File & Folder Operations (CRUD)
All operations are run via terminal commands with flags:
# (OOP: Encapsulation) Each operation (create, delete, rename, move) is a method of the explorer class, which manages state changes and enforces rules.
# (Data Structures: Tree) Each file/folder is a node in the tree, with parent/child relationships.

Command	Description
sw	Switch between Owner and User profiles
# (OOP: Polymorphism) The active user object is switched, changing the behavior of permission checks and available commands.

cr	Create a file or directory
  -f <filename>	Create file
  -d <dirname>	Create directory
# (OOP: Encapsulation) Methods for creating nodes ensure only valid operations are performed, and permissions are set appropriately.
# (Data Structures: Tree) New nodes are added as children of the current directory node.

dl	Delete a file or directory
  -f <filename>	Delete file
  -d <dirname>	Delete directory
# (OOP: Encapsulation) Deletion methods check permissions and update the tree structure.
# (Algorithms: Tree Traversal) The node to delete is found via traversal, and references are updated to remove it.

rn <old> <new>	Rename a file or folder
# (OOP: Encapsulation) The rename method updates the node's name property, ensuring no naming conflicts.

mv <name> <path>	Move a file or folder to a directory
# (OOP: Encapsulation) The move method changes the parent pointer of a node, updating the tree structure and checking permissions.

ls	List current directory contents
  -f	Only files
  -d	Only directories
# (Algorithms: Tree Traversal) Lists children of the current directory node, optionally filtering by type.

tr	Display tree structure from current path
# (Algorithms: DFS/BFS) Recursively traverses and prints the subtree from the current node, using DFS for depth-first display.

lc	Print current working path
# (Data Structures: Stack/Array) The current path is tracked as a stack or array, allowing efficient navigation and display.

📄 File Content Access
Command	Description
rd <filename>	Read file
  -ul <n>	Read up to line n
  -ol <n>	Read only line n
# (OOP: Encapsulation) The file read method checks permissions before accessing content.
# (Algorithms: File I/O, Slicing) Efficiently reads only the requested lines, minimizing memory usage.

wr <filename>	Write to file
  -a	Append instead of overwrite
# (OOP: Encapsulation) The file write method checks write permissions and updates content, supporting both overwrite and append modes.

⏪ Version Control
Command	Description
un	Undo last state-altering command (cr, dl, mv, rn)
# (Data Structures: Stack) A stack is used to store snapshots or command objects representing previous states, enabling undo functionality.
# (Algorithms: Command Pattern) Each operation is encapsulated as a command object, which can be reversed by calling its undo method.

📊 Analytics
Command	Description
tp	Top-N files
bt	Bottom-N files
  -n <number>	Number of files to return
  -r	Sort by recency
  -s	Sort by size
  -o	Return only the Nth file
  -a	Search recursively in subdirectories
# (Algorithms: Sorting, Heap) Heaps (priority queues) are used to efficiently find the top/bottom N files by size or recency, rather than sorting the entire list.
# (Data Structures: Heap, Priority Queue) These structures allow for fast insertion and retrieval of the largest/smallest elements.

🔍 Search
Command	Description
fd <name>	Search for file/folder
  -f	Search for file
  -d	Search for directory
# (Algorithms: DFS/BFS, String Matching) The search traverses the tree (DFS or BFS) and uses string matching to find nodes with matching names.

❌ Exit
Command	Description
ex	Exit program safely (keyboard interrupts are disabled)
# (OOP: Encapsulation) The exit method ensures all resources are cleaned up and state is saved if needed, hiding cleanup logic from the user.

🔐 Permissions System
Owner Permissions
Full CRUD capabilities.

Can set or modify file/folder permissions for users.
# (OOP: Encapsulation) Permissions are stored as private/protected attributes, only modifiable by the Owner.
# (Data Structures: Hash Map) Permissions are mapped from users to files/folders using hash maps for fast access.

User Permissions (default rw on creation)
Can read/write to files and folders they have access to.

Cannot change permissions.

File Permissions:

read, write

Folder Permissions:

read, write

These permissions only apply to the User profile. The Owner has full access regardless of permissions.
# (OOP: Inheritance/Polymorphism) The Owner class overrides permission check methods to always grant access, while User checks actual permissions.

📁 Folder Permissions
Permission	Allows User to...	Affects Commands
read	View contents of the folder	ls, tr, fd, tp, bt, lc
write	Modify contents of the folder	cr, dl, mv, rn, writing files inside the folder

# (OOP: Encapsulation) Permission checks are performed before each operation, ensuring users cannot bypass restrictions.

🚫 No read on folder:
ls, tr, fd, tp, bt will not list contents but will list folder in parent directory. ls will not show tree beyond folder as root but will show up in tree of parent folder. files not searched by fd, tp, bt but can mv into folder. lc location and create files and folders you will have rw permissions on. You can delete files you know the names of and even rename them whether you made them or not.
# (OOP: Encapsulation) These behaviors are enforced by encapsulating permission logic in the folder's methods.

🚫 No write on folder:
Can't create (cr) files/folders inside it.
Can't delete (dl) anything in it.
Can't move (mv) things into it or around in it.
Can't rename (rn) anything within it. 
Can only ls, lc, tree, fd, tp, and bt.
# (OOP: Encapsulation) Write restrictions are checked before any modifying operation.

# (OOP: Encapsulation) Permission logic encapsulated in folder methods.

📄 File Permissions
Permission	Allows User to...	Affects Commands
read	View file contents	rd, tp, bt, fd,
can read contents and files shows up in tp, bt, ls, tr, and fd

write	Modify file contents	wr, mv, rn, dl (deletion of file)
can rename, move, write to, and delete

🚫 No read on file:
Cannot read using rd.
Cannot analyze with tp, bt.

🚫 No write on file:
Cannot write (wr) to file.
Cannot rename (rn) or move (mv) the file.
Cannot delete (dl) the file.

# (OOP: Encapsulation) File methods check permissions before action, preventing unauthorized access or modification.

By default, files/folders created by the User have rw permissions (for that user only)
# (OOP: Constructor/Initialization) Default permissions are set in the constructor, ensuring new objects start with a secure state.

TO change permissions owner can use cp command with flags

cp <path> 
✔️ Flags
Flag	Description
-r	Add read permission
-w	Add write permission
--r	Remove read permission
--w	Remove write permission

# (OOP: Encapsulation) The cp method modifies permission attributes, ensuring only the Owner can change them and enforcing all rules internally.

Only the Owner can use this command. It will return:

0 if permissions updated successfully

1 if the command fails (invalid path, not owner, etc.)
# (OOP: Exception Handling) Return codes are used for error handling, allowing the program to respond appropriately to failures (e.g., invalid path, insufficient permissions).

