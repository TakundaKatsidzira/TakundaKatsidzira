# PROBLEM SOLVING STEPS

# 0. Understand the Problem

* Read the problem statement thoroughly.
* Don’t rush. Aim to fully grasp what is being asked before even thinking of code.

* Study the examples carefully.
* Use the provided examples to understand the desired input-output behavior. Try to generalize from them.

* Re-read the problem.
* After reviewing examples, go back and re-read the prompt. Often things make more sense on a second pass.

* Clarify ambiguities.
* Ask yourself:
  * What are the input types and ranges?
  * Are there edge cases (e.g., empty lists, negative numbers, very large inputs)?
  * What should happen in invalid or extreme scenarios?

* Highlight key constraints.
* Comment or mark things like time/space limits, input sizes, and unique rules.

# 1. Work Through Examples

* Simulate given examples cases manually.
* Step through them as if you were the machine, and observe how inputs are transformed into outputs.

* Create your own examples.
* Especially ones that test edge cases or unusual input structures.

* Draw diagrams or memory maps.
* Sketch how inputs are stored and manipulated. This is useful for visualizing pointers, recursion trees, hashmaps, etc.

* Look for repeated patterns.
* Take note of what parts repeat, grow, or change. This helps in identifying algorithmic approaches.

# 2. Start With a Naive (Brute Force) Solution**

* Formulate a basic approach first.
* Even if inefficient, this helps you understand the mechanics of solving the problem.

* Don’t prematurely optimize.
* Focus on correctness first. Understand what works before worrying about efficiency.

* Write down your thought process.
* Comment the logic in plain language or pseudocode. Think out loud in comments.


# 3. Explore Optimization Opportunities and Different Approaches

* Look for patterns or key data structures.
* Ask yourself:
  * Is this a common problem type (e.g., two pointers, sliding window, binary search)?
  * Can I use a hash set/map to speed things up?
  * Would recursion or dynamic programming help?

* Analyze time and space complexity.
* Evaluate your naive solution and try to reduce it step-by-step.

* Compare multiple approaches.
* Consider trade-offs (e.g., readability vs. performance).

# 4. Plan Your Implementation Clearly

* Write pseudocode or step-by-step logic.**
  Before writing code, outline:
  * What inputs the function receives
  * What outputs it should return
  * The core logic broken into steps

* Validate with your examples.
* Walk your pseudocode through the sample inputs again to make sure it aligns with the expected outputs.

# 5. Implement Your Solution Carefully

* Code from your plan.
* Use your pseudocode as a checklist for the actual implementation.

* Use clear and descriptive variable names.
* Avoid `x`, `y`, `z` unless you're dealing with coordinates , pointers or obvious values.

* Write helper functions if needed.
* Split large problems into smaller, testable units.

* Test as you go.
* Use print/debug statements or assertions to verify intermediate steps.

* Use all test cases, especially edge cases.
* Don’t stop at the example inputs; create ones that test size limits and boundary conditions.

# 6. Test and Refine

* Run all test cases, including edge and large inputs.

* Debug methodically.
* If a test fails:

  * Trace it step-by-step
  * Add logging or breakpoints
  * Use small tests to isolate logic errors

* Refactor if needed.
* Clean up code once it works. Make it more elegant or concise if possible without sacrificing readability.


# 7. Review, Reflect, and Reinforce

* If your solution is accepted:
  * Review your logic.
  * Ask: “Why does this work?” and “Why is it efficient?”
  * Could you have done it cleaner or faster?
  * Analyze it's complexity.

* Attempt other approaches.
  Think about:
  * How would a recursive version look?
  * Could this be done with a different data structure?

* Compare with others.
* Read top submissions or editorial solutions. Learn new patterns and Python tricks.
* Compare all complexities.

* Study unfamiliar concepts.
* If the problem involved something you don’t know well, bookmark it and study it separately.

# 8. When You’re Stuck

* If stuck for >15 minutes without a brute force idea, look up hints or solutions.**

* Don’t just read—understand.
* Pause at each step of the solution and try to reconstruct it yourself.

* Write it from scratch.
* After studying a solution, wait a few minutes, then try solving it from memory.

* Revisit later.
* If still unclear, flag the problem and revisit after a break or after solving similar problems.

# 9. Take Care of Yourself

* Don’t let frustration build.
* If you’re stuck or angry, step away—touch grass, hydrate, take a walk.

* Celebrate small wins.
* Even understanding the brute force approach or identifying the right data structure is a success.

* Be patient.
* LeetCode skills compound over time with deliberate practice.

# NOTES

# 🔧 Common Data Structures.

# 0. Array / List

* Main Idea: Contiguous block of memory with fixed or dynamically allocated size.

* Purpose: Store elements in order, allow quick index-based access.

* Time Complexity:
  * Access O(1)
  * Insert/Delete: O(n) (due to shifting)

* Use When:
  * Number of elements is known or small.
  * You need fast random access.
  * Order matters.

* Why It Helps:
  * Great cache locality → faster access in practice.
  * Minimal overhead compared to other data structures.

> Example: Accessing the 100th element in a sequence → Arrays give instant access.

# 1. HashMap / HashSet

* Main Idea: Uses a hash function to map keys to indices in an underlying array.

* Purpose: Efficient key-based access and fast existence checks.

* Time Complexity: Average O(1) for insert, delete, lookup (O(n) worst-case with collisions).

* Use When:
  * Checking if something has already been seen (e.g., detecting duplicates).
  * Counting frequencies (e.g., word counts).
  * Mapping unique keys to values (e.g., caching results).

