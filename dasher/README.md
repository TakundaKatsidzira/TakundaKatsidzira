# 🚀 Dasher
# (OOP: Naming, Abstraction) The project is named and structured as a class/module, abstracting delivery simulation logic. Study: OOP basics, class/module design.

Dasher is a simulation of a delivery optimization system using **Directed Weighted Graphs**. It demonstrates how different **pathfinding strategies** and **algorithmic agents** (Random, Greedy, Dynamic Programming, Backtracking, and Bitmap DP) perform on a delivery map with real-time decision-making.
# (OOP: Abstraction, Polymorphism) Agents use a common interface but implement different strategies. Study: Abstract base classes, method overriding.
# (DSA: Graphs, Pathfinding) Uses directed weighted graphs and pathfinding algorithms. Study: Graph theory, Dijkstra's algorithm, TSP.

## 🧠 Core Concept

Dasher creates a **directed, weighted graph** with 10 nodes representing locations on a map. The graph must be **strongly connected**, meaning there is a path from every node to every other node. The project then simulates delivery orders, and multiple agents attempt to complete them in the most optimal way possible, based on their strategies.
# (DSA: Graph Connectivity) Ensures strong connectivity using algorithms like Kosaraju's. Study: Strongly connected components, graph traversal.
# (OOP: Encapsulation) Graph and agent logic are encapsulated in their own classes. Study: Encapsulation, modularity.

---

## 📦 Features

* Create a strongly connected **directed weighted graph**
  # (DSA: Graph Construction) Builds a graph with edge weights and strong connectivity. Study: Graph data structures, connectivity algorithms.
* Generate 10 delivery orders with unique pickup and dropoff points
  # (DSA: Random Sampling, Uniqueness) Ensures orders are unique. Study: Random sampling, set operations.
* Initialize all agents at the same random start location
  # (OOP: Initialization) Agents share a common starting state. Study: Object initialization, shared state.
* Simulate order execution for:
  # (OOP: Polymorphism) Each agent executes orders using its own strategy. Study: Method overriding, polymorphism.

  * 🔄 Random Agent
    # (OOP: Inheritance) Inherits from base agent, overrides order selection. Study: Subclassing, randomization.
  * ⚡ Greedy Agent
    # (OOP: Inheritance) Implements greedy selection logic. Study: Greedy algorithms, subclassing.
  * 🔍 Dynamic Programming + Backtracking Agent
    # (DSA: DP, Backtracking) Uses recursion and memoization for optimal order. Study: DP, recursion, memoization.
  * 🧮 Bitmap DP Agent
    # (DSA: Bitmasking, DP) Uses bitmask DP for TSP-like optimization. Study: Bitmasking, dynamic programming.
  * 🧪 Same-Order Agent (baseline)
    # (OOP: Baseline Implementation) Provides a simple, non-optimized reference. Study: Baseline comparison.

* Log:
  # (OOP: Encapsulation, Logging) Logging is handled by a dedicated module/class. Study: Logging patterns, separation of concerns.

  * The initial map
    # (DSA: Graph Serialization) Stores the graph structure for analysis. Study: Serialization, graph export.
  * Initial order list
    # (DSA: List, Metadata) Stores orders for reproducibility. Study: List data structures.
  * For each agent:
    # (OOP: Aggregation) Aggregates results per agent. Study: Data aggregation.

    * Sorted order list
      # (DSA: List, Sorting) Shows the order in which deliveries are executed. Study: Sorting algorithms.
    * Total distance traveled
      # (DSA: Path Cost Calculation) Sums edge weights for the agent's path. Study: Path cost, graph traversal.
    * Decision-making time
      # (DSA: Time Measurement) Measures agent computation time. Study: time module, performance profiling.

---

## 🧱 Project Structure

```bash
dasher/
│
├── agents/
│   ├── base_agent.py
│   ├── random_agent.py
│   ├── greedy_agent.py
│   ├── dp_agent.py
│   ├── bitmap_agent.py
│
├── graph/
│   ├── map_graph.py
│   └── utils.py
│
├── orders/
│   └── order_generator.py
│
├── main.py
├── README.md
└── requirements.txt
```
# (OOP: Modularity, Separation of Concerns) Each module handles a specific responsibility. Study: Modular design, project organization.

