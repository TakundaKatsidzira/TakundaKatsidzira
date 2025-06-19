#  Data Structures.

# 0. Array / List

* The main idea is a contiguous block of memory. Size varies on whether its fixed or dynamic. Python uses dynamic arrys by leaving space for them to grow as needed.
* Elements are stored at indexes.
* Purpose: Store elements in order, allow quick index-based access.
* Space Complexity is the number of elements and time complexity is contant for access, linear for insert and delete except for edge cases at each end and lists.
* Useful when the number of elements is known and small and use case requires fast random access while order matters.
* Offer great cache locality and minimal overhead.
* Common methods include, append(), insert(), remove(), delete [], index(), count(), sort(), reverse(), len(), sum(), min(), max(), sorted().
* Supports slicing and list comprehensions. 

# 1. HashMap / HashSet

* The main idea is to use a hash function to map keys to indices in an underlying array.
* This offers efficeint key based access and existence checks.
* Space complexity is linear, time complexity is constant for insertions deletions look ups, worst case not common is linear time with all collisions.
* Useful for existence checkc frequency maps and caching.
* Common methods include hash(), set(), get(), pop(), del [], keys(), values(), items(), and clear().
* Collections library also supports Counters and built in support for dictionary comprehensions.

# 2. Stacks

* The main idea is elements last added are first removed by the LIFO principle.
* Space complexity is linear while time complexity is constant for fundamental operations.
* Implemented using lists in python.
* Common methods includ push(), pop(), peek(), and isempty(). these are implemented using append() pop() slicing and len().
* Useful when reversing data and operations such as in recursions and used in graph traversals like DFS.

# 3. Queue / Deque

* The main idea is elements first added are first removed following the FIFO principle:
* Space complexity is linear and time complexity is dependant on implementation but constant for most fundamental operations as implemented commonly with a linked list.* Deques are double ended queuess allowing for both stack and queue behavior supported by collection.deque. 
* Common methods include append(), appendleft(), pop(), popleft(), clear(), len(), isempty() and peek and peekleft using 0 and negative indexing. 
* Can limit size with maxLen argument, and use rotate() to shift elements cyclicly. 
* Useful for task scheduling, graph  traversal with BFS and sliding window problems.
* Enforces fairness or temporal ordering.

# 4. Linked List

* The main idea is using node classes that hold data with pointers directing you to the next and previous elements dpending on implemetation.
* Supports insertions and deletions without needing resizing or shifting.
* Space complexity is linear for both singly and doubly linked lists with linear time for look ups.
* Option for a tail and head pointer for faster operations at each end.
* Traversals while next pointer not None from head.
##  Singly Linked Lists
    * Only supports next pointer, time complexity constant for insertions and deletions at tail and end but linear for middle elements.
## Doubly Linked Lists
    * Supports next and prev pointers, time complexity constant for insertions and deletions at all indexes.
* Insert at head in singly by creating new node and setting next to head then  head to new node.
* In doubly create new node and set next to head and head prev to new node. Set new node prev to  None. Have pointer to tail
* Insert at end in singly by traversing to tail setting tail next to new node with next set to none.
* In doubly create new node, set tail next to new node and new node prev to tail, new node next is None and tail pointer points to new node. 
* Insert at index i in singly by traversing to i-1th, set new nodes next to 1-th next and i-1th next  to new node.
* Insert at index i in doubly by traversing to ith, set its prev to and new node next to ith, new nodes prev is i-1th and i-1th next is new node.
* Delete at head by setting head pointer to current heads next. Garbage collector handles memory.
* Delete at tail by setting tail pointer to current tail pointers prev in doubly or traversing to last - 1 in singly and setting its next to None.
* Delete at index i in singly by traversing to i-1th and setting its next to its next's next.
* Delete at index i in doubly by traversing to ith and setting its prev's next to its next and its next's prev to its prev.  
* Useful when operations include many insertions and deletions and random access is not needed.


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

# 7. Graph (Adjacency List / Matrix)

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

