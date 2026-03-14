---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Week 7 Lecture Notes

## Overview
In this lecture, we explored the concepts of vector spans and their geometric interpretations in the context of linear algebra. We discussed the relationships between different spans, determined whether certain sets are subspaces, and examined linear independence and dependence among vectors. The lecture also included practical examples and exercises to reinforce these concepts.

## Key Concepts & Definitions
- **Span**: The set of all possible linear combinations of a given set of vectors. For example, span{u1, u2, u3} represents all vectors that can be formed using u1, u2, and u3.
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication.
- **Linear Independence**: A set of vectors is linearly independent if no vector in the set can be expressed as a linear combination of the others.
- **Row Echelon Form (REF)**: A form of a matrix where all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row.

## Detailed Technical Breakdown

### Announcements
- **Quiz**: Attempt quiz 3.5 to 3.7, due on Friday, 6 March 2026.
- **Homework**: Homework 2 published, due Sunday, 22 March 2026.
- **Midterm**: Scheduled for Friday, 13 March 2026, from 1900hrs to 2000hrs at MPSH1. Check Canvas for venue and seat number.

### Vector Span Examples
1. **Example 1**: 
   \[
   \begin{pmatrix}
   2 & -1 & 0 & 1 & 0 \\
   -2 & 1 & 0 & -1 & 1 \\
   0 & -1 & 9 & -5 & 1
   \end{pmatrix} \rightarrow 
   \begin{pmatrix}
   0 & 1 & -9 & 5 & 0 \\
   0 & 0 & 0 & 1 & 0
   \end{pmatrix}
   \]
   - Result: span{v1, v2} ⊆ span{u1, u2, u3}.

2. **Example 2**: 
   \[
   \begin{pmatrix}
   1 & 0 & 2 & -1 & 0 \\
   -1 & 1 & -2 & 1 & 0
   \end{pmatrix} \rightarrow 
   \begin{pmatrix}
   0 & 1 & 0 & 0 & 0
   \end{pmatrix}
   \]
   - Result: span{u1, u2, u3} ⊆ span{v1, v2}.

### Geometric Interpretation
- Both span{u1, u2, u3} and span{v1, v2} represent planes in R³ that intersect along a line through the origin.

### Subspace Determination
- **Question 2**: Determine if the following sets are subspaces:
  - **Set S**: 
    \[
    S = \text{span} \left\{ \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} \right\}
    \]
    - **Conclusion**: S is a subspace as it is closed under addition and scalar multiplication.

## Implementation/Examples
```matlab
% MATLAB code to find the RREF of a matrix
A = [1 0 1; 0 1 2; 0 1 -1];
RREF_A = rref(A);
```

> [!note] **Important**: Always check if the set contains the zero vector, as any set containing the zero vector is linearly dependent.

> [!warning] **Caution**: Ensure to verify the conditions for subspaces, particularly closure under addition and scalar multiplication.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Linear Algebra Concepts]]