---

## ⚙️ Object-Oriented Design

### 📌 Class Responsibilities

* **Graph (`MapGraph`)**:
  # (OOP: Encapsulation) Encapsulates all graph logic. Study: Class design, encapsulation.

  * Handles node/edge creation
    # (DSA: Graph Construction) Adds nodes and edges. Study: Graph data structures.
  * Ensures strong connectivity
    # (DSA: Connectivity Algorithms) Uses algorithms to guarantee strong connectivity. Study: Kosaraju's algorithm.
  * Calculates shortest paths using Dijkstra's algorithm
    # (DSA: Shortest Path) Uses Dijkstra's for efficient routing. Study: Dijkstra's algorithm.

* **OrderManager**:
  # (OOP: Encapsulation) Manages order creation and storage. Study: Class responsibility.

  * Generates and stores pickup/dropoff order dictionaries
    # (DSA: Dictionary, List) Uses dicts/lists for order metadata. Study: Dict/list usage.

* **Agent (Abstract Base Class)**:
  # (OOP: Abstraction, Inheritance) Provides a common interface for all agents. Study: Abstract base classes, inheritance.

  * Contains shared logic for agents: navigating, logging, etc.
    # (OOP: Code Reuse) Shared logic avoids duplication. Study: DRY principle.
  * Each subclass implements its own `sort_orders` method
    # (OOP: Polymorphism) Subclasses override methods for custom behavior. Study: Method overriding.

### 🧠 Why OOP?

* **Encapsulation**: Keeps behavior and data together (e.g., Graph manages its own validation and shortest path logic)
  # (OOP: Encapsulation) Data and methods are bundled in classes. Study: Encapsulation, class attributes.
* **Polymorphism**: Each agent behaves differently but shares a common interface
  # (OOP: Polymorphism) Enables flexible agent strategies. Study: Polymorphism, interfaces.
* **Extensibility**: New agents/strategies can be added with minimal changes to existing code
  # (OOP: Extensibility) Design supports easy addition of new features. Study: Open/closed principle.

---

## 🛠 Data Structures and Algorithms

### 🔄 Graph Representation

* **Adjacency List** with edge weights: Efficient for sparse graphs
  # (DSA: Adjacency List) Stores graph efficiently. Study: Adjacency list, edge weights.
* **Dijkstra’s Algorithm**: Used to compute shortest paths between all pairs (preprocessed for fast lookup)
  # (DSA: Shortest Path, Preprocessing) Fast pathfinding using Dijkstra's. Study: Dijkstra's, all-pairs shortest path.
* **Strong Connectivity Check**:
  # (DSA: Connectivity, Kosaraju's Algorithm) Ensures all nodes are reachable. Study: Kosaraju's, graph traversal.

  * DFS forward and reverse using **Kosaraju’s Algorithm**
    # (DSA: DFS, Kosaraju's) Finds strongly connected components. Study: DFS, Kosaraju's steps.
  * Random edges are added until connectivity is guaranteed
    # (DSA: Randomization, Connectivity) Ensures strong connectivity. Study: Random edge addition.

### 📋 Order Management

* `orders = [{"start": node1, "end": node2}, ...]` where each node is a graph vertex
  # (DSA: List of Dicts) Stores orders as dictionaries in a list. Study: List/dict usage.
* Orders are unique and randomly generated
  # (DSA: Random Sampling, Set) Ensures uniqueness. Study: Random sampling, set operations.

---

## 🧠 Agent Strategies & Trade-Offs

### 🧪 Same-Order Agent (Baseline)

* Executes orders in given list order.
  # (OOP: Baseline Implementation) No optimization, just follows input. Study: Baseline comparison.
* **Complexity**: O(n)
  # (DSA: Complexity Analysis) Linear time. Study: Big O notation.
