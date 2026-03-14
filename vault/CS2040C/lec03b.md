---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Sorting Extras

## Overview
This lecture focuses on advanced sorting techniques and introduces the concept of prefix sums. It highlights the limitations of comparison-based sorting algorithms, emphasizing that the best achievable time complexity is Ω(n log n) for sorting n elements. Additionally, it explores alternative sorting methods, such as [[Counting Sort]], and discusses the counting of inversions and minimum swaps required to sort an array.

## Key Concepts & Definitions
- **Sorting**: The process of arranging elements in a specified order.
- **Comparison-based Sorting**: A sorting method that determines the order of elements through pairwise comparisons.
- **Counting Sort**: A non-comparison-based sorting algorithm that counts the occurrences of each element.
- **Inversions**: A pair of indices (i, j) such that i < j and A[i] > A[j].
- **Prefix Sum**: A technique for calculating cumulative sums of a sequence of numbers.

## Detailed Technical Breakdown

### Sorting Techniques
- **Comparison-based Sorting Lower Bound**:
  - The theoretical lower bound for sorting n elements using comparisons is Ω(n log n).
  
- **Counting Sort Example**:
  - An alternative solution for sorting colors using counting sort:
    ```cpp
    class Solution {
    public:
        void sortColors(vector<int>& nums) {
            int f[3] = {0}; // Frequency array for 0s, 1s, and 2s
            for (const auto& num : nums) // O(n)
                ++f[num];
            int k = 0; // Output index
            for (int i = 0; i <= 2; ++i) // Sorted order is 0s, 1s, and 2s
                for (int j = 0; j < f[i]; ++j) // Echo i, f[i] times
                    nums[k++] = i;
        }
    };
    ```

### Counting Inversions and Minimum Swaps
- **Counting Inversions**:
  - Naive approach: O(n²) by counting pairs directly.
  - Efficient approach: O(n log n) by counting during the merge step of [[Merge Sort]].

- **Counting Minimum Swaps**:
  - Naive approach: O(n²) using [[Selection Sort]].
  - Efficient approach: O(n log n) (details to be studied independently).

### Prefix Sum Example
- **Finding the Highest Altitude**:
  - A simple problem demonstrating the use of prefix sums:
    ```cpp
    class Solution {
    public:
        int largestAltitude(vector<int>& gain) {
            int n = (int)gain.size();
            int pre[n+1]; // Array to store prefix sums
            pre[0] = 0; // Starting altitude
            for (int i = 1; i <= n; ++i) // Offset by 1
                pre[i] = pre[i-1] + gain[i-1];
            return *max_element(pre, pre+n+1); // Maximum altitude
        }
    };
    ```

> [!note] **Important Note**: Understanding the limitations of comparison-based sorting is crucial for grasping more advanced sorting techniques.
> 
> [!warning] **Caution**: While prefix sums can simplify certain problems, ensure you understand their application to avoid common pitfalls.

## Related
- [[lec04a]]: Further exploration of sorting algorithms.
- [[ch2]]: Fundamental concepts in data structures.
- [[Tutorial+1+Solution]]: Practical applications of sorting techniques.
- [[AY2122+Sem1+Homework+3]]: Related homework problems on sorting and algorithms.