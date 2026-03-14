---
tags: [CS2040C, complexity, big-o, analysis]
---

# Complexity Analysis

## Overview

Complexity analysis is the foundation of algorithm design. It provides a framework to evaluate how an algorithm's resource usage (time or space) scales with input size $n$. In CS2040C, we primarily use **Big-O notation** to express worst-case upper bounds.

## Asymptotic Notations

| Notation | Meaning | Formal Definition |
|----------|---------|-------------------|
| $O(f(n))$ | Upper bound (worst case) | $T(n) \leq c \cdot f(n)$ for all $n \geq n_0$ |
| $\Omega(f(n))$ | Lower bound (best case) | $T(n) \geq c \cdot f(n)$ for all $n \geq n_0$ |
| $\Theta(f(n))$ | Tight bound | $c_1 \cdot f(n) \leq T(n) \leq c_2 \cdot f(n)$ |

> [!important] Big-O Growth Rate Hierarchy
> $O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$

## Analyzing Time Complexity

### Rules for Counting Operations

1. **Simple statements** (assignment, comparison, arithmetic): $O(1)$
2. **Sequential statements**: Add complexities (take the dominant term)
3. **If-else**: Take the worst case of the two branches
4. **Loops**: Multiply the loop body cost by the number of iterations
5. **Nested loops**: Multiply the complexities of each loop level

### Common Patterns

**Single loop over n elements:**
```cpp
for (int i = 0; i < n; i++) {
    // O(1) work
}
// Total: O(n)
```

**Nested loops:**
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // O(1) work
    }
}
// Total: O(n^2)
```

**Halving loop (logarithmic):**
```cpp
for (int i = n; i > 0; i /= 2) {
    // O(1) work
}
// Total: O(log n)
```

**Dependent nested loop:**
```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < i; j++) {
        // O(1) work
    }
}
// Total: 0 + 1 + 2 + ... + (n-1) = n(n-1)/2 = O(n^2)
```

## Space Complexity

Space complexity measures the additional memory an algorithm requires beyond the input.

| Usage | Space |
|-------|-------|
| Fixed number of variables | $O(1)$ |
| Array of size n | $O(n)$ |
| 2D matrix n x n | $O(n^2)$ |
| Recursive call stack depth d | $O(d)$ |

> [!note] In-Place Algorithms
> An algorithm is **in-place** if it uses only $O(1)$ extra space (not counting the input). Examples: Insertion Sort, Bubble Sort. Counter-example: Merge Sort uses $O(n)$ extra space.

## Recurrence Relations

Many recursive algorithms have time complexity described by recurrences.

### Master Theorem

For recurrences of the form $T(n) = aT(n/b) + O(n^d)$:

| Condition | Result |
|-----------|--------|
| $d > \log_b a$ | $T(n) = O(n^d)$ |
| $d = \log_b a$ | $T(n) = O(n^d \log n)$ |
| $d < \log_b a$ | $T(n) = O(n^{\log_b a})$ |

### Common Recurrences

| Algorithm | Recurrence | Solution |
|-----------|-----------|----------|
| Binary Search | $T(n) = T(n/2) + O(1)$ | $O(\log n)$ |
| Merge Sort | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| Quick Sort (avg) | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| Quick Sort (worst) | $T(n) = T(n-1) + O(n)$ | $O(n^2)$ |

## Amortized Analysis

> [!note] Key Idea
> Some operations may be expensive occasionally but cheap on average. Amortized analysis gives a tighter bound by averaging over a sequence of operations.

**Example: Dynamic Array (std::vector)**
- Most `push_back` operations are $O(1)$
- Occasionally requires resizing (copy all elements): $O(n)$
- Amortized cost per insertion: $O(1)$ (doubling strategy)

## Complexity Comparison Table

| Complexity | Name | Example Operations |
|-----------|------|-------------------|
| $O(1)$ | Constant | Array access, hash table lookup (avg) |
| $O(\log n)$ | Logarithmic | Binary search, BST operations (balanced) |
| $O(n)$ | Linear | Linear search, traversing a list |
| $O(n \log n)$ | Linearithmic | Merge sort, heap sort |
| $O(n^2)$ | Quadratic | Bubble sort, insertion sort (worst) |
| $O(n^3)$ | Cubic | Floyd-Warshall, naive matrix multiply |
| $O(2^n)$ | Exponential | Subset enumeration |
| $O(n!)$ | Factorial | Generating all permutations |

> [!warning] Practical Guideline
> For competitive programming and CS2040C problems, a rough rule: $10^8$ simple operations per second. So for $n = 10^6$, an $O(n \log n)$ algorithm runs in about 0.02s, but an $O(n^2)$ algorithm takes about 1000s.

## Related Notes

- [[Sorting Algorithms]] - complexity analysis applied to sorting
- [[Trees and BSTs]] - logarithmic operations on balanced trees
- [[Hash Tables]] - amortized O(1) operations
