# ✅ **DAA PRACTICALS – COMPLETE VIVA MATERIAL (Option B Format)**

---

# **DAA Practical 1 — Fibonacci (Recursive & Non-Recursive) + Complexity**

## **Aim**

To implement Fibonacci using recursive and non-recursive methods and analyze time & space complexity.

---

## **Concept**

The Fibonacci sequence:
F(n) = F(n−1) + F(n−2), with F(0)=0, F(1)=1.

Two implementations:

### **1. Recursive Fibonacci**

Directly calls the formula recursively.
**Very slow** due to repeated subproblems.

### **2. Iterative Fibonacci**

Uses a loop and stores previous two values.
**Very fast** and memory efficient.

---

## **Time & Space Complexity**

| Method    | Time Complexity         | Space Complexity        |
| --------- | ----------------------- | ----------------------- |
| Recursive | **O(2ⁿ)** (exponential) | **O(n)** (stack frames) |
| Iterative | **O(n)**                | **O(1)**                |

Recursive version explodes due to repeated calculations.
Iterative version is optimal.

---

## **Viva Questions**

**Q1. Why is recursive Fibonacci slow?**
Because it recomputes the same values repeatedly → exponential time.

**Q2. How does iterative Fibonacci improve performance?**
It computes each Fibonacci number once → linear time.

**Q3. What is tail recursion?**
A recursion where the recursive call is the last statement. (Fibonacci is not tail recursive.)

**Q4. Which version uses more stack memory?**
Recursive.

**Q5. What real-life uses does Fibonacci have?**
Dynamic programming, financial predictions, nature patterns, trees/graphs.

---

---

# **DAA Practical 2 — Huffman Encoding (Greedy Algorithm)**

## **Aim**

To compress text using Huffman coding, which is based on greedy selection of minimum-frequency characters.

---

## **Concept**

Huffman encoding assigns:

* **Shorter codes → frequent characters**
* **Longer codes → rare characters**

Steps:

1. Count character frequencies
2. Build a min-heap
3. Repeatedly merge the two smallest nodes
4. Generate binary codes by traversing the tree

---

## **Why Greedy?**

At each step, it picks the two characters with the smallest frequency.

This ensures optimal prefix-free compression.

---

## **Complexity**

Building heap + tree:

**O(n log n)**

Encoding text:
**O(n)**

---

## **Viva Questions**

**Q1. Why does Huffman give optimal prefix codes?**
Because it always merges the two lowest-frequency nodes (greedy choice).

**Q2. What is a prefix code?**
No code is a prefix of another → avoids decoding ambiguity.

**Q3. What data structure is used?**
Min-Heap (priority queue).

**Q4. Why do we traverse left=0 and right=1 in the tree?**
To generate unique binary codes.

**Q5. Can Huffman be used for images?**
Yes, part of PNG, JPEG compression pipelines.

---

---

# **DAA Practical 3 — Fractional Knapsack (Greedy)**

## **Aim**

Maximize profit by choosing items (fraction allowed) using greedy ratio sorting.

---

## **Concept**

Each item has:

* Weight
* Value
* Value/Weight ratio

Greedy steps:

1. Compute ratio = value/weight
2. Sort items by ratio descending
3. Take full items until capacity is reached
4. Take fraction of last item

---

## **Complexity**

Sorting → **O(n log n)**
Selection → **O(n)**
Total → **O(n log n)**

---

## **Viva Questions**

**Q1. Why fractional knapsack is greedy but 0-1 knapsack is not?**
Because fractional knapsack allows taking part of an item → greedy is guaranteed optimal.

**Q2. What happens if partial items are not allowed?**
It becomes 0-1 knapsack.

**Q3. What is optimal substructure?**
A problem whose solution can be built from solutions of subproblems.

**Q4. Where is knapsack used?**
Loading trucks, portfolio optimization, resource allocation.

---

---

# **DAA Practical 4 — 0-1 Knapsack (Dynamic Programming)**

## **Aim**

To implement 0-1 knapsack (no fractional items allowed).

---

## **Concept**

State definition:

dp[i][w] = max profit using first i items with capacity w

Transition:

If item fits:
dp[i][w] = max( include , exclude )

If not:
dp[i][w] = dp[i−1][w]

---

## **Complexity**

| Approach | Time       | Space      |
| -------- | ---------- | ---------- |
| DP       | **O(n·W)** | **O(n·W)** |

---

