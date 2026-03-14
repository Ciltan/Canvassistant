---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 02a

## Overview
This lecture focuses on Big O asymptotic analysis, a crucial concept in evaluating the efficiency of algorithms. We explore various sorting algorithms, contrasting slower O(n²) methods with faster O(n log n) techniques. The session includes practical demonstrations and a live coding exercise to solidify understanding of these concepts.

## Key Concepts & Definitions
- **Big O Notation**: A mathematical notation used to describe the upper limit of an algorithm's runtime or space requirements in terms of input size, denoted as O(f(n)).
- **Asymptotic Analysis**: The study of the behavior of algorithms as the input size approaches infinity.
- **Sorting Algorithms**: Techniques for arranging elements in a specified order. Key types include:
  - **O(n²) Slow Sorting Algorithms**: Such as [[Bubble Sort]], [[Insertion Sort]], and [[Selection Sort]].
  - **O(n log n) Faster Sorting Algorithms**: Such as [[Merge Sort]] and [[Quick Sort]].
- **Arithmetic Progression (AP)**: A sequence of numbers in which the difference between consecutive terms is constant.
- **Geometric Progression (GP)**: A sequence where each term after the first is found by multiplying the previous term by a fixed, non-zero number.

## Detailed Technical Breakdown

### Opening Activity
- **Objective**: Sort two shuffled decks of cards.
- **Participants**: Two students shuffle, two students sort.
- **Recorded Times**: 2m 21s and 3m 40s.

### Course Administration
- **PS0 Issues**: Only 147 out of 160 students scored ≥ 300 points.
- **VA Account Activation**: Ensure activation before VA OQ 1.
- **Lab Group Assignments**: 145 out of 160 students have their own lab groups.

### Mathematical Background Check
- **Sum of Arithmetic Progression**:
  - \(1 + 2 + 3 + ... + n = \frac{n(n + 1)}{2}\) is in O(n²).
- **Sum of Geometric Progression**:
  - \(1 + \frac{1}{2} + \frac{1}{4} + ... = 2\) is in O(n).
- **Harmonic Series**:
  - \(H_n = 1 + \frac{1}{2} + \frac{1}{3} + ... + \frac{1}{n}\) is bounded by O(log n).

### Basic Asymptotic Algorithm Analysis
- **Demonstration of O(n²)**: Using SpeedTest.cpp to measure runtime.
- **Customizing SpeedTest.cpp**:
  - O(n): Remove one loop.
  - O(n³): Add an innermost loop.
  - O(n log n): Change one loop to log.
  - O(log n): Keep only the log growth loop.
  - O(1): Constant steps regardless of n.

### Live Coding Example
#### Problem: /thanos
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int T; cin >> T;
    while (T--) {
        long long P, R, F; cin >> P >> R >> F;
        int ans = 0;
        while (P <= F) {
            ++ans;
            P *= R;
        }
        cout << ans << '\n';
    }
    return 0;
}
```
- **Time Complexity**: O(T * log F).

### Sorting Algorithms
- **Bubble Sort**:
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n = 5, A[n];
    for (int i = 0; i < n; i++)
        scanf("%d", &A[i]);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n-1; j++)
            if (A[j] > A[j+1]) {
                swap(A[j], A[j+1]);
                for (int k = 0; k < n; k++)
                    printf("%d ", A[k]);
                printf("\n");
            }
    return 0;
}
```
- **Time Complexity**: O(n²).

## Implementation/Examples
- **Live Solve Another Application**: 
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n; cin >> n;
    vector<int> c(n, 0);
    for (auto& ci : c)
        cin >> ci;
    sort(c.begin(), c.end());
    int ans = c[0];
    for (int i = 1; i < n; ++i)
        if (c[i] != c[i-1] + 1)
            ans += c[i];
    cout << ans << '\n';
    return 0;
}
```
- **Time Complexity**: O(n log n).

> [!note] Remember to review the sorting algorithms and their complexities for the upcoming midterm.
> [!important] Ensure your VA account is activated to participate in upcoming assessments.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]