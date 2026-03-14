---
tags: [CS2040C, arrays, linked-lists, linear-data-structures]
---

# Arrays and Linked Lists

## Overview

Arrays and linked lists are the two fundamental linear data structures. They represent different tradeoffs between random access speed, insertion/deletion efficiency, and memory usage. Understanding these tradeoffs is essential for choosing the right data structure.

## Arrays

### Static Arrays

Fixed-size, contiguous block of memory. In C++: `int arr[100];`

```cpp
// Declaration and initialization
int arr[5] = {10, 20, 30, 40, 50};

// Access by index
int val = arr[2]; // O(1) - direct memory offset calculation
```

### Dynamic Arrays (std::vector)

Resizable array that doubles capacity when full.

```cpp
#include <vector>
vector<int> v;
v.push_back(10);    // Amortized O(1)
v.push_back(20);
v[0] = 15;          // O(1) access
v.pop_back();       // O(1)
v.insert(v.begin() + 1, 25); // O(n) - shifts elements
v.erase(v.begin());          // O(n) - shifts elements
```

> [!note] Doubling Strategy
> When a vector is full and a new element is added:
> 1. Allocate new array of 2x capacity
> 2. Copy all elements to new array
> 3. Delete old array
>
> This gives **amortized** $O(1)$ insertion. The total cost of $n$ insertions is $O(n)$, even though individual insertions occasionally cost $O(n)$.

### Array Operations Complexity

| Operation | Time |
|-----------|------|
| Access by index | $O(1)$ |
| Search (unsorted) | $O(n)$ |
| Search (sorted, binary search) | $O(\log n)$ |
| Insert at end (dynamic) | Amortized $O(1)$ |
| Insert at position | $O(n)$ |
| Delete at end | $O(1)$ |
| Delete at position | $O(n)$ |

## Linked Lists

### Singly Linked List

Each node contains data and a pointer to the next node.

```cpp
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class SinglyLinkedList {
    Node* head;
public:
    SinglyLinkedList() : head(nullptr) {}

    // Insert at front: O(1)
    void insertFront(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    // Insert at back: O(n) - must traverse to end
    void insertBack(int val) {
        Node* newNode = new Node(val);
        if (!head) { head = newNode; return; }
        Node* curr = head;
        while (curr->next) curr = curr->next;
        curr->next = newNode;
    }

    // Delete node with given value: O(n)
    void deleteNode(int val) {
        if (!head) return;
        if (head->data == val) {
            Node* temp = head;
            head = head->next;
            delete temp;
            return;
        }
        Node* curr = head;
        while (curr->next && curr->next->data != val)
            curr = curr->next;
        if (curr->next) {
            Node* temp = curr->next;
            curr->next = temp->next;
            delete temp;
        }
    }

    // Search: O(n)
    bool search(int val) {
        Node* curr = head;
        while (curr) {
            if (curr->data == val) return true;
            curr = curr->next;
        }
        return false;
    }
};
```

### Doubly Linked List

Each node has pointers to both the next and previous nodes.

```cpp
struct DNode {
    int data;
    DNode* prev;
    DNode* next;
    DNode(int val) : data(val), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedList {
    DNode* head;
    DNode* tail;
public:
    DoublyLinkedList() : head(nullptr), tail(nullptr) {}

    // Insert at front: O(1)
    void insertFront(int val) {
        DNode* newNode = new DNode(val);
        newNode->next = head;
        if (head) head->prev = newNode;
        head = newNode;
        if (!tail) tail = newNode;
    }

    // Insert at back: O(1) with tail pointer
    void insertBack(int val) {
        DNode* newNode = new DNode(val);
        newNode->prev = tail;
        if (tail) tail->next = newNode;
        tail = newNode;
        if (!head) head = newNode;
    }

    // Delete a known node: O(1)
    void deleteNode(DNode* node) {
        if (node->prev) node->prev->next = node->next;
        else head = node->next;
        if (node->next) node->next->prev = node->prev;
        else tail = node->prev;
        delete node;
    }
};
```

### Linked List Operations Complexity

| Operation | Singly | Doubly |
|-----------|--------|--------|
| Insert at front | $O(1)$ | $O(1)$ |
| Insert at back | $O(n)$ / $O(1)$ with tail | $O(1)$ with tail |
| Delete front | $O(1)$ | $O(1)$ |
| Delete back | $O(n)$ | $O(1)$ with tail |
| Delete known node | $O(n)$ (need prev) | $O(1)$ |
| Search | $O(n)$ | $O(n)$ |
| Access by index | $O(n)$ | $O(n)$ |

## Array vs Linked List Comparison

| Feature | Array | Linked List |
|---------|-------|-------------|
| Memory layout | Contiguous | Scattered (nodes + pointers) |
| Random access | $O(1)$ | $O(n)$ |
| Insert/delete at front | $O(n)$ | $O(1)$ |
| Insert/delete at end | Amortized $O(1)$ | $O(1)$ with tail pointer |
| Insert/delete in middle | $O(n)$ | $O(1)$ if node is known |
| Memory overhead | Low | Higher (pointer storage) |
| Cache performance | Excellent (locality) | Poor (pointer chasing) |

> [!warning] Memory and Cache
> Arrays have significantly better cache performance due to spatial locality. Even though linked lists have better theoretical complexity for some operations, arrays are often faster in practice for small to medium data sets due to hardware caching.

## C++ STL Containers

| Container | Underlying Structure | Key Use |
|-----------|---------------------|---------|
| `std::vector` | Dynamic array | Default choice; random access |
| `std::list` | Doubly linked list | Frequent insert/delete in middle |
| `std::forward_list` | Singly linked list | Minimal overhead linked list |
| `std::deque` | Array of arrays | Fast front and back operations |

## Related Notes

- [[Stacks and Queues]] - built on top of arrays/linked lists
- [[Sorting Algorithms]] - sorting these data structures
- [[Complexity Analysis]] - analyzing operations on linear structures
