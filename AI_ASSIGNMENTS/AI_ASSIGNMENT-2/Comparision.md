# Best First Search vs A* Search

## Best First Search (Greedy)
- Uses only a **heuristic function** `h(n)` (e.g., Euclidean or Manhattan distance to the goal).  
- Always expands the node that appears closest to the goal.  
- **Advantages:**  
  - Faster and simpler (less computation).  
  - Often finds a path quickly.  
- **Disadvantages:**  
  - Does **not guarantee the shortest path**.  
  - Can get stuck in detours if the heuristic misleads the search.  

---

## A* Search
- Uses both the **path cost so far** `g(n)` and the **heuristic estimate** `h(n)`.  
- Expands the node with the lowest total score: `f(n) = g(n) + h(n)`.  
- **Advantages:**  
  - Always finds the **shortest path** if the heuristic is admissible.  
  - More reliable for pathfinding problems.  
- **Disadvantages:**  
  - More computation and memory usage compared to Greedy Best First Search.  

---

##  Key Difference
- **Best First Search** is greedy and fast but **not optimal**.  
- **A\*** is slightly slower but **guarantees optimality**.  
