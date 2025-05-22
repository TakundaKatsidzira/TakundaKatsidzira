# WebCrawler
# (OOP: Naming, Abstraction) The project is organized as a class/module, abstracting crawling logic. Study: OOP basics, class/module design.

## Overview
**WebCrawler** is a recursive crawler tailored for Wikipedia pages. It explores internal links, maps the link structure, and analyzes metadata like page depth, dead links, and graph relationships. The crawler is powered by a suite of advanced algorithms and data structures, enabling efficient and scalable performance.
# (OOP: Encapsulation) Crawling, parsing, and analysis logic are encapsulated in classes/modules. Study: Encapsulation, modularity.
# (DSA: Recursion, Graphs, Trees) Uses recursion for crawling, graphs/trees for structure. Study: Recursive algorithms, graph/tree data structures.

Run with link to wikipedia pages as argument at command line. write to log file data off all checks
# (OOP: Abstraction, Encapsulation) The crawler abstracts command-line interaction and encapsulates logging logic. Study: Command-line interfaces, encapsulation of I/O.

---
Visited Pages List
# (DSA: List, Metadata Aggregation) Stores all successfully crawled URLs in a list, each with associated metadata. Study: List data structure, metadata collection.

All successfully crawled URLs.
# (DSA: List) Simple storage of URLs. Study: List basics.

Includes metadata like depth, size, time to fetch.
# (DSA: Metadata, Tuple/Dict) Each URL entry includes extra info, often stored as a tuple or dictionary. Study: Tuple/dict usage for metadata.

Dead Links Report
# (DSA: Error Handling, Hash Map) Tracks unreachable or broken links, often using a hash map for fast lookup. Study: Exception handling, dictionary for status.

Unreachable, broken, or redirecting-to-dead pages.
# (DSA: Error Handling) Identifies and logs failed requests. Study: Error/exception handling.

Include HTTP status codes and error messages.
# (DSA: Metadata, Logging) Stores status codes and errors for analysis. Study: Logging patterns, HTTP status codes.

Redirect Map
# (DSA: Hash Map) Maps original URLs to their redirected targets. Study: Dictionary mapping, redirect handling.

Shows original URLs and their final redirected target (useful for Wikipedia disambiguation).
# (DSA: Mapping) Useful for tracking disambiguation and canonical URLs. Study: Mapping relationships.

Unvisited Pages
# (DSA: Set, Filtering) Tracks discovered but unvisited pages, often using a set for uniqueness. Study: Set operations, filtering logic.

Pages discovered via links but not visited due to depth limits or filtering.
# (DSA: Filtering, Set) Filtering logic for crawl limits. Study: Filtering algorithms.

Page Tree Hierarchy
# (DSA: Tree) Represents crawl structure as a tree based on depth. Study: Tree data structures, parent-child relationships.

Based on crawl depth, shows a tree structure from the root page.
# (DSA: Tree Traversal) Visualizes crawl as a tree. Study: Tree traversal, visualization.

Page Size Ranking
# (DSA: Sorting, Ranking) Ranks pages by their byte size using sorting algorithms. Study: Sorting, ranking techniques.

Already discussed — ranks pages by their byte size.
# (DSA: Sorting) Applies sorting to metadata. Study: Sorting algorithms.

Link Popularity Ranking
# (DSA: In-degree, Graph Analysis) Sorts pages by how many other pages link to them (in-degree). Study: Graph in-degree, popularity metrics.

Sort pages by in-degree (how many other pages link to them).
# (DSA: Graph Metrics) Measures link popularity. Study: Graph theory.

Graph Cycles Detected
# (DSA: Cycle Detection, Graph) Identifies loops in the link graph. Study: Cycle detection algorithms, graph traversal.

Looping links (e.g., A links to B, B back to A).
# (DSA: Cycle Example) Illustrates a simple cycle. Study: Cycle examples.

Topological Sort of Pages
# (DSA: Topological Sort) Orders pages if treating links as dependencies (DAG). Study: Topological sorting, DAGs.

If treating links as dependencies.
# (DSA: DAG, Dependency Analysis) Applies to dependency graphs. Study: DAG properties, dependency resolution.
---

