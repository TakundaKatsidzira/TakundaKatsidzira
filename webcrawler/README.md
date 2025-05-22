✅ PROJECT OVERVIEW
# (OOP: Documentation, Abstraction) Start with a clear overview to abstract the system's purpose and guide modular design. Study: Writing docstrings, module-level comments.

Project Name: Crawly
# (OOP: Naming, Modularity) Use meaningful names for classes, modules, and files to support modularity and maintainability. Study: Naming conventions, modular project structure.

Purpose: Recursively traverse a directed acyclic graph (DAG) of text files linked by URLs, analyze structure, detect cycles, find leaf and dead nodes, compute dependency depth, and rank files by traversal count and size.
# (DSA: Graphs, Recursion, DAGs) Represent the file/link structure as an adjacency list (dict of lists). Use recursion for traversal and DAG properties for dependency analysis. Study: Graph data structures, recursion, DAG algorithms.
# (OOP: Encapsulation) Encapsulate traversal, analysis, and ranking logic in separate classes/modules for clarity and reusability. Study: Class design, separation of concerns.

Features:
# (OOP: Feature Modularity) Implement each feature as a method or class for better organization, testing, and extensibility. Study: Single Responsibility Principle, modular design.

DFS & BFS for traversal
# (DSA: DFS, BFS) Implement both depth-first and breadth-first search for flexible graph traversal. Use a stack for DFS and a queue for BFS. Study: Stack/queue usage, iterative vs recursive traversal.
# (OOP: Strategy Pattern) Use the strategy pattern to allow switching between traversal methods at runtime. Study: Design patterns for interchangeable algorithms.

Cycle and dead link detection
# (DSA: Cycle Detection, Error Handling) Use visited sets and recursion stacks for cycle detection; handle HTTP errors for dead links. Study: Cycle detection algorithms, exception handling.
# (OOP: Encapsulation) Place detection logic in an Analyzer class to keep code modular and testable. Study: Encapsulation, modular error handling.

Leaf node identification
# (DSA: Degree Calculation) Identify nodes with no outgoing edges by checking adjacency lists. Study: Out-degree calculation, graph traversal.
# (OOP: Utility Methods) Implement as a utility method in the analyzer class for reuse. Study: Utility/helper functions.

Dependency and depth analysis
# (DSA: Topological Sort, BFS) Use topological sort for dependency order and BFS for depth calculation. Study: Kahn's algorithm, level-order traversal.
# (OOP: Reusability) Reuse traversal logic for multiple analyses to avoid code duplication. Study: Code reuse, DRY principle.

File ranking
# (DSA: Heap, Sorting) Use heaps for top-K ranking and sorting for full ranking. Study: heapq module, sorting algorithms.
# (OOP: Aggregation) Aggregate ranking logic in a dedicated class or method for clarity. Study: Aggregation patterns.

Complexity analytics and statistics
# (DSA: Time/Space Complexity) Track and log time/memory usage during traversal using profiling tools. Study: Profiling, complexity analysis.
# (OOP: Logging, Monitoring) Encapsulate analytics in a logger or monitor class to keep concerns separated. Study: Logging best practices, monitoring patterns.

Report generation
# (OOP: Separation of Concerns) Separate report formatting and output from core logic by using a ReportGenerator class. Study: Report generator classes, template methods.
# (DSA: File I/O, Serialization) Efficiently write structured data to files for analysis and sharing. Study: File operations, serialization formats.

📁 PROJECT STRUCTURE
# (OOP: Modularity, Separation of Concerns) Organize code into folders by responsibility (src, data, scripts, tests) for maintainability. Study: Project organization, modularity.

crawly/
│                    
├── src/
│   ├── __init__.py
│   ├── crawly.py  # Main execution script
│   ├── graph_builder.py        # Build the graph from root URL
│   ├── analyzer.py             # Perform analysis (DFS, cycle detect, etc.)
│   ├── utils.py                # Helper functions (e.g., fetch URL)
│   └── report_generator.py     # Generate and format report
│
├── data/
│   └── cache/ # Stores fetched and parsed files locally
|   └── analysis_report.txt   # Output report               
├── scripts/
│   └── run.sh scpt to run program 
|   └── test.sh scrpt to run tests on all modules using pytest -v
|   └── clean.sh scrpt to delete all pycache              
├── tests/
│   └── test_crawly.py
|   └── test_graph_builder.py
|   └── test_utils.py
└── README.txt                  # Project overview and usage

