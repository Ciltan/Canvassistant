---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 03a

## Overview
This lecture focuses on O(N log N) sorting algorithms, specifically exploring the intricacies of [[Merge Sort]] and [[Quick Sort]]. We revisit the sorting library and discuss the importance of custom comparison functions in sorting operations. Additionally, cultural insights are shared through the lens of the Five Blessings in Chinese culture, emphasizing the intersection of technical knowledge and broader life lessons.

## Key Concepts & Definitions
- **Sorting Algorithms**: Procedures for arranging elements in a specific order.
- **Merge Sort**: A divide-and-conquer algorithm that sorts by recursively splitting the array into halves, sorting each half, and merging them back together.
- **Quick Sort**: An efficient sorting algorithm that selects a 'pivot' and partitions the array into elements less than and greater than the pivot.
- **Stable Sort**: A sorting algorithm that maintains the relative order of records with equal keys.
- **Custom Comparison Function**: A user-defined function that specifies the criteria for comparing elements during sorting.

## Detailed Technical Breakdown

### Sorting Library, Revisited
- The default sorting library sorts elements based on their natural ordering.
- Custom comparison functions can be implemented using lambda expressions in C++.
- Example of a custom comparison function that compares the first two characters of strings.

### Merge Sort
- **Complexity**: O(N log N)
- **Stability**: Maintains the order of equal elements.
- **Temporary Array Requirement**: Merge Sort requires a temporary array of size O(n) for merging, making it not in-place.

### Quick Sort
- **Expected Complexity**: O(N log N)
- **Partitioning**: In-place partitioning is cache-friendly.
- **Stability**: Typically not stable due to element swapping.

### Implementation/Examples

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int n;
    bool FirstTC = true;
    while (1) {
        scanf("%d ", &n);
        if (n == 0) break;
        vector<string> names;
        for (int i = 0; i < n; ++i) {
            char name[25]; 
            scanf("%s ", &name);
            names.push_back(name);
        }
        sort(names.begin(), names.end(), [](string a, string b) {
            if (a[0] != b[0]) return a[0] < b[0];
            else return a[1] < b[1];
        });
        if (!FirstTC) cout << '\n';
        FirstTC = false;
        for (const auto& name : names) cout << name << '\n';
    }
    return 0;
}
```

> [!note] **Important Note**: The implementation of sorting algorithms can vary based on the programming language and the specific requirements of the problem at hand.

### Cultural Insight: The Five Blessings
1. **Longevity (sh`ou)**: A long life.
2. **Wealth (fu`)**: Prosperity and material comfort.
3. **Health (k¯ang n´ıng)**: Good physical and mental health.
4. **Virtue (yo¯u hˇao d´e)**: Love of virtue and noble character.
5. **Peaceful Death (kˇao zh¯ong m`ıng)**: A natural, peaceful death at old age.

> [!important] **Reminder**: If you missed the lecture, refer to the recording for context on the discussed topics.

## Related
- [[lec04a]]
- [[lec03b]]
- [[SortingDemo.cpp]]
- [[AY2122+Sem1+Homework+3]]
- [[Midterm+Briefing]]