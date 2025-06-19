# PYTHON PROGRAMMING CLASSES & OBJECTS

## 0. FUNCTIONAL TOOLS 

* Python supports the functional programming paradigm for clean code. This avoids changing states of mutable data by creating new data, sacrificing space for readability.
* Functional programming is great for manipulation,tranforming and aggregating frequent data tasks.
* Most functions need list wrapper to access output but for calls and iterations just use laxy results to save space.

## lambda (Anonymous functions)

* A one-inline function with no name used for quick short taskslike sorting, mapping and transferals.
* Custom sort keys (e.g., sort a list of intervals by end time).
8 Sorting dictionaries by keys or list of tuples.
* intervals = [(1,4), (2,3), (1,5)]
* intervals.sort(key=lambda x: x[1])
* sorted_dict = sorted(dict, key=lambda keys: keys[values])
* squares_sum = lamda x, y : (x ** 2) + (y ** 2)

## sorted(iterable, key=None, reverse=False)

* return a new iterable from the input sorted as needed.* Returns a new sorted list from any iterable.
* Supports, descending order with reverse=True argument and  custom sorts with lamda.
* great for sorting ntervals and greedy tasks and stable preserving original order of equal elements.
* intervals = [(1,4), (2,3), (1,5)]
* intervals.sort(key=lambda x: x[1])


## enumerate(iterable, start=0)

* Keeps a index, counter lazily while iterating.
* Useful when both the data and index are valuable in a loop, like sliding windows.
* Substitutes for i in range(len) with for i, item in enumerate(iterable).

## map(function, iterable)

* Applies its function argument to an iterables items.
* Returns a lazy map object (wrap with list() if needed).
* Useful for mathematical operations on array elements , preprocessing and encoding strings to numbers.
* words = ["name ", " job ", "house"]
* info = list(map(lamda s: s.strip().title(), words)) 
* Custom function on words
* squares = list(map(lambda x: my_func(x), words))

## filter(function, iterable)

* Filters out elements in an iterable by a function if funtion return false for element.
* Also returns lazily so wrap with list.
* Useful to remove unwanted nodes or elements.
* nums = [1, 2, 3, 4, 5]
* evens = list(filter(lambda x : x % 2 ==0, nums))

## reduce(function, iterable)

* Reduces iterable to single value by cumulatively applying function to elements like sum().
* Must import functools, and very useful to aggregate results like sums and products even finfing largest common facto with gcd from math module.
* Useful when mrging intervals.
* Generate full path of file after import os.
* path = [home, documents, textbooks, atomic habits.pdf]
* full_path = reduce(os.path.join, path)

## zip(iterable1, iterable2, ...)

* Builds tuples from two or more iterables by elements at matching positions.
* Lazy returns so wrap with list if not iterating or making a simple call.
* stops at shortest len of inputs.
* a = [1, 2, 3]
* b = [4, 2, 6]
* if any(x == y) in (zip(a, b)):
*    return False # matching elements

# 1. COMPREHENSIONS (Declarative Data Creation)

* Build new lists dictionaries and sets with concise readable logic.

## List Comprehension

* Pattern: [expression for item in iterable if condition].
* Building filtered arrays by squares primes in a single pass.
* nums = [1, 2, 3, 4, 5]
* odd_squares = [x**2 for x in nums if x % 2 != 0]

## Dict Comprehension

* Pattern: {key_expression : value_expression for item in iterable if condition}.
* Build hashmaps by filtering lists and matching keys to values.
* Build adjacency lists or memoization tables.
* Frequency map brute force.
* arr = [1,2,2,3,4,1,5,2,6,4,7,8]
* counter = {x : arr.count(x) for x in arr if x % 2 == 0}

## Set Comprehension

* Pattern: {expression for item in iterable if condition}.
* removing duplicates and testing membership.
* nums = [1, 2, 2, 3, 4]
* evens = {x for x in nums if x % 2 == 0}  # {2, 4}

## Generators 

* Pattern: (expression for item in iterable if condition)
* List comprehension like statement to lazily yield results one by one.
* nums = [1, 2, 3, 4, 5, 6]
* evens_squared = (x * x for x in nums if x % 2 == 0)
* list(evens_squared)  # [4, 16, 36]

#  2. itertools (Efficient Iterators & Combinatorics)

* from itertools import product, permutations, combinations, groupby.
* Memory efficiant, lazy tools for processing products, permuations, combinations and grouping.finite sequences, and grouping.

## product()

* Produces a cartesian product on inputs, with repeats allowed with len specified by repeat argument.
* All possible arrangements where you pick one element from each input for each element.
* Brute-force search in grid/parameter space like with nested loops.
* from itertools import product
* for p in product([0, 1], repeat=3): 
*    print(p)
* (0, 0, 0)
* (0, 0, 1)
* (0, 1, 0)
* ...
* (1, 1, 1)

## permutations()

* All order-sensitive arrangements of given length with no repetitioms.
* Solve permutation backtracking problems.
* list(permutations([1, 2, 3], 2))
* [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

## combinations()

* All order-insensitive subsets of a given length, with no repetition.
* Selecting groups from items.
* list(combinations([1, 2, 3, 4], 2)) 
* [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

###  groupby()

* Groups items next to each other by key fuction and returns key and group as iterable.
* Must sort for unsorted lists
* Cluster similar elements (frequency compression).
* data = [1,1,2,2,2,3,3,1]
* for key, group in groupby(data):
*   print(key, list(group))
* 1 [1, 1]
* 2 [2, 2, 2]
* 3 [3, 3]
* 1 [1]


#  3. DSA-RELEVANT MODULES

##  `collections` (Extended Data Structures)

* `Counter`
* Subclass of `dict` for counting hashable objects.
* Automatically initializes counts to 0.
* Frequency maps (most common elements, sliding window).
* Histogram buckets for sorting/counting sort.

## `defaultdict`

* Like `dict`, but provides a default value for missing keys via a factory (e.g., `int`, `list`).
* Automatically create adjacency lists (for graphs).
* Avoid KeyErrors in DP tables or recursion.

## `deque`

* Double-ended queue supporting fast appends/pops from both ends.
* Better performance than `list` for queue/stack behavior.
* Breadth-first search (queue).
* Sliding window problems (monotonic queue).
* Efficient reversal or trimming.

##  `heapq` (Priority Queue via Binary Heap)

* Min-Heap (default behavior)
* Supports log-time insertion and deletion of the smallest element.
* Can emulate a max-heap using negative values.
* Dijkstra’s shortest path algorithm.
* Merging sorted lists/streams.
* Finding top-k largest/smallest items efficiently.

## `bisect` (Binary Search Helpers)

* Works on sorted lists to find insertion points using binary search.
* `bisect_left`, `bisect_right`
* Return index where element should go to maintain sorted order.
* Left includes the position if equal; right skips over duplicates.

## `insort()`

* Inserts value into correct position in sorted list (maintains order).
* Efficient rank queries.
* Range queries (prefix sums, counts).
* Keeping a sorted list during iteration (e.g., sliding window median).