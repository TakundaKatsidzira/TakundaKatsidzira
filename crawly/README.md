## Crawly
✅ PROJECT OVERVIEW

Project Name: Crawly
📁 PROJECT STRUCTURE
Got it! Here's your project tree with inline comments explaining the purpose of each file or folder:

```
crawly/
├── src/                            # Core logic for crawling, analyzing, and reporting
│   ├── __init__.py                 # Initializes the src module
│   ├── crawly.py                   # Main entry point: argument parsing, orchestrates all components
│   ├── graph_builder.py           # Builds the hyperlink graph from text URLs (DFS/BFS traversal)
│   ├── analyzer.py                # Analyzes the graph: cycles, leaf nodes, dead links, ranks, stats
│   ├── utils.py                   # Helper functions: URL handling, memoization, metrics
│   └── report_generator.py        # Generates text-based summary report from analysis results
├── data/                           # Output and temporary files
│   ├── cache/                      # Cached raw files or intermediate data
│   └── analysis_report.txt         # Generated report with structure stats, rankings, metrics
├── scripts/                        # Shell scripts for automation
│   ├── run.sh                      # Runs the main Crawly pipeline with default args
│   ├── test.sh                     # Runs unit tests
│   └── clean.sh                    # Cleans up cached files and reports
├── tests/                          # Unit tests for core modules
│   ├── __init__.py                 # Initializes the tests module
│   ├── test_crawly.py              # Tests for CLI and orchestration logic in crawly.py
│   ├── test_graph_builder.py       # Tests graph construction from linked text files
│   └── test_utils.py               # Tests for helper functions (e.g., hashing, tracking)
├── README.txt                      # Project overview, features, usage, and output description
└── .gitignore                      # Files and directories to exclude from version control
```

Purpose: Recursively traverse a directed acyclic graph (DAG) of text files linked by URLs hosted in github project repo, analyze structure, detect cycles, find leaf and dead nodes, compute dependency depth, and rank files by traversal count and size.
Run analysis from terminal with commands using argeparse to do the following controllinf flags for depth and number etc and check for
Features:
DFS & BFS for traversal
Cycle and dead link detection
Leaf node identification
Dependency and depth analysis
File ranking
Complexity analytics and statistics
Report generation
🧾 INPUT REQUIREMENTS
A text file URL (e.g., https://example.com/root.txt) as root input.
Each file contains plain text URLs, one per line.
Files may reference other files (forming a DAG or cycles).

--report report/analysis_report.txt
--verbose

🔁 INPUT SEQUENCE & LOGIC FLOW
Fetch Root URL
-> Parse contents into a list of links

Build Graph (graph_builder.py)
-> Recursively fetch and parse linked files
-> Track visited URLs to avoid duplication
-> Store structure as adjacency list

Analyze (analyzer.py)

DFS to detect:
Cycles using visited set and recursion stack
Leaf nodes (nodes with no children)
Dead links (404s or invalid files)
BFS for shortest path to leaf
Topological Sort for dependency order
Hashing and bitmasking for memoization and visit tracking
Top-K Heap for ranking files by size or visit frequency
Log Time/Space Complexity
Count nodes, edges, recursion depth, memory usage, etc.

Generate Report

FEATURES:
----------
- * Detect cycles using DFS
- * Find leaf nodes (files with no further links)
- * Identify dead/unreachable links
- * Rank files by:
  * Size
  * How frequently they're traversed
- * Calculate dependency depth
- * Compute shortest path from root to leaf using BFS
- * Generate analytics:
  * Time and space complexity of traversal
  * Structure stats
  * Dependency analysis

DATA STRUCTURES USED:
----------------------
- Graphs (Adjacency List)
- Stacks, Queues
- Hash Maps
- Bitmasks (for visited tracking)
- Heaps to rank files
- Dynamic Programming (memoization)
- Topological Sort dependancies

OUTPUT:
--------
Generates:

- output report to terminal
- Logs and runtime metrics

- Summary of:
   * Total nodes
   * Dead links
   * Leaf files
   * Cycles
   * Most linked files
   * File size ranks
   * Graph depth
   * Page Tree Hierarchy
   * Topological Sort of Pages, treating links as dependencies.


DEPENDENCIES:
--------------
- requests
- tqdm
- heapq
- collections
