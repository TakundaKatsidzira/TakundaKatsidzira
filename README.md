TAKUNDA KATSIDZIRA 
CODE 

GOALS
  Learn Python
  Learn OOP and Data Structures and Algorithms
  Complete Project

COURSES
  CS50P
  CS50AI

BOOKS
  Automate The Boring Stuff With Python
  Beyond The Basic Stuff In Python

DATA STRUCTURES AND ALGORITHMS
  Algorithm Analysis
  Arrays and Hashing
  Stacks and Queues
  Linked Lists
  Searching, Sorting and Recursion
  Two Pointers, Fast and Slow Pointers and Sliding Window
  Merge Intervals
  Cyclic Sort
  Subsets
  Modified Binary Search
  Prefix Sum
  Monotonic Stack
  In Place Reversal Of Linked List
  
  Trees and Tries
  Heaps
  Graphs
  Breadth and Depth First Search
  Two Heaps
  Top K Elements
  K way Merge
  Backtracking
  Dynamic Programming
  Greedy Algorithms
  Topological Sort
  Matrix Traversal
  
  Bit Manipulation
  BITWISE XOR

LEETCODE
  Blind 75
  Neetcode 150


PROJECT
    DASHER
    
  Dasher is a dynamic, graph-based delivery simulation game where a Dasher navigates a city to accept, pick up, and deliver orders while optimizing for       
  distance, time, and profit. The game introduces real-time decision-making under changing road and traffic conditions, with a limited unit budget determining 
  game over. A Simulator entity spawns orders and controls road closures and traffic behavior, creating a constantly shifting challenge.
    
  Core Features:
    
    A. Dasher Agent
      •	Accepts, cancels (before pickup), picks up, and delivers orders.
      •	Tracks limited unit budget:
      •	Distance: 1 unit per edge traveled.
      •	Time inefficiency: 1 unit per node above optimal path.
      •	Supports multi-order batching:
      •	Can hold multiple active orders.
      •	Chooses pickup/dropoff sequencing for maximum efficiency.
      •	Challenges:
      •	Strategic tradeoffs: cancel a current order for a better one?
      •	Balance short, quick orders vs. long, high-paying ones.
      •	Batch route optimization becomes complex as active orders grow.
      
    B. Road Network
      •	Implemented as a weighted graph (nodes and edges).
      •	Each edge has:
      •	Distance cost (fixed).
      •	Time weight (can change dynamically).
      •	Supports closed roads:
      •	Simulator can open/close edges at any time.
      •	Forces dasher to re-route and adapt on the fly.
      •	Challenges:
      •	Real-time pathfinding under constraints.
      •	Efficient rerouting when road conditions shift mid-delivery.
      
    C. Order System
      •	Orders have pickup/dropoff nodes, variable payouts.
      •	Orders spawn dynamically during gameplay (even mid-delivery).
      •	Orders may expire or penalize for lateness.
      •	Penalty/cancellation rules:
      •	Orders can be canceled before pickup at a cost.
      •	Cannot cancel after pickup.
      •	Challenges:
      •	Managing order expiration or deadlines under limited budget.
      •	Identifying “trap” orders: good payout but high hidden costs.
      •	Prioritizing high-value orders that align with current path or batch.
      
    D. Simulator
      •	Drives time loop and game world.
      •	Dynamically changes traffic weights (edge time costs) based on:
      •	Time of day (e.g., rush hour).
      •	Simulated events like weather or blockages.
      •	Opens and closes roads mid-game to force strategic adaptation.
      •	Spawns orders with random or strategic timing and difficulty.
  