## Features

- 🌐 **Recursive Wikipedia Link Exploration**  
  Start from any Wikipedia page and recursively follow internal links to construct a web graph.
  # (DSA: Recursion, Graph Traversal) Recursively explores links using DFS/BFS. Study: Recursive functions, graph traversal.

- 🌳 **Tree Structure & Graph Generation**  
  Build both hierarchical and flat graph representations of the crawl.
  # (DSA: Trees, Graphs) Hierarchical (tree) and flat (graph) structures for representing links. Study: Tree vs graph, adjacency lists/matrices.

- 📏 **Page Depth Metrics**  
  Track how deeply nested each page is relative to the starting point.
  # (DSA: BFS/DFS, Depth Tracking) Uses traversal depth to annotate nodes. Study: BFS/DFS with depth, level-order traversal.

- 🚫 **Dead Link Detection**  
  Identify and report unreachable or broken URLs.
  # (DSA: Error Handling, Hash Map) Track failed requests and mark as dead links. Study: Exception handling, hash maps for status.

- 📊 **Graph Visualization Output**  
  Export `.dot` or `.json` files to visualize hyperlink relationships.
  # (DSA: Serialization, Graph Export) Serializes graph data for visualization. Study: JSON, DOT format, serialization.

- 📁 **Configurable Depth & Strategy**  
  Choose between BFS or DFS with customizable crawl depth.
  # (OOP: Strategy Pattern) Allows switching between BFS/DFS. Study: Strategy pattern, function pointers, configuration.

---

## Enhanced Algorithmic Toolkit

### Core Algorithms
- **DFS & BFS**: Primary traversal strategies for link exploration.
  # (DSA: DFS, BFS) Fundamental graph traversal algorithms. Study: Stack/queue-based traversal, recursion vs iteration.
- **Backtracking**: Handles loops, redirects, and dead ends.
  # (DSA: Backtracking) Retraces steps on failure/loops. Study: Recursive backtracking, visited sets.
- **Dynamic Programming**: Cache results and memoize page data.
  # (DSA: Memoization, DP) Avoids redundant work by caching results of previous computations. Study: Memoization techniques, dynamic programming patterns, cache invalidation.

- **Greedy Algorithms**: Optimize link prioritization under constraints.
  # (DSA: Greedy) Chooses the best local option at each step for efficiency, often used for prioritizing which links to crawl next. Study: Greedy algorithm design, optimal substructure, examples like Dijkstra's algorithm.

- **Topological Sort**: Analyze dependency order of linked articles.
  # (DSA: Topological Sort) Orders nodes in a directed acyclic graph (DAG) to respect dependencies, useful for understanding prerequisite relationships between pages. Study: Kahn's algorithm, DFS-based topological sort, DAG properties.

### Fundamental Techniques
- **Algorithm Analysis**: Time and space complexity optimization.
  # (DSA: Complexity Analysis) Evaluates the efficiency of algorithms in terms of time and space. Study: Big O notation, asymptotic analysis, profiling tools.

- **Searching, Sorting & Recursion**: Efficiently manage and process URL lists.
  # (DSA: Search, Sort, Recursion) Core techniques for handling and organizing data, such as finding links, ordering them, and using recursion for traversal. Study: Binary search, quicksort, merge sort, recursion basics.

- **Modified Binary Search**: For sorted link metadata or fast lookup.
  # (DSA: Binary Search) Enables fast lookup in sorted data structures, such as quickly finding a link or metadata entry. Study: Binary search variants, lower/upper bound search.

- **Prefix Sum & Hashing**: Track depth, visit frequency, and reachability.
  # (DSA: Prefix Sum, Hash Map) Prefix sums allow efficient range queries (e.g., number of visits in a range), while hash maps provide fast lookup for visited URLs and metadata. Study: Prefix sum arrays, hash functions, dictionary usage.

- **Two Pointers & Sliding Window**: Track sequences of similar/related pages.
  # (DSA: Two Pointers, Sliding Window) Efficiently process and analyze sequences or subarrays, such as finding the longest chain of related pages. Study: Windowed algorithms, pointer manipulation, sequence analysis.