## **Viva Questions**

**Q1. Why greedy fails for 0-1 knapsack?**
Because taking the best ratio item may block a more optimal combination.

**Q2. Why DP works?**
It tries all combinations using tabulation.

**Q3. What is overlapping subproblem property?**
Same subproblems occur repeatedly → DP is ideal.

**Q4. Where is 0-1 knapsack used?**
Budget planning, project selection, resource scheduling.

---

---

# **DAA Practical 5 — N-Queens (Backtracking)**

## **Aim**

Place N queens on an NxN board such that none attack each other.

---

## **Concept**

A queen attacks horizontally, vertically, diagonally.

Backtracking steps:

1. Place 1 queen per row
2. Check if safe
3. If safe → move to next row
4. If stuck → backtrack

---

## **Complexity**

Worst-case exponential: **O(N!)**

---

## **Viva Questions**

**Q1. Why backtracking?**
Because it systematically tries all safe possibilities.

**Q2. What is pruning?**
Stopping a path early if it's invalid.

**Q3. What does is_safe() check?**
Column + 2 diagonals.

**Q4. Can N-Queens be solved with greedy?**
No, requires backtracking or advanced algorithms.

---

---

# **DAA Practical 6 — Quick Sort (Deterministic vs Randomized)**

## **Aim**

Compare quicksort with fixed pivot vs random pivot selection.

---

## **Concept**

Deterministic: pivot = first/last element
Randomized: pivot = randomly chosen element

Random pivot avoids worst case on sorted arrays.

---

## **Complexity**

| Variant       | Average    | Worst      | Reason                     |
| ------------- | ---------- | ---------- | -------------------------- |
| Deterministic | O(n log n) | O(n²)      | Bad pivot chosen           |
| Randomized    | O(n log n) | O(n log n) | Unlikely to hit worst-case |

Randomized is generally preferred.

---

## **Viva Questions**

**Q1. Why is randomized quicksort faster?**
It avoids worst-case pivot patterns.

**Q2. Is quicksort stable?**
No.

**Q3. Does quicksort use extra memory?**
Tail recursion → O(log n) space.

**Q4. What is partitioning?**
Rearranging elements around pivot.

---

---

# **DAA Practical 7 — Matrix Multiplication + Multithreading**

## **Aim**

To implement normal matrix multiplication and accelerate using threads.

---

## **Concept**

Normal multiplication: 3 nested loops → O(n³)

Two threading methods:

### **1. One thread per row**

Each thread computes one row of result.

### **2. One thread per cell**

Each thread computes one cell.

---

## **Performance**

* Per-row = faster for large matrices
* Per-cell = huge overhead (too many threads)

---

## **Viva Questions**

**Q1. Which method is better?**
Thread-per-row (balanced workload).

**Q2. Why is thread-per-cell slow?**
Too many threads → context switching overhead.

**Q3. Time complexity?**
Computation: O(n³)
Multithreading improves constant factor only.

---

---

# **DAA Practical 8 — Merge Sort & Multithreaded Merge Sort**

## **Concept**

Merge sort = divide array into halves until 1 element, then merge.

Multithreaded version:
Create threads for left and right halves.

---

## **Complexity**

| Case  | Time       |
| ----- | ---------- |
| Best  | O(n log n) |
| Worst | O(n log n) |

Multithreaded version reduces merge time on multi-core CPUs.

---

## **Viva Questions**

**Q1. Why merge sort is stable?**
During merge, equal elements keep their original order.

**Q2. Why good for large data?**
Predictable O(n log n) performance.

**Q3. Why thread count must be limited?**
Too many threads reduces performance.

---

---

# **DAA Practical 9 — Naive String Matching vs Rabin-Karp**

## **Concept**

### **Naive Approach**

Check pattern at every index → O(n·m)

### **Rabin-Karp**

Uses rolling hash → average O(n+m)

---

## **Difference**

| Algorithm  | Avg Time | Worst Time | Notes        |
| ---------- | -------- | ---------- | ------------ |
| Naive      | O(nm)    | O(nm)      | Simple       |
| Rabin-Karp | O(n+m)   | O(nm)      | Uses hashing |

---

## **Viva Questions**

**Q1. Why Rabin-Karp is faster?**
Because it compares hash values instead of entire strings.

**Q2. When does Rabin-Karp degrade?**
Hash collisions.

**Q3. What is rolling hash?**
Hash updated in O(1) when sliding window.