* Why It Helps:
  * Avoids scanning arrays or lists — just jump directly to the right bucket.
  * Extremely efficient for membership tests (`in` operations).

> Example: Checking if a number has already appeared in a list → Use a `HashSet` to check in O(1) time instead of O(n).

# 2. Stack

* Main Idea: Elements are added and removed from the same end.

* Purpose: Model LIFO "recent-first" behaviors.

* Time Complexity: O(1) push and pop

* Use When:
  * Reversing data.
  * Backtracking (e.g., DFS, expression evaluation).

* Why It Helps:
  * Naturally matches recursive or nested logic.
  * Easy to implement with arrays or linked lists.

> Example: Validating balanced parentheses or navigating back in UI navigation.

# 3. Queue / Deque

* Main Idea:

  * Queue: FIFO — first added, first removed.

  * Deque: Double-ended — add/remove from both ends.

* Purpose: Maintain processing order or a sliding window of elements.

* Time Complexity: O(1) for enqueue/dequeue with a good implementation (like `collections.deque` in Python).

* Use When:
  * Task scheduling.
  * Breadth-first search (BFS).
  * Sliding window problems.

* Why It Helps:
  * Enforces fairness or temporal ordering.
  * Deques allow efficient additions/removals on both ends.

> Example: Print job queue, or finding the max in a sliding window of size k.

# 4. Linked List

* Main Idea: Nodes connected by pointers; each node holds data + next (and possibly previous) pointer.

* Purpose: Dynamic size without needing resizing or shifting.

* Time Complexity:
  * Insert/Delete at head/tail: O(1)
  * Access/Search: O(n)

* Use When:
  * You frequently add/remove items at the beginning or middle.
  * Random access is not needed.

* Why It Helps:
  * No need to shift elements like in arrays.
  * Useful in implementing stacks, queues, or undo functionality.

> Example: Browser history or undo stacks → Easy to add/remove recent actions.

# 5. Tree / Binary Search Tree (BST)

* Main Idea: Hierarchical structure; BST has left < root < right ordering.

* Purpose: Maintain sorted data with log-time insert, delete, and search.

* Time Complexity:
  * Balanced BST: O(log n)
  * Unbalanced (e.g., linked list): O(n)

* Use When:
  * Fast in-order traversal or range queries are needed.
  * Keeping data sorted dynamically (vs. sorting after-the-fact).

* Why It Helps:
  * Binary structure enables divide-and-conquer efficiency.
  * Self-balancing BSTs (AVL, Red-Black) avoid degenerating into lists.

> Example: Implementing ordered maps or sets.

# 6. Priority Queue / Heap

* Main Idea: Binary heap (min or max) to maintain priority ordering efficiently.

* Purpose: Always access and remove the element with the highest/lowest priority.

* Time Complexity:
  * Insert: O(log n)
  * Remove top: O(log n)

* Use When:
  * Dijkstra’s algorithm (shortest path).
  * Task scheduling (OS job queues).
  * Top-k elements.

* Why It Helps:
  * Avoids sorting the entire list repeatedly.
  * Always gives you the best candidate for next action.

> Example: Merging k sorted arrays using a heap of size k.

# 7. Trie (Prefix Tree)

* Main Idea: Tree structure where each node represents a character; paths represent words.

* Purpose: Efficiently store and search prefixes.

* Time Complexity: O(k) for search/insert (k = length of word)

* Use When:
  * Prefix searches (e.g., autocomplete).
  * Implementing dictionaries with fast retrieval.

* Why It Helps:
  * Avoids repeated comparisons by sharing common prefixes.
  * Faster than hash maps when working with prefixes or subsets.

> Example: Search engine suggestions or spell check.

# 8. Graph (Adjacency List / Matrix)

* Main Idea: Nodes (vertices) connected by edges (can be weighted, directed, etc.)

* Purpose: Model relationships, paths, and dependencies.

* Time Complexity:
  * Adjacency List: O(V + E)
  * Adjacency Matrix: O(V²), but faster access to edge presence.

* Use When:
  * Representing maps, networks, dependency chains.
  * Solving pathfinding, flow, or cycle detection problems.

* Why It Helps:
  * Enables powerful traversal algorithms (DFS, BFS, Dijkstra, etc.)
  * Encodes complex relationships naturally.

> Example: Google Maps, dependency resolution in build systems, or social networks.

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


# 8. Bit Manipulation

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

# 9. Intervals (Merge & Overlapping)

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

# 10. Union-Find / Disjoint Set

* Main Idea: Quickly manage group membership and connectivity

* Use When:
  * Cycle detection in undirected graphs
  * Connected components, Kruskal’s MST

* Why It Helps:
  * Very fast (near O(1)) with path compression and union by rank

* Common Problems:
  * Number of islands II, accounts merge, redundant connection

* Edge Notes: Requires parent/size arrays; be careful with path compression implementation.


# 11. Topological Sort / DAG Traversal

* Main Idea: Linear ordering of vertices such that for every edge (u → v), u comes before v

* Use When:
* Course scheduling / dependency resolution
* Any time you work with Directed Acyclic Graphs (DAGs)

* Why It Helps:
* Detects cycles
* Solves ordering constraints

* Common Problems:
* Course Schedule I & II (LC 207, 210)
* Alien Dictionary (LC 269)
* Task scheduling

* Edge Notes:
* Use DFS or Kahn’s algorithm (BFS with in-degree tracking). Cycles → no valid topo sort.