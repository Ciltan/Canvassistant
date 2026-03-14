---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 5: Counting

## Overview
This chapter introduces fundamental concepts in counting, essential for understanding combinatorial problems. It covers the Product Rule, Sum Rule, and Difference Rule, providing a framework for calculating the number of ways to perform operations and select items. Through various examples, the chapter illustrates how these rules apply to real-world scenarios, such as labeling seats and creating passwords.

## Key Concepts & Definitions
- **Product Rule**: If an operation can be broken down into a sequence of steps, the total number of ways to perform the operation is the product of the number of ways to perform each step. 
- **Sum Rule**: If there are two properties with no overlap, the total number of objects is the sum of the objects with each property.
- **Difference Rule**: If there are objects with two properties, the number of objects with one property but not the other is the difference between the total objects with both properties and those with the second property.
- **Inclusion/Exclusion Principle**: A method for counting the number of elements in the union of multiple sets, accounting for overlaps.

## Detailed Technical Breakdown

### 5.1 Basics

#### Product Rule
- **Definition**: If the first step can be done in \( r \) ways and the second step can be done in \( s \) ways, then the total number of ways to perform the operation is \( rs \).
- **Example**: Labeling auditorium chairs with a letter (26 options) and a number (100 options):
  - Total labels = \( 26 \times 100 = 2600 \).

#### Sum Rule
- **Definition**: If there are \( m \) objects with property 1 and \( n \) objects with property 2, and no overlap, then the total is \( m + n \).
- **Example**: Counting n-letter passwords:
  - For \( n = 1 \): 26 passwords.
  - For \( n = 2 \): \( 26^2 = 676 \) passwords.
  - For \( n = 3 \): \( 26^3 = 17576 \) passwords.
  - Total = \( 26 + 676 + 17576 = 18278 \).

#### Difference Rule
- **Definition**: If there are \( m \) objects with property 1 and \( n \) objects with property 2, the number of objects with property 1 but not property 2 is \( m - n \).
- **Example**: Counting 4-character PINs:
  - Total PINs = \( (26 + 10)^4 = 1,679,616 \).
  - Distinct character PINs = \( 36 \times 35 \times 34 \times 33 = 1,413,720 \).
  - PINs with repeated characters = \( 1,679,616 - 1,413,720 = 265,896 \).

### Inclusion/Exclusion Principle
- **Definition**: For finite sets \( A, B, C \):
  - \( |A \cup B| = |A| + |B| - |A \cap B| \)
  - \( |A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C| \)

## Implementation/Examples
```plaintext
# Example of counting functions
Let A have m elements and B have n elements.
- Total functions from A to B: \( n^m \)
- 1-1 functions from A to B (if \( n \geq m \)): \( n(n-1)(n-2)...(n-m+1) \)
```

> [!note] The Product Rule is foundational in combinatorics and is widely applicable in various fields, including computer science and operations research.

> [!important] Always ensure that the conditions for applying the Sum and Difference Rules are met, particularly regarding overlaps between sets.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]