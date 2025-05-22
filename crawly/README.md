## Crawly
✅ PROJECT OVERVIEW

Project Name: Crawly

Purpose: Recursively traverse a directed acyclic graph (DAG) of text files linked by URLs, analyze structure, detect cycles, find leaf and dead nodes, compute dependency depth, and rank files by traversal count and size.

Features:

DFS & BFS for traversal

Cycle and dead link detection

Leaf node identification

Dependency and depth analysis

File ranking

Complexity analytics and statistics

Report generation

📁 PROJECT STRUCTURE

crawly/
│                    
├── src/
│   ├── __init__.py
│   ├── crawly.py
│   ├── graph_builder.py
│   ├── analyzer.py
│   ├── utils.py
│   └── report_generator.py
├── data/
│   └── cache/
|   └── analysis_report.txt
├── scripts/
│   └── run.sh
|   └── test.sh
|   └── clean.sh
├── tests/
│   └── test_crawly.py
|   └── test_graph_builder.py
|   └── test_utils.py
└── README.txt
│__.gitignore

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
Write:
Graph structure summary
Node rankings
Leaf, dead links
Dependency stats
Performance metrics

🧾 OUTPUT
Printed summary to console (optional)

Generated text file:
report/analysis_report.txt
Contains:
Total files visited
Dead links
Leaf nodes
Cycles detected
Top 10 largest and most traversed files
Dependency tree depth
Shortest path analysis
Complexity stats (DFS, BFS, memory, etc.)

📄 README.txt
====================================
Crawly - Recursive URL Graph Crawler
====================================

DESCRIPTION:
-------------
Given a root text file URL, Crawly recursively fetches all linked files to build and analyze a directed hyperlink graph. It detects cycles, leaf nodes, dead links, dependency depths, ranks files by size and visit frequency, and generates a comprehensive report.

FEATURES:
----------
- Detect cycles using DFS
- Find leaf nodes (files with no further links)
- Identify dead/unreachable links
- Rank files by:
  * Size
  * How frequently they're traversed
- Calculate dependency depth
- Compute shortest path from root to leaf using BFS
- Generate analytics:
  * Time and space complexity of traversal
  * Structure stats
  * Dependency analysis

DATA STRUCTURES USED:
----------------------
- Graphs (Adjacency List)
- Stacks, Queues
- Hash Maps
- Bitmasks (for visited tracking)
- Min/Max Heaps
- Dynamic Programming (memoization)
- Topological Sort

   --report <path> Specify custom output file
   --verbose       Enable detailed logs

OUTPUT:
--------
Generates:

- A text-based report in /report/analysis_report.txt

- Logs and runtime metrics

- Summary of:
   * Total nodes
   * Dead links
   * Leaf files
   * Cycles
   * Most linked files
   * File size ranks
   * Graph depth

DEPENDENCIES:
--------------
- requests
- tqdm
- heapq
- collections
All successfully crawled URLs.

Includes metadata like depth, size, time to fetch.

Dead Links Report

Unreachable, broken, or redirecting-to-dead pages.

Include HTTP status codes and error messages.

Redirect Map

Shows original URLs and their final redirected target (useful for Wikipedia disambiguation).

Unvisited Pages

Pages discovered via links but not visited due to depth limits or filtering.

Page Tree Hierarchy

Based on crawl depth, shows a tree structure from the root page.

Page Size Ranking

Already discussed — ranks pages by their byte size.

Link Popularity Ranking

Sort pages by in-degree (how many other pages link to them).

Graph Cycles Detected

Looping links (e.g., A links to B, B back to A).

Topological Sort of Pages

If treating links as dependencies.
---

## Features

- 🌐 **Recursive Wikipedia Link Exploration**  
  Start from any Wikipedia page and recursively follow internal links to construct a web graph.

- 🌳 **Tree Structure & Graph Generation**  
  Build both hierarchical and flat graph representations of the crawl.

- 📏 **Page Depth Metrics**  
  Track how deeply nested each page is relative to the starting point.

- 🚫 **Dead Link Detection**  
  Identify and report unreachable or broken URLs.

- 📊 **Graph Visualization Output**  
  Export `.dot` or `.json` files to visualize hyperlink relationships.

- 📁 **Configurable Depth & Strategy**  
  Choose between BFS or DFS with customizable crawl depth.

---

## Enhanced Algorithmic Toolkit

### Core Algorithms
- **DFS & BFS**: Primary traversal strategies for link exploration.
- **Backtracking**: Handles loops, redirects, and dead ends.
- **Dynamic Programming**: Cache results and memoize page data.
- **Greedy Algorithms**: Optimize link prioritization under constraints.
- **Topological Sort**: Analyze dependency order of linked articles.

### Fundamental Techniques
- **Algorithm Analysis**: Time and space complexity optimization.
- **Searching, Sorting & Recursion**: Efficiently manage and process URL lists.
- **Modified Binary Search**: For sorted link metadata or fast lookup.
- **Prefix Sum & Hashing**: Track depth, visit frequency, and reachability.
- **Two Pointers & Sliding Window**: Track sequences of similar/related pages.