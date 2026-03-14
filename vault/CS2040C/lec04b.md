---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 04b

## Overview
In this lecture, we explored advanced techniques for manipulating [[Linked Lists]], focusing on two specific LeetCode problems: deleting the middle node of a linked list and removing stars from a string. We discussed two distinct approaches for each problem, highlighting the efficiency and complexity of the solutions. Additionally, we addressed important administrative notes regarding upcoming lectures and potential changes in the schedule.

## Key Concepts & Definitions
- **Linked List**: A linear data structure where each element is a separate object, consisting of a node containing data and a reference to the next node.
- **Brute Force**: A straightforward approach to solving a problem by trying all possible solutions.
- **Stack**: A data structure that follows the Last In First Out (LIFO) principle, where the last element added is the first to be removed.
- **Pointer Techniques**: Methods used in programming to manipulate data structures through references.

## Detailed Technical Breakdown

### Deleting the Middle Node of a Linked List
#### Approaches
1. **Count and Delete**:
   - Count the total number of nodes, `n`.
   - If `n` is 1, return `NULL`.
   - For `n ≥ 2`, traverse to the node just before the middle and delete the middle node.

2. **Three Pointer Technique**:
   - Use three pointers: `pre`, `tortoise`, and `hare`.
   - `pre` points to the node before the middle, `tortoise` moves at normal speed, and `hare` moves at double speed.

#### Code Example
```cpp
// Solution 1: Count and Delete
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (head->next == NULL) return NULL;
        ListNode* cur = head;
        int n = 0;
        while (cur != NULL) {
            ++n;
            cur = cur->next;
        }
        cur = head;
        int bef_to_del = n / 2 - 1;
        for (int _ = 0; _ < bef_to_del; ++_)
            cur = cur->next;
        ListNode* to_del = cur->next;
        cur->next = to_del->next;
        delete to_del;
        return head;
    }
};

// Solution 2: Three Pointer Technique
class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* dummy = new ListNode(-1, head);
        ListNode* pre = dummy;
        ListNode *tortoise = head;
        ListNode *hare = head->next;
        while (hare != NULL) {
            pre = pre->next;
            tortoise = tortoise->next;
            hare = hare->next;
            if (hare == NULL) break;
            hare = hare->next;
        }
        pre->next = pre->next->next;
        return dummy->next;
    }
}
```

### Removing Stars from a String
#### Approaches
1. **Brute Force**:
   - Identify the first `*`, delete it along with its preceding character, resulting in O(n²) complexity.

2. **Stack-Based Approach**:
   - Treat `*` as a closing bracket and lowercase characters as opening brackets, allowing for an O(n) solution using a stack.

#### Code Example
```cpp
// Removing Stars from a String
class Solution {
public:
    string removeStars(string s) {
        vector<char> st;
        for (const auto& si : s) {
            if (si == '*')
                st.pop_back();
            else
                st.push_back(si);
        }
        return string(st.begin(), st.end());
    }
};
```

> [!important] **Administrative Notes**: 
> - Dr. Alan Cheng Holun will cover the next lecture if necessary.
> - No tutorials or labs during Week 06 and Recess Week.

> [!note] **Upcoming Events**: 
> - Midterm test scheduled for Tue, 03 Mar 2026.

## Related
- [[lec04a]]
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]