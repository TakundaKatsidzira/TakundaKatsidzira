## TAKUNDA KATSIDZIRA
# 👋 Hey there, 

Welcome to my GitHub profile! I'm a student passionate about data driven insights

## 🚀 About Me

Learning Programming with a interest in real world problem solving and AI

## GOALS
*  Learn Python;
*  Learn OOP and Data Structures and Algorithms;
*  Write readable, maintanable code and work on testing and debugging
*  Complete Projects;

## COURSES
*  CS50P;
*  CS50AI;

## BOOKS
*  Automate The Boring Stuff With Python;
*  Beyond The Basic Stuff In Python;

## DATA STRUCTURES AND ALGORITHMS
*  Algorithm Analysis;
*  Arrays and Hashing;
*  Stacks and Queues;
*  Linked Lists;
*  Searching, Sorting and Recursion;
*  Two Pointers, Fast and Slow Pointers and Sliding Window;
*  Merge Intervals;
*  Cyclic Sort;
*  Subsets;
*  Modified Binary Search;
*  Prefix Sum;
*  Monotonic Stack;
*  In Place Reversal Of Linked List;
*  
*  Trees and Tries;
*  Heaps;
*  Graphs;
*  Breadth and Depth First Search;
*  Two Heaps;
*  Top K Elements;
*  K way Merge;
*  Backtracking;
*  Dynamic Programming;
*  Greedy Algorithms;
*  Topological Sort;
*  Matrix Traversal;
*  
*  Bit Manipulation;
*  BITWISE XOR;

## LEETCODE
*  Blind 75;
*  Neetcode 150;


## PROJECTS

## TicTacToe

* Game optimized for performance, where the computer plays itself using random choices (no strategy). Logs include: who played first, was it a draw, who won, did the first player win, first move position, full move sequence, number of moves, and win method (e.g., row_1, diag_anti) saved to a CSV file.
* Develop multiple computer agents with different strategies.
* Backtracking can be used to simulate future game states and evaluate optimal moves (e.g., using minimax).
* Dynamic programming can cache board evaluations to avoid redundant computation during simulations.

**Techniques:**
* **Backtracking**: Simulate future game states with Minimax to find the best move.
* **Dynamic Programming**: Cache board evaluations to avoid recomputation during simulations.
* **Bit Manipulation**: Represent board states compactly using bitmasks for speed.
* **Prefix Sum**: Track cumulative results (like win rates for certain opening moves).
* **Top K Elements**: Analyze the most common winning sequences/moves over many games.

**Data Structures:**
* **Arrays**: Represent the game board (3x3 grid).
* **Hash Maps**: Cache board state evaluations (memoization).
* **Heaps**: Store top strategies by win rate or efficiency.
* **Stacks**: Enable undo/redo functionality for game simulations or replays.


## Sequence

* Build an accurate version of the Sequence game.
* Implement board logic, card handling, and rules.
* Support two or three players or teams.
* Optimize for performance and allow AI agents with a mix of strategy and randomness.
* Backtracking can simulate token placements and analyze optimal sequences.
* Dynamic programming helps detect sequences efficiently on the grid by caching token alignments.

**Techniques:**
* **Backtracking**: Simulate placing tokens to explore future winning sequences.
* **Dynamic Programming**: Cache aligned token sequences to speed up win detection.
* **Sliding Window**: Detect 5-in-a-row sequences on the board.
* **Two Pointers**: Scan for sequences in linear directions.
* **Prefix Sum**: Accelerate count of token alignments.

**Data Structures:**
* **2D Arrays**: Represent the board.
* **Hash Maps**: Track card/token ownership.
* **Tries**: Store patterns for token placement or card sequences.
* **Graphs**: Represent player adjacency or strategic clustering.
* **Stacks**: Allow undoing of token placements.

## Explorer

* A file explorer for creating, reading, updating, and deleting files/folders starting from a root directory. Includes user/owner permissions and role-based access.
* Command history and undo supported via a stack.
* Autocorrect for commands and paths using edit distance + dynamic programming.
* Trie stores valid commands and paths for fast prefix search and autocorrect.
* The filesystem is structured as a tree, and symbolic links (if supported) can introduce a DAG structure.
* Backtracking enables undo/redo of file operations.
* Heaps can identify top-N largest or most recent files.

**Techniques:**
* **Prefix Tree (Trie)**: Fast path/command suggestions.
* **Stack**: Command history and undo.

**Data Structures:**
* **Trees**: Represent folder hierarchy.
* **Tries**: Autocomplete paths.
* **Stacks**: Command/operation history.
* **Hash Maps**: Track permissions, file metadata.
* **Heaps**: Find top-N largest or most modified files.


## Crawly

## Given as a root a single text file URL, this file contains links to other files that contain links to other files and so on, Each of those links might also contain more links or be empty files forming a directed acrylic graph. 

  ## **The gaol is to recursively traverse all links**
## **detect cycles**
## **Find dead links (unreachable)**
##**Identify leaf nodes (files with no further links)**
##**Rank files by size and by how often they were traversed**
##**identify dependacies and dependancy depth**
##**Find shortest path from root to leaf nodes**
##**Use data structures and algorithms such as DFS,BFS, Topological Sort, Cyclic sort,hashing, Stacks and Queues, heaps, two heaps, Top K elements, backtracking , dynamic programming, bit manipulation with bitmasks,**
## **Log analytics as well as statistics time and space complexity of data structures and algorithms used**
## **Produce a report with details  of the analysis and computational complexity**


**Techniques:**
* **DFS & BFS**: Traverse page links recursively or level-wise.
* **Backtracking**: Roll back from dead or looped links.
* **Dynamic Programming**: Cache visited URLs to prevent re-crawling.
* **Topological Sort**: Analyze dependency/order of linked pages.
* **Hashing**: Track depth and reachability metrics.
* **Bitmasks can effeciently encode sets of visited nodes**
* **Top K elements to rank files by how often they are traversed and size**
* **Two pointers can be an alternative way to detect cycles**


**Data Structures:**
* **Graphs**: Represent the hyperlink structure.
* **Trees**: Store crawl structure with depth.
* **Hash Maps**: Store visited URLs with metadata.
* **Stacks/Queues**: For DFS/BFS implementations.

