## TAKUNDA KATSIDZIRA
# 👋 Hey there, 

Welcome to my GitHub profile! I'm a Computer Science Student passionate about problem solving, data driven insights and development.

## GOALS
*  Learn Python;
*  Learn OOP and Data Structures and Algorithms;
*  Write readable, maintanable code and work on testing and debugging
*  Complete Projects;

## COURSES
*  CS50P;
*  Data Structures and Algorithms;
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

* Game optimized for performance, where the computer plays itself using different strategies. Logs include: who played first, was it a draw, who won, did the first player win, first move position, full move sequence, number of moves, and win method (e.g., row_1, diag_anti) saved to a CSV file.
* Develop multiple computer agents with different strategies.
* Backtracking can be used to simulate future game states and evaluate optimal moves (e.g., using minimax).
* Use bitmasks to simulate the board and agents moves

**Techniques:**
* **Backtracking**: Simulate future game states with Minimax to find the best move.
* **Bit Manipulation**: Represent board states compactly using bitmasks for speed.

**Data Structures:**
* **Hash Maps**: Cache board state evaluations (memoization).
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

**Data Structures:**
* **2D Arrays**: Represent the board.
* **Hash Maps**: Track card/token ownership.

## Explorer

* A file explorer for creating, reading, updating, and deleting files/folders starting from a root directory. 
* The filesystem is structured as a tree, and symbolic links (if supported) can introduce a DAG structure.
* Heaps can identify top-N largest or most recent files.

**Techniques:**
* **Heap**: Top-n analytics.
* **Stack**: Command history.

**Data Structures:**
* **Trees**: Represent folder hierarchy.
* **Stacks**: Command/operation history.
* **Heaps**: Find top-N largest or most modified files.


## Crawly

* Build a DAG using links found in text files and analyze to track dependencies or find cycles. The goal is to recursively traverse all links, Find dead links (unreachable), Identify leaf nodes (files with no further links), Rank files by size and by how often they were traversed, identify dependacies and dependancy depth,Find shortest path from root to leaf nodes

**Techniques:**
* **DFS & BFS**: Traverse page links recursively or level-wise.
* **Backtracking**: Roll back from dead or looped links.
* **Dynamic Programming**: Cache visited URLs to prevent re-crawling.
* **Topological Sort**: Analyze dependency/order of linked pages.
* **Hashing**: Track depth and reachability metrics.
* **Top K elements to rank files by how often they are traversed and size**


**Data Structures:**
* **Graphs**: Represent the hyperlink structure.
* **Trees**: Store crawl structure with depth.
* **Hash Maps**: Store visited URLs with metadata.
* **Stacks/Queues**: For DFS/BFS implementations.

