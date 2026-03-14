---
tags: [CS1231, lecture-notes, academic]
---

# Alternate Solutions in Chapter 2

## Overview
This note summarizes alternate solutions presented in Chapter 2 of the CS1231 course material. It explores the relationships between sets and their intersections, as well as the implications of various mathematical operations on these sets. The content emphasizes the importance of understanding the properties of sets and their representations on the number line.

## Key Concepts & Definitions
- **Sets**: A collection of distinct objects, considered as an object in its own right. 
- **Intersection**: The set containing all elements that are common to both sets, denoted as \( A \cap B \).
- **Union**: The set containing all elements from both sets, denoted as \( A \cup B \).
- **Inequality**: A mathematical statement that describes the relative size or order of two values.
- **Number Line**: A visual representation of numbers on a straight line, where each point corresponds to a number.

## Detailed Technical Breakdown

### Alternate Solution 1 (Page 2)
- Given sets \( A \) and \( B \):
  - If \( a \in A \) and \( b \in B \), then \( n = 4 \) implies \( a^2 = b^2 \).
  - Squaring both sides leads to \( a = \pm b \).
- Let \( t = a^4 \) and \( t \in \mathbb{Z} \):
  - Then \( t = 1 \) implies \( n \neq 0 \) for all integers \( a \).
  - Thus, \( t - 1 = 0 \) leads to \( A = B \).

### Alternate Solution 2 (Page 6)
1. **Union of Sets**:
   - Let \( U = \mathbb{R} \) and \( A = \{ n \in \mathbb{R} \mid n < 0 \} \), \( B = \{ a \in \mathbb{R} \mid a \geq 0 \} \).
   - The union \( A \cup B \) covers all real numbers:
     - \( A \) covers everything less than 0.
     - \( B \) covers everything greater than or equal to 0.
   - Together, they cover all \( \mathbb{R} \).

2. **Intersection of Sets**:
   - To be in the intersection \( A \cap B \):
     - A number must satisfy conditions from both sets.
     - The only number that satisfies both conditions is \( n = 0 \).
   - Thus, \( A \cap B = \{ 0 \} \).

3. **Set Differences**:
   - For \( B - A \):
     - Since \( B \) contains all \( \mathbb{R} \) that are greater than or equal to 0, it excludes elements in \( A \).
   - Therefore, \( B - A = [0, \infty) \).

> [!note] **Key Takeaway**: Understanding the properties of sets and their operations is crucial for solving problems in set theory and logic.
> 
> [!important] **Important Concept**: The intersection of two sets can yield a single element, demonstrating the unique relationships between different sets.

## Implementation/Examples
```math
A = \{ n \in \mathbb{R} \mid n < 0 \}
B = \{ a \in \mathbb{R} \mid a \geq 0 \}
A \cup B = \mathbb{R}
A \cap B = \{ 0 \}
B - A = [0, \infty)
```

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]