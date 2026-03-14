---
tags: [CS2040C, heap, priority-queue, heapsort]
---

# Heaps and Priority Queues

## Overview

A **heap** is a complete binary tree that satisfies the heap property. A **max-heap** has the largest element at the root; a **min-heap** has the smallest. Heaps are the standard implementation for **priority queues**, which support efficient extraction of the minimum (or maximum) element. CS2040C also covers **Heap Sort**.

## Heap Properties

### Structure Property
A heap is a **complete binary tree**: all levels are fully filled except possibly the last, which is filled from left to right.

### Heap-Order Property
- **Max-Heap**: Every parent $\geq$ its children
- **Min-Heap**: Every parent $\leq$ its children

> [!note] Array Representation
> A complete binary tree maps naturally to an array (0-indexed):
> - Parent of node $i$: $\lfloor (i-1)/2 \rfloor$
> - Left child of node $i$: $2i + 1$
> - Right child of node $i$: $2i + 2$
>
> No pointers needed -- memory efficient!

## Heap Operations

### Insert (Swim / Bubble Up)

1. Add element at the end of the array (next available position)
2. **Swim up**: Compare with parent; swap if heap property violated; repeat

```cpp
class MinHeap {
    vector<int> heap;

    void swimUp(int idx) {
        while (idx > 0) {
            int parent = (idx - 1) / 2;
            if (heap[idx] < heap[parent]) {
                swap(heap[idx], heap[parent]);
                idx = parent;
            } else break;
        }
    }

    void sinkDown(int idx) {
        int n = heap.size();
        while (true) {
            int smallest = idx;
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            if (left < n && heap[left] < heap[smallest])
                smallest = left;
            if (right < n && heap[right] < heap[smallest])
                smallest = right;
            if (smallest != idx) {
                swap(heap[idx], heap[smallest]);
                idx = smallest;
            } else break;
        }
    }

public:
    void insert(int val) {
        heap.push_back(val);
        swimUp(heap.size() - 1);
    }

    int extractMin() {
        int minVal = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) sinkDown(0);
        return minVal;
    }

    int peekMin() { return heap[0]; }
    bool isEmpty() { return heap.empty(); }
    int size() { return heap.size(); }
};
```

### Extract Min/Max (Sink / Bubble Down)

1. Replace root with last element
2. Remove last element
3. **Sink down**: Compare root with children; swap with the smaller (min-heap) child; repeat

### Heap Operations Complexity

| Operation | Time |
|-----------|------|
| Insert | $O(\log n)$ |
| Extract Min/Max | $O(\log n)$ |
| Peek Min/Max | $O(1)$ |
| Build Heap (heapify) | $O(n)$ |
| Search | $O(n)$ (heap is not sorted) |

> [!important] Build Heap is O(n), not O(n log n)
> Building a heap by calling `sinkDown` on all internal nodes (from bottom up) is $O(n)$, not $O(n \log n)$. Intuitively, most nodes are near the leaves and sink only a few levels.
>
> Mathematical proof: $\sum_{h=0}^{\lfloor \log n \rfloor} \lceil n / 2^{h+1} \rceil \cdot O(h) = O(n)$

### Build Heap (Heapify)

```cpp
void buildHeap(vector<int>& arr) {
    int n = arr.size();
    // Start from last internal node, sink each down
    for (int i = n / 2 - 1; i >= 0; i--) {
        sinkDown(arr, i, n);
    }
}
```

## Heap Sort

Uses a max-heap to sort in ascending order:

1. Build a max-heap from the array: $O(n)$
2. Repeatedly extract the max and place at the end: $O(n \log n)$

```cpp
void heapSort(vector<int>& arr) {
    int n = arr.size();

    // Build max-heap
    for (int i = n / 2 - 1; i >= 0; i--)
        sinkDown(arr, i, n); // Max-heap sinkDown

    // Extract elements one by one
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);    // Move max to end
        sinkDown(arr, 0, i);     // Restore heap on reduced array
    }
}
```

| Case | Time | Space |
|------|------|-------|
| Best | $O(n \log n)$ | $O(1)$ |
| Average | $O(n \log n)$ | $O(1)$ |
| Worst | $O(n \log n)$ | $O(1)$ |

> [!note] Heap Sort Properties
> - **In-place**: Yes (only $O(1)$ extra space)
> - **Stable**: No
> - **Guaranteed** $O(n \log n)$: Unlike Quick Sort
> - In practice, slower than Quick Sort due to poor cache locality

## Priority Queue

A priority queue is an ADT that supports:
- **Insert** with a priority
- **Extract** the element with highest (or lowest) priority

### C++ STL Priority Queue

```cpp
#include <queue>

// Max-heap (default)
priority_queue<int> maxPQ;
maxPQ.push(10);
maxPQ.push(30);
maxPQ.push(20);
cout << maxPQ.top(); // 30
maxPQ.pop();

// Min-heap
priority_queue<int, vector<int>, greater<int>> minPQ;
minPQ.push(10);
minPQ.push(30);
minPQ.push(20);
cout << minPQ.top(); // 10

// Custom comparator for pairs
priority_queue<pair<int,int>, vector<pair<int,int>>,
               greater<pair<int,int>>> pq;
```

### Priority Queue Applications

1. **Dijkstra's shortest path algorithm**: Extract closest unvisited vertex
2. **Prim's MST algorithm**: Extract cheapest edge
3. **Huffman coding**: Build optimal prefix code
4. **K-th largest/smallest element**: Maintain a heap of size k
5. **Merge K sorted lists**: Use min-heap to track current minimums
6. **Event-driven simulation**: Process events in order of time

## Heap vs BST Comparison

| Feature | Heap | BST (Balanced) |
|---------|------|----------------|
| Find min/max | $O(1)$ (peek) | $O(\log n)$ |
| Extract min/max | $O(\log n)$ | $O(\log n)$ |
| Insert | $O(\log n)$ | $O(\log n)$ |
| Search | $O(n)$ | $O(\log n)$ |
| Find successor | $O(n)$ | $O(\log n)$ |
| Memory | Array (compact) | Pointers (overhead) |

> [!warning] When to Use Which
> - Use a **heap** when you only need the min/max element efficiently
> - Use a **BST** when you need search, ordered traversal, or successor/predecessor queries

## Related Notes

- [[Trees and BSTs]] - BSTs provide ordered operations heaps cannot
- [[Sorting Algorithms]] - Heap Sort as a comparison-based sort
- [[Graphs]] - Dijkstra's and Prim's use priority queues
- [[Complexity Analysis]] - understanding the O(n) build heap proof
