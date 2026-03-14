---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 2: Sets and Functions

## Overview
This chapter introduces fundamental concepts in set theory, including definitions, operations, and properties of sets. It emphasizes the importance of understanding sets as collections of objects and explores various set operations such as union, intersection, and difference. The chapter also discusses the Cartesian product and power sets, providing a foundation for further studies in functions and relations.

## Key Concepts & Definitions
- **Set**: An unordered collection of objects, known as elements or members. 
  - Notation: \( x \in A \) (x is a member of set A), \( x \notin A \) (x is not a member of set A).
- **Subset**: A set A is a subset of set B if every element of A is also an element of B, denoted \( A \subseteq B \).
- **Proper Subset**: A set A is a proper subset of B if \( A \subseteq B \) and \( A \neq B \), denoted \( A \subset B \).
- **Universal Set**: The set that contains all objects under discussion, denoted by U.
- **Empty Set**: A set with no members, denoted by \( \emptyset \) or \( \{\} \).
- **Singleton Set**: A set with exactly one element.
- **Power Set**: The set of all subsets of a set A, denoted \( P(A) \).
- **Cartesian Product**: The set of all ordered pairs from sets A and B, denoted \( A \times B \).

## Detailed Technical Breakdown

### 2.1 Sets
- **Notation**:
  - \( D = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\} \)
  - Positive odd integers less than 10: \( \{1, 3, 5, 7, 9\} \)

- **Important Sets**:
  - \( \mathbb{R} \): Real numbers
  - \( \mathbb{Q} \): Rational numbers
  - \( \mathbb{Z} \): Integers
  - Positive numbers: \( \mathbb{R}^+ \), Negative numbers: \( \mathbb{R}^- \), Nonnegative numbers: \( \mathbb{R}^* \)

- **Set Equality**:
  - Sets A and B are equal if they have the same members: \( A = B \iff \forall x (x \in A \iff x \in B) \).

### 2.2 Set Operations
- **Union**: \( A \cup B = \{x | x \in A \lor x \in B\} \)
- **Intersection**: \( A \cap B = \{x | x \in A \land x \in B\} \)
- **Difference**: \( B - A = \{x | x \in B \land x \notin A\} \)
- **Complement**: \( A' = U - A = \{x | x \notin A\} \)
- **Disjoint Sets**: Sets A and B are disjoint if \( A \cap B = \emptyset \).

> [!note] **Important Distinction**: 
> - \( 2 \in \{1, 2, 3\} \) is correct, while \( \{2\} \in \{1, 2, 3\} \) is incorrect.

## Implementation/Examples
```markdown
### Example of Set Operations
Let \( U = \mathbb{R} \), \( A = \{x | x \leq 0\} \), \( B = \{x | 0 \leq x < 1\} \).
- Union: \( A \cup B = \{x | x < 1\} = (-\infty, 1) \)
- Intersection: \( A \cap B = \{0\} \)
- Difference: \( B' = \{x | x < 0 \lor x \geq 1\} = (-\infty, 0) \cup [1, \infty) \)
```

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]