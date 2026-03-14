---
tags: [CS2040C, lecture-notes, academic]
---

# Lecture 05: Heaps and HeapSort

## Overview
This lecture introduces the concept of [[Priority Queues]] and their implementation using [[Binary Heaps]]. We explore the operations associated with priority queues, including insertion and extraction of elements based on priority. The lecture culminates in a discussion of [[HeapSort]], a sorting algorithm that utilizes heaps to efficiently sort data.

## Key Concepts & Definitions
- **Priority Queue ADT**: An abstract data type that maintains a set of prioritized objects, allowing for operations such as `insert`, `extractMin`, and `decreaseKey`.
- **Binary Heap**: A complete binary tree that satisfies the heap property, where the parent node's priority is greater than or equal to that of its children.
- **HeapSort**: A sorting algorithm that leverages the properties of heaps to sort elements in O(n log n) time.

## Detailed Technical Breakdown

### Priority Queue Operations
- **Min Priority Queue**:
  - `insert(Key k, Priority p)`: Adds a new object with a specified priority.
  - `extractMin()`: Removes and returns the object with the minimum priority.
  - `decreaseKey(Key k, Priority p)`: Reduces the priority of a key.
  - `contains(Key k)`: Checks if the queue contains a specific key.
  - `isEmpty()`: Checks if the queue is empty.

- **Max Priority Queue**:
  - Similar operations as Min Priority Queue, but focused on maximum priority.

### Performance Analysis
| Implementation Type | Insert Time | Extract Max Time |
|---------------------|-------------|-------------------|
| Sorted Array        | O(n)       | O(1)              |
| Unsorted Array      | O(1)       | O(n)              |
| AVL Tree            | O(log n)   | O(log n)          |
| Binary Heap         | O(log n)   | O(log n)          |

### Properties of a MaxHeap
1. **Heap Ordering**: For any given node, the priority of the parent is greater than or equal to that of its children.
2. **Complete Binary Tree**: All levels are fully filled except possibly the last, which is filled from left to right.

### Heap Operations
- **Insert**: Add a new element and bubble it up to maintain heap order.
- **ExtractMax**: Remove the root and bubble down to restore heap order.
- **IncreaseKey**: Update the priority of a key and bubble up if necessary.
- **DecreaseKey**: Update the priority and bubble down if necessary.
- **Delete**: Remove a specific element and restore heap order.

## Implementation/Examples
```java
class MaxHeap {
    private List<Node> heap;

    public void insert(int priority, Key key) {
        Node newNode = new Node(priority, key);
        heap.add(newNode);
        bubbleUp(heap.size() - 1);
    }

    private void bubbleUp(int index) {
        while (index > 0) {
            int parentIndex = (index - 1) / 2;
            if (heap.get(index).priority > heap.get(parentIndex).priority) {
                swap(index, parentIndex);
                index = parentIndex;
            } else {
                break;
            }
        }
    }

    public Key extractMax() {
        if (heap.isEmpty()) return null;
        Key max = heap.get(0).key;
        heap.set(0, heap.remove(heap.size() - 1));
        bubbleDown(0);
        return max;
    }

    private void bubbleDown(int index) {
        while (index < heap.size()) {
            int leftChild = 2 * index + 1;
            int rightChild = 2 * index + 2;
            int largest = index;

            if (leftChild < heap.size() && heap.get(leftChild).priority > heap.get(largest).priority) {
                largest = leftChild;
            }
            if (rightChild < heap.size() && heap.get(rightChild).priority > heap.get(largest).priority) {
                largest = rightChild;
            }
            if (largest != index) {
                swap(index, largest);
                index = largest;
            } else {
                break;
            }
        }
    }

    private void swap(int i, int j) {
        Node temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }
}
```

> [!note] **Heap Storage**: A binary heap can be efficiently stored in an array, where the parent-child relationship can be calculated using indices.
> 
> [!important] **HeapSort Complexity**: The overall time complexity for HeapSort is O(n log n), making it efficient for large datasets.

## Related
- [[HeapSort]]
- [[Binary Heaps]]
- [[Priority Queues]]
- [[CS2040C]]