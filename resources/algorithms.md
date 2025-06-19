# 📈 Common Algorithms / Patterns (Expanded)

# 0. Two Pointers

* Main Idea: Use two indices to iterate from different ends or parts of a collection.

* Use When:
  * Working with **sorted arrays** (e.g., pair sum to target)
  * **Removing duplicates** (e.g., in-place operations)
  * **Palindrome checking**
  * **Partitioning** or **merging**

* Why It Helps:
  * Reduces O(n²) to O(n)
  * Elegant for linear scans without extra space

* Common Problems:
  * 2-sum (sorted), container with most water, remove duplicates
* Edge Notes: Works best when order or sorting is guaranteed.

# 1. Sliding Window

* Main Idea: Use a fixed or dynamic-size window to scan part of an array/string.

* Use When:
  * Subarray problems (max sum, average, etc.)
  * String pattern matching (longest substring with k distinct chars)
  * Continuous metrics over sequences

* Why It Helps:
  * Avoids recalculating values repeatedly
  * Achieves O(n) for what may seem like O(n²)

* Common Problems:
  * Longest substring without repeating characters, max sum subarray

* Edge Notes: Know when to shrink/grow the window — often uses a hashmap or set.

# 2. Binary Search

* Main Idea: Halve the search space each time

* Use When:
  * Sorted arrays
  * Finding boundaries (first/last occurrence)
  * Min/max value search in a monotonic space

* Why It Helps:
  * O(log n) search, efficient even on large datasets

* Common Problems:
  * Search in rotated array, find k-th element, binary search on answer

* Edge Notes: Can be adapted for decimals, ranges, function results, or “binary search the answer.”

# 3. Depth-First Search (DFS)

* Main Idea: Recursively explore as deep as possible before backtracking

* Use When:
  * Explore all paths, like maze solving
  * Tree traversal, permutation generation
  * Graph connectivity (e.g., islands, components)

* Why It Helps:
  * Naturally fits recursive solutions
  * Efficient for problems with deep, narrow search trees

* Common Problems:
  * Generate combinations, detect cycles, clone graphs

* Edge Notes: Watch for infinite loops in graphs — track visited nodes!

# 4. Breadth-First Search (BFS)

* Main Idea: Explore neighbors level-by-level using a queue

* Use When:
  * Finding the shortest path in unweighted graphs
  * Multi-source spread (e.g., infection, fire)

* Why It Helps:
  * Guarantees shortest path
  * Systematic, layer-wise traversal

* Common Problems:
  * Word ladder, shortest path in grid, minimum moves

* Edge Notes: Use a queue; can combine with visited sets or levels.

# 5. Backtracking

* Main Idea: Try all possibilities, backtrack when a choice leads to dead end

* Use When:
  * Generate all solutions (combinations, permutations)
  * Constraint problems (Sudoku, N-Queens)

* Why It Helps:
  * Prunes invalid paths early
  * Solves hard combinatorial problems neatly

* Common Problems:
  * Subsets, word search, valid parentheses

* Edge Notes: Optimize with pruning and early exits; exponential in worst-case.

# 6. Dynamic Programming (DP)

* Main Idea: Break problems into overlapping subproblems with optimal substructure

* Use When:
  * Problems with repeating subproblems
  * Resource allocation, counting, string similarity

* Why It Helps:
  * Converts exponential recursion into polynomial time
  * Tabulation/memoization reduce redundant work

* Common Problems
  * Fibonacci, knapsack, longest common subsequence, edit distance

* Edge Notes: Think in terms of state — e.g., `dp[i][j]` — and transitions.

# 7. Greedy

* Main Idea: Always take the best immediate (local) option

* Use When:
  * Problem allows greedy choice property
  * Interval covering, scheduling, optimization

* Why It Helps:
  * Very fast (often linear or log-linear)
  * Simple, avoids DP’s overhead when applicable

* Common Problems:
  * Activity selection, jump game, Huffman coding, coin change (special case)

* Edge Notes: Greedy doesn’t always guarantee global optimum — prove correctness!

# 8. Intervals (Merge & Overlapping)

* Main Idea: Sort intervals and process them linearly to detect or combine overlaps

* Use When:
* Merging overlapping intervals
* Inserting a new interval into an existing list
* Checking for any overlaps (e.g., meeting conflicts)
* Finding free time between intervals
* Minimizing overlaps (e.g., scheduling without conflicts)

* Why It Helps:
* Sorting by start time simplifies comparison
* Enables a linear O(n) sweep after O(n log n) sort
* Replaces brute-force comparisons with elegant logic

* Common Problems:
* Merge Intervals (LC 56)
* Insert Interval (LC 57)
* Non-overlapping Intervals (LC 435)
* Meeting Rooms I & II (LC 252, 253)

* Edge Notes :
* Use a min-heap when tracking ongoing intervals (e.g., for counting rooms).
* Always sort intervals by start time before processing.
* Merge condition: `if curr_start <= prev_end → merge`.


# 9. Bit Manipulation

* Main Idea: Use binary representations to optimize operations

* Use When:
  * Subset generation (e.g., 2^n states)
  * Flag combinations, parity checks, math tricks

* Why It Helps:
  * Memory and performance efficient
  * Bitwise ops are O(1)

* Common Problems:
  * Single number (XOR), subset sum with bitmask DP, power of 2

* Edge Notes: Useful for up to \~20 elements (2^20 is \~1 million).

