---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 01b

## Overview
In this lecture, we explore fundamental concepts in data structures and algorithms, focusing on operations with the [[std::vector]] in C++. We discuss the implementation of a ranking problem and a 2D grid traversal technique, both of which are essential for understanding algorithmic efficiency and problem-solving strategies. The lecture also emphasizes the importance of visual tools for algorithm analysis and preparation for upcoming tutorials.

## Key Concepts & Definitions
- **[[std::vector]]**: A dynamic array in C++ that allows for flexible storage and manipulation of data.
- **Ranking Problem**: A problem that involves maintaining and updating a list of ranks based on certain conditions.
- **2D Grid Traversal**: Techniques used to navigate through a two-dimensional array or grid, often utilized in algorithmic challenges.
- **[[dx/dy technique]]**: A method to simplify movement in a grid by using directional arrays to represent changes in coordinates.

## Detailed Technical Breakdown

### Ranking Problem
- **Objective**: Maintain a list of ranks and update them based on input commands.
- **Key Operations**:
  - **Initialization**: Use `iota` to fill the vector with initial ranks.
  - **Input Handling**: Read commands to swap ranks based on conditions.
  - **Output**: Display the final ranking.

#### Sample Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    vector<int> rank(n);
    iota(rank.begin(), rank.end(), 1);
    while (m--) {
        char d1, d2; int T1, T2; cin >> d1 >> T1 >> d2 >> T2; cin.ignore();
        int r1 = find(rank.begin(), rank.end(), T1) - rank.begin();
        int r2 = find(rank.begin(), rank.end(), T2) - rank.begin();
        if (r1 > r2) {
            rank.erase(rank.begin() + r2);
            rank.insert(rank.begin() + r1, T2);
        }
    }
    for (const auto& ri : rank)
        cout << 'T' << ri << ' ';
    cout << '\n';
    return 0;
}
```

### 2D Grid Traversal
- **Objective**: Determine if a sequence of moves returns to the origin in a 2D grid.
- **Key Operations**:
  - **Movement Representation**: Use arrays to represent movement in the x and y directions.
  - **Input Processing**: Iterate through the moves and update coordinates accordingly.

#### Sample Code
```cpp
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        string moveset = "RLUD";
        int dx[] = { 1, -1, 0, 0 };
        int dy[] = { 0, 0, 1, -1 };
        for (const auto& m : moves) {
            int i = (int)moveset.find(m);
            x += dx[i];
            y += dy[i];
        }
        return (x == 0) && (y == 0);
    }
};
```

> [!note] **Important Reminder**: Students are encouraged to review the provided links to visual tools and algorithm analysis notes before the next lecture to ensure a solid understanding of the material.

> [!warning] **Flipped Classroom Reminder**: Make sure to read the specified sections of the algorithm analysis lecture notes to avoid confusion in upcoming classes.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[lec04a]]
- [[lec04b]]
- [[Tutorial+1+Solution]]
- [[Midterm+Briefing]]