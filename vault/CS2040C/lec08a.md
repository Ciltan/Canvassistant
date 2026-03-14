---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 08a - Hash Table

## Overview
In this lecture, we delve into the concept of Hash Tables, a crucial data structure in computer science. We explore the Table Abstract Data Type (ADT), Direct Addressing Tables (DAT), and various hashing techniques, including collision resolution strategies. The session also includes practical examples and discussions on the implications of load factors and performance in hash table implementations.

## Key Concepts & Definitions
- **Hash Table**: A data structure that implements an associative array, a structure that can map keys to values.
- **Table ADT**: An abstract data type that allows for efficient search, insert, and remove operations.
- **Direct Addressing Table (DAT)**: A type of table where the key itself is used as an index to store associated data.
- **Hashing**: The process of converting an input (or 'key') into a fixed-size string of bytes.
- **Collision Resolution (CR)**: Techniques used to handle situations where two keys hash to the same index.
- **Open Addressing (OA)**: A collision resolution method that finds another open slot within the hash table itself.
- **Separate Chaining (SC)**: A collision resolution method that uses linked lists to store multiple values at the same index.

## Detailed Technical Breakdown

### Table ADT
- **Comparison with List ADT**:
  - In a [[List ADT]], specific positioning of values is crucial.
  - In a [[Table ADT]], the underlying data structure manages positioning, allowing for operations faster than O(N).

### Direct Addressing Table (DAT)
- **Key Concept**: Uses integer keys as indices for storage.
- **Size Consideration**: A size slightly larger than the maximum key value is often used to avoid off-by-one errors.

### Hashing
- **Birthday Paradox**: A classic problem illustrating the counterintuitive nature of probability in hashing.
- **Prime Number Size**: Hash tables are often sized to prime numbers to maximize efficiency.

### Collision Resolution Techniques
1. **Separate Chaining (SC)**:
   - Utilizes an array of linked lists.
   - Time complexity for search and remove operations is O(1 + α), where α is the load factor.

2. **Open Addressing (OA)**:
   - **Linear Probing (LP)**: Searches for the next available slot in a linear manner.
     - **Primary Clustering**: A performance issue where clusters of filled slots degrade efficiency.
   - **Quadratic Probing (QP)**: Uses a quadratic function to find the next available slot.
     - **Secondary Clustering**: Similar to primary clustering but less severe.

3. **Double Hashing (DH)**:
   - Uses a second hash function to determine the step size for probing.
   - Avoids clustering issues associated with linear and quadratic probing.

### Performance Considerations
- **Load Factor (α)**: The ratio of the number of entries to the number of slots in the hash table.
- **Deleted Markers**: Special markers used in OA techniques to handle deletions without losing the integrity of the hash table.

## Implementation/Examples
```cpp
class MyHashMap {
private:
    hash_table<int, int>* ht;
public:
    MyHashMap() {
        ht = new hash_table<int, int>(997);
    }
    void put(int key, int value) {
        ht->insert({key, value});
    }
    int get(int key) {
        return ht->find(key);
    }
    void remove(int key) {
        ht->erase(key);
    }
};
/**
* Your MyHashMap object will be instantiated and called as such:
* MyHashMap* obj = new MyHashMap();
* obj->put(key,value);
* int param_2 = obj->get(key);
* obj->remove(key);
*/
```

> [!note] **Important Note**: The choice of hash table size and collision resolution technique significantly impacts performance. Always consider the load factor when designing hash tables.

> [!warning] **Caution**: Avoid using high load factors (> 0.5) with open addressing techniques to prevent performance degradation.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[lec04a]]
- [[ch2]]
- [[lec04b]]
- [[Stacks and Queues]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]