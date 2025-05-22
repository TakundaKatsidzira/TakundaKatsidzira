🧭 EXPLORER: Terminal-Based Virtual File System

EXPLORER is a terminal-based file explorer that simulates a virtual file system with robust functionality for file and folder management, access control, recall of previous commands, and analytics. It supports two user roles—Owner and User—each with distinct permissions, providing a secure and controlled environment for file operations.

🚀 Getting Started
To start the application, run EXPLORER with the path to an empty directory:



Enter a 4-digit Owner Key.

Choose to continue as either:

Owner Profile: Full permissions including setting user permissions.
User Profile: Limited to existing permissions (default: rw for created files/folders).

📁 Core Features
✅ File & Folder Operations (CRUD)
All operations are run via terminal commands with flags:

Command	Description
sw	Switch between Owner and User profiles

cr	Create a file or directory
  -f <filename>	Create file
  -d <dirname>	Create directory

dl	Delete a file or directory
  -f <filename>	Delete file
  -d <dirname>	Delete directory

rn <old> <new>	Rename a file or folder

mv <name> <path>	Move a file or folder to a directory

ls	List current directory contents
  -f	Only files
  -d	Only directories

tr	Display tree structure from current path

lc	Print current working path

📄 File Content Access
Command	Description
rd <filename>	Read file
  -ul <n>	Read up to line n
  -ol <n>	Read only line n

wr <filename>	Write to file
  -a	Append instead of overwrite

📊 Analytics
Command	Description
tp	Top-N files
bt	Bottom-N files
  -n <number>	Number of files to return
  -r	Sort by recency
  -s	Sort by size
  -o	Return only the Nth file
  -a	Search recursively in subdirectories

🔍 Search
Command	Description
fd <name>	Search for file/folder
  -f	Search for file
  -d	Search for directory

📜 Command Recall
Command	Description
rc	Recall a previous command from history
  -n <number>	Recall the nth previous command (e.g., rc -3 recalls the third most recent command)

❌ Exit
Command	Description
ex	Exit program safely (keyboard interrupts are disabled)

🔐 Permissions System
Owner Permissions
Full CRUD capabilities.

Can set or modify file/folder permissions for users.


User Permissions (default rw on creation)
Can read/write to files and folders they have access to.

Cannot change permissions.

File Permissions:

read, write

Folder Permissions:

read, write

These permissions only apply to the User profile. The Owner has full access regardless of permissions.

📁 Folder Permissions
Permission	Allows User to...	Affects Commands
read	View contents of the folder	ls, tr, fd, tp, bt, lc
write	Modify contents of the folder	cr, dl, mv, rn, writing files inside the folder

🚫 No read on folder:
ls, tr, fd, tp, bt will not list contents but will list folder in parent directory. ls will not show tree beyond folder as root but will show up in tree of parent folder. files not searched by fd, tp, bt but can mv into folder. lc location and create files and folders you will have rw permissions on. You can delete files you know the names of and even rename them whether you made them or not.


🚫 No write on folder:
Can't create (cr) files/folders inside it.
Can't delete (dl) anything in it.
Can't move (mv) things into it or around in it.
Can't rename (rn) anything within it. 
Can only ls, lc, tree, fd, tp, and bt.
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

By default, files/folders created by the User have rw permissions (for that user only)

TO change permissions owner can use cp command with flags

cp <path> 
✔️ Flags
Flag	Description
-r	Add read permission
-w	Add write permission
--r	Remove read permission
--w	Remove write permission

Only the Owner can use this command. It will return:

0 if permissions updated successfully

1 if the command fails (invalid path, not owner, etc.)