* **Pros**: Simple, no processing cost
* **Cons**: Likely inefficient in total distance

---

### 🔄 Random Agent

* Shuffles order list randomly.
  # (DSA: Randomization) Provides a stochastic baseline. Study: random.shuffle.
* **Complexity**: O(1) + O(n) for simulation
  # (DSA: Complexity Analysis) Constant for shuffle, linear for execution. Study: Complexity breakdown.
* **Trade-Off**: No optimization but provides a stochastic baseline

---

### ⚡ Greedy Agent

* Always picks the next closest available pickup.
  # (DSA: Greedy Algorithm) Chooses locally optimal next step. Study: Greedy heuristics.
* **Complexity**: O(n²)
  # (DSA: Complexity Analysis) Quadratic due to repeated nearest search. Study: Nested loops.
* **Pros**: Fast, low overhead
* **Cons**: Can get stuck in local minima

---

### 🔍 DP + Backtracking Agent

* Tries all order permutations via backtracking and caches sub-results with memoization.
  # (DSA: Backtracking, Memoization) Explores all possibilities, caches results. Study: Recursion, memoization.
* **Complexity**: O(n!), reduced by memoization
  # (DSA: Complexity Analysis) Factorial, but improved by DP. Study: Factorial growth, DP optimization.
* **Pros**: Near-optimal result for small n
* **Cons**: Exponential growth, only feasible for n ≤ 10

---

### 🧮 Bitmap DP Agent

* Uses bitmasking and DP to find the optimal order sequence (similar to TSP solution).
  # (DSA: Bitmask DP) Efficiently solves TSP-like problems. Study: Bitmasking, DP state compression.
* **Complexity**: O(n² \* 2^n)
  # (DSA: Complexity Analysis) Exponential but much faster than pure backtracking. Study: Bitmask DP complexity.
* **Pros**: Much faster than pure backtracking, optimal
* **Cons**: High memory usage, still exponential

---

## 🧪 Optimization Insights

* **Preprocessing all-pairs shortest paths** saves time during agent simulations.
  # (DSA: Preprocessing) Reduces repeated computation. Study: Floyd-Warshall, all-pairs shortest path.
* **Memoization and Bitmasking** in agents drastically improve performance.
  # (DSA: Memoization, Bitmasking) Speeds up repeated subproblems. Study: Memoization, bitmask tricks.
* **Trade-off** between CPU time (DP agents) and accuracy (Greedy agent).
  # (DSA: Trade-Off Analysis) Balances speed and optimality. Study: Algorithm trade-offs.
* Agents simulate order execution **dynamically**: after each dropoff, the agent continues from the last dropoff location.
  # (OOP: State Management) Agent state updates after each action. Study: Stateful simulation.

---

## 📤 Output Example

### 🔹 Initial Orders

```
[{'start': 2, 'end': 5}, {'start': 3, 'end': 8}, ..., {'start': 6, 'end': 0}]
```
# (DSA: List of Dicts) Example of order data structure. Study: List/dict formatting.

### 🔹 Agent Report (Greedy)

```
Sorted Orders:
[{'start': 3, 'end': 8}, {'start': 2, 'end': 5}, ...]

Total Distance Traveled: 87.3
Decision Time: 0.0042 seconds
```
# (DSA: Output Formatting, Logging) Shows agent results. Study: Output formatting, logging.

---

## ⏱ Performance Logging

| Agent           | Distance | Time (s) |
| --------------- | -------- | -------- |
| Same Order      | 124.5    | 0.0001   |
| Random          | 118.3    | 0.0003   |
| Greedy          | 87.3     | 0.0042   |
| DP Backtracking | 69.1     | 2.1351   |
| Bitmap DP       | 69.1     | 0.2123   |
# (DSA: Performance Measurement, Comparison) Enables benchmarking of agent strategies. Study: Performance profiling, comparative analysis.

---

## ✅ Requirements

* Python 3.8+
* `networkx`
* `numpy`
# (DSA: Library Usage) Uses libraries for graph and numeric operations. Study: networkx for graphs, numpy for arrays.

---