🧾 INPUT REQUIREMENTS
A text file URL (e.g., https://example.com/root.txt) as root input.
# (OOP: Input Validation) Encapsulate input validation and parsing in a dedicated function or class. Study: Input validation, error handling.

Each file contains plain text URLs, one per line.
# (DSA: File Parsing) Use line-by-line file reading for efficient parsing. Study: File I/O, parsing techniques.

Files may reference other files (forming a DAG or cycles).
# (DSA: Graph Construction) Build the adjacency list as you parse links. Study: Graph building, cycle detection.

--report report/analysis_report.txt
--verbose           # Print traversal logs
# (OOP: Command-Line Interface) Use argparse or click to encapsulate CLI logic. Study: CLI libraries, argument parsing.

🔁 INPUT SEQUENCE & LOGIC FLOW
Fetch Root URL
-> Parse contents into a list of links
# (OOP: Pipeline Design) Structure the process as a pipeline of encapsulated steps. Study: Pipeline patterns, modular workflow.

Build Graph (graph_builder.py)
-> Recursively fetch and parse linked files
-> Track visited URLs to avoid duplication
-> Store structure as adjacency list
# (DSA: Recursion, Hash Set) Use recursion and a set to avoid revisiting nodes. Study: Recursive traversal, set operations.

Analyze (analyzer.py)
# (OOP: Analyzer Class) Encapsulate all analysis logic in a dedicated class. Study: Analyzer pattern, modular analysis.

DFS to detect:
Cycles using visited set and recursion stack
Leaf nodes (nodes with no children)
Dead links (404s or invalid files)
# (DSA: DFS, Cycle Detection, Error Handling) Use DFS for traversal, recursion stack for cycle detection, and error handling for dead links. Study: DFS, cycle detection, exception handling.

BFS for shortest path to leaf
# (DSA: BFS, Shortest Path) Use BFS for shortest path calculations. Study: BFS, shortest path algorithms.

Topological Sort for dependency order
# (DSA: Topological Sort) Use Kahn's algorithm or DFS-based sort for dependency analysis. Study: Topological sorting.

Hashing and bitmasking for memoization and visit tracking
# (DSA: Hashing, Bitmasking, Memoization) Use hash maps and bitmasks to efficiently track visited nodes and cache results. Study: Hashing, bitmasking, memoization.

Top-K Heap for ranking files by size or visit frequency
# (DSA: Heap, Top-K) Use a min-heap for efficient top-K queries. Study: heapq, top-K algorithms.

Log Time/Space Complexity
Count nodes, edges, recursion depth, memory usage, etc.
# (DSA: Profiling, Complexity Analysis) Use profiling tools and counters to track resource usage. Study: Profiling, complexity metrics.

Generate Report
Write:
Graph structure summary
Node rankings
Leaf, dead links
Dependency stats
Performance metrics
# (OOP: ReportGenerator Class) Encapsulate all report logic in a dedicated class for maintainability. Study: Report generation, formatting.

🧾 OUTPUT
Printed summary to console (optional)
# (OOP: Output Abstraction) Abstract output logic to support both console and file output. Study: Output abstraction, interface design.

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
# (OOP: Structured Output, DSA: Aggregation) Aggregate and format results for reporting. Study: Data aggregation, output formatting.

📄 README.txt
====================================
Crawly - Recursive URL Graph Crawler
====================================

DESCRIPTION:
-------------
Given a root text file URL, Crawly recursively fetches all linked files to build and analyze a directed hyperlink graph. It detects cycles, leaf nodes, dead links, dependency depths, ranks files by size and visit frequency, and generates a comprehensive report.
# (OOP: High-Level Abstraction) Summarize the system's high-level responsibilities. Study: Abstraction, system design.

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
# (OOP: Feature Encapsulation) Each feature should be encapsulated in its own method or class for clarity and reuse. Study: Encapsulation, modularity.

DATA STRUCTURES USED:
----------------------
- Graphs (Adjacency List)
- Stacks, Queues
- Hash Maps
- Bitmasks (for visited tracking)
- Min/Max Heaps
- Dynamic Programming (memoization)
- Topological Sort
# (DSA: Data Structure Selection) Choose the most efficient data structure for each task to optimize performance and code clarity. Study: Data structure trade-offs, algorithm selection.

   --report <path> Specify custom output file
   --verbose       Enable detailed logs
# (OOP: Configurability) Use configuration options to make the tool flexible and user-friendly. Study: Configurable software design.

OUTPUT:
--------
Generates:
# (OOP: Encapsulation, Separation of Concerns) Output generation is encapsulated in a report module/class, keeping reporting logic separate from crawling/analysis. Study: Encapsulation, modular design.

- A text-based report in /report/analysis_report.txt
  # (DSA: File I/O, Serialization) Writes structured data to a file for later review. Study: File operations, serialization formats.

- Logs and runtime metrics
  # (DSA: Logging, Time/Space Complexity) Captures logs and performance metrics during execution. Study: Logging patterns, performance profiling.

- Summary of:
   * Total nodes
     # (DSA: Graph Traversal, Counting) Counts all nodes in the graph. Study: Graph traversal (BFS/DFS), counting algorithms.
   * Dead links
     # (DSA: Error Handling, Hash Map) Tracks unreachable nodes using error handling and hash maps for fast lookup. Study: Exception handling, dictionary usage.
   * Leaf files
     # (DSA: Graph Analysis, Degree Calculation) Identifies nodes with no outgoing edges (leaves). Study: Out-degree calculation, graph theory.
   * Cycles
     # (DSA: Cycle Detection, DFS) Detects cycles using DFS and recursion stack. Study: Cycle detection algorithms, DFS.
   * Most linked files
     # (DSA: In-degree, Sorting) Ranks nodes by in-degree (number of incoming links). Study: In-degree calculation, sorting.
   * File size ranks
     # (DSA: Sorting, Ranking) Sorts files by size for ranking. Study: Sorting algorithms, ranking techniques.
   * Graph depth
     # (DSA: BFS/DFS, Depth Calculation) Calculates the maximum depth of the graph using BFS or DFS. Study: Level-order traversal, recursion depth.

DEPENDENCIES:
--------------
- requests
  # (DSA: HTTP Requests) Used for fetching files over the web. Study: HTTP protocol, requests library.
- tqdm
  # (DSA: Progress Bar, Iteration) Provides progress bars for loops. Study: tqdm usage, iteration patterns.
- heapq
  # (DSA: Heap/Priority Queue) Used for efficient top-K ranking and priority queues. Study: Heap data structure, heapq module.

- collections
  # (DSA: Data Structures) Provides specialized containers like deque, Counter, defaultdict for efficient data handling. Study: collections module, advanced data structures.
