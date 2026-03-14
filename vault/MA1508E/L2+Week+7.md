---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Week 7 Lecture Notes

## Overview
This lecture focuses on the concepts of linear spans and subspaces within the context of linear algebra. Key topics include determining the relationships between spans of vectors, geometric interpretations of spans, and the identification of subspaces. The lecture also covers practical examples and exercises to reinforce understanding.

## Key Concepts & Definitions
- **Span**: The set of all possible linear combinations of a given set of vectors. For example, span{u1, u2, u3} represents all vectors that can be formed by linear combinations of vectors u1, u2, and u3.
- **Subspace**: A subset of a vector space that is itself a vector space under the same operations. A set is a subspace if it contains the zero vector, is closed under vector addition, and is closed under scalar multiplication.
- **RREF (Reduced Row Echelon Form)**: A form of a matrix that simplifies the process of solving linear equations and determining the span of vectors.

## Detailed Technical Breakdown

### Announcements
- **Quiz**: Attempt quiz 3.5 to 3.7, due on Friday, 6 March 2026.
- **Homework**: Homework 2 published, due Sunday, 22 March 2026.
- **Midterm**: Scheduled for Friday, 13 March 2026, from 1900hrs to 2000hrs at MPSH1. Check Canvas for venue and seat number.

### Example Problems
1. **Determining Span Relationships**
   - Given vectors:
     - \( u_1 = \begin{pmatrix} 2 \\ -2 \\ 0 \end{pmatrix}, u_2 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \)
     - \( v_1 = \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, v_2 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \)
   - Determine if \( \text{span}\{u_1, u_2, u_3\} \subseteq \text{span}\{v_1, v_2\} \) and vice versa.

   > [!note] **Key Insight**: The spans can be visualized geometrically as planes in \( \mathbb{R}^3 \) that may intersect along a line.

2. **Geometric Interpretation of Spans**
   - If \( \text{span}\{u_1, u_2, u_3\} \) is a plane, find the equation of the plane in the form \( ax + by + cz = 0 \).
   - Example solution:
     - Substitute points into the equation to derive coefficients \( a, b, c \).

### Implementation/Examples
```matlab
% Example MATLAB code to find RREF
A = [2 -1 0 1 0; -2 1 0 -1 1; 0 -1 9 -5 1];
RREF_A = rref(A);
```

## Related
- For further reading, refer to [[Determinants]], [[Stacks and Queues]], and [[Matlab for Engineering]] for applications of linear algebra concepts in engineering contexts.