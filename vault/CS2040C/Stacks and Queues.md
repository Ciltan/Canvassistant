---
tags: [CS2040C, stacks, queues, ADT, linear-data-structures]
---

# Stacks and Queues

## Overview

Stacks and queues are abstract data types (ADTs) that restrict how elements are added and removed. A **stack** follows Last-In-First-Out (LIFO) order, while a **queue** follows First-In-First-Out (FIFO) order. Both can be implemented using arrays or linked lists.

## Stack (LIFO)

### Concept

A stack only allows operations at one end (the "top"):
- **Push**: Add element to the top
- **Pop**: Remove element from the top
- **Peek/Top**: View the top element without removing

Think of it like a stack of plates: you can only add or remove from the top.

### Array-Based Implementation

```cpp
class ArrayStack {
    int arr[MAX_SIZE];
    int topIdx;
public:
    ArrayStack() : topIdx(-1) {}

    void push(int val) {
        if (topIdx == MAX_SIZE - 1) throw overflow_error("Stack full");
        arr[++topIdx] = val;
    }

    int pop() {
        if (isEmpty()) throw underflow_error("Stack empty");
        return arr[topIdx--];
    }

    int top() {
        if (isEmpty()) throw underflow_error("Stack empty");
        return arr[topIdx];
    }

    bool isEmpty() { return topIdx == -1; }
    int size() { return topIdx + 1; }
};
```

### Linked List Implementation

```cpp
class LinkedStack {
    Node* topNode;
    int count;
public:
    LinkedStack() : topNode(nullptr), count(0) {}

    void push(int val) {
        Node* newNode = new Node(val);
        newNode->next = topNode;
        topNode = newNode;
        count++;
    }

    int pop() {
        if (isEmpty()) throw underflow_error("Stack empty");
        int val = topNode->data;
        Node* temp = topNode;
        topNode = topNode->next;
        delete temp;
        count--;
        return val;
    }

    int top() { return topNode->data; }
    bool isEmpty() { return topNode == nullptr; }
};
```

### Stack Operations Complexity

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Push | $O(1)$ amortized | $O(1)$ |
| Pop | $O(1)$ | $O(1)$ |
| Top/Peek | $O(1)$ | $O(1)$ |
| isEmpty | $O(1)$ | $O(1)$ |

### Stack Applications

1. **Expression evaluation**: Postfix (RPN) evaluation, infix to postfix conversion
2. **Parenthesis matching**: Check if brackets are balanced
3. **Function call stack**: Runtime call management and recursion
4. **Undo/Redo**: Text editors, browser back button
5. **DFS traversal**: Iterative depth-first search on graphs

> [!important] Parenthesis Matching Algorithm
> ```cpp
> bool isBalanced(string s) {
>     stack<char> st;
>     for (char c : s) {
>         if (c == '(' || c == '[' || c == '{') st.push(c);
>         else {
>             if (st.empty()) return false;
>             char top = st.top(); st.pop();
>             if ((c == ')' && top != '(') ||
>                 (c == ']' && top != '[') ||
>                 (c == '}' && top != '{'))
>                 return false;
>         }
>     }
>     return st.empty();
> }
> ```

## Queue (FIFO)

### Concept

A queue allows:
- **Enqueue**: Add element to the back
- **Dequeue**: Remove element from the front
- **Front/Peek**: View the front element

Think of it like a line at a counter: first person in line gets served first.

### Circular Array Implementation

```cpp
class CircularQueue {
    int arr[MAX_SIZE];
    int front, rear, count;
public:
    CircularQueue() : front(0), rear(-1), count(0) {}

    void enqueue(int val) {
        if (count == MAX_SIZE) throw overflow_error("Queue full");
        rear = (rear + 1) % MAX_SIZE;
        arr[rear] = val;
        count++;
    }

    int dequeue() {
        if (isEmpty()) throw underflow_error("Queue empty");
        int val = arr[front];
        front = (front + 1) % MAX_SIZE;
        count--;
        return val;
    }

    int peek() { return arr[front]; }
    bool isEmpty() { return count == 0; }
    int size() { return count; }
};
```

> [!note] Why Circular?
> A naive array queue wastes space as `front` advances. A circular array wraps around using modulo arithmetic: `(index + 1) % capacity`. This reuses vacated positions at the front.

### Linked List Implementation

```cpp
class LinkedQueue {
    Node* front;
    Node* rear;
    int count;
public:
    LinkedQueue() : front(nullptr), rear(nullptr), count(0) {}

    void enqueue(int val) {
        Node* newNode = new Node(val);
        if (rear) rear->next = newNode;
        rear = newNode;
        if (!front) front = newNode;
        count++;
    }

    int dequeue() {
        if (isEmpty()) throw underflow_error("Queue empty");
        int val = front->data;
        Node* temp = front;
        front = front->next;
        if (!front) rear = nullptr;
        delete temp;
        count--;
        return val;
    }

    int peek() { return front->data; }
    bool isEmpty() { return front == nullptr; }
};
```

### Queue Operations Complexity

| Operation | Circular Array | Linked List |
|-----------|---------------|-------------|
| Enqueue | $O(1)$ | $O(1)$ |
| Dequeue | $O(1)$ | $O(1)$ |
| Peek | $O(1)$ | $O(1)$ |
| isEmpty | $O(1)$ | $O(1)$ |

### Queue Applications

1. **BFS traversal**: Level-order traversal of trees and graphs
2. **Scheduling**: CPU task scheduling, print queue
3. **Buffering**: I/O buffers, producer-consumer pattern

## Deque (Double-Ended Queue)

Allows insertion and removal from both ends. In C++: `std::deque`.

| Operation | Time |
|-----------|------|
| Push front / back | $O(1)$ |
| Pop front / back | $O(1)$ |
| Access by index | $O(1)$ |

## C++ STL

```cpp
#include <stack>
#include <queue>
#include <deque>

stack<int> s;        // LIFO - uses deque internally
queue<int> q;        // FIFO - uses deque internally
deque<int> dq;       // Double-ended queue

// Priority queue (max-heap by default)
priority_queue<int> pq;
// Min-heap:
priority_queue<int, vector<int>, greater<int>> minPQ;
```

## Related Notes

- [[Arrays and Linked Lists]] - underlying implementations
- [[Graphs]] - BFS uses queues, DFS uses stacks
- [[Trees and BSTs]] - level-order traversal uses queues
- [[Heaps and Priority Queues]] - priority queue as specialized queue
