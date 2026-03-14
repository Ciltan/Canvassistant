---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 2

## Overview
This document outlines the requirements and tasks for Homework 2 in the MA1508E Linear Algebra course at the National University of Singapore. It includes instructions for submission, as well as specific mathematical problems related to vector spaces, subspaces, and matrix theory. The homework emphasizes the importance of clear workings and the use of MATLAB for calculations.

## Key Concepts & Definitions
- **Vector Space**: A collection of vectors that can be added together and multiplied by scalars.
- **Subspace**: A subset of a vector space that is itself a vector space.
- **Basis**: A set of linearly independent vectors that span a vector space.
- **Dimension**: The number of vectors in a basis for a vector space.
- **Nullspace**: The set of all vectors that, when multiplied by a matrix, yield the zero vector.
- **Rank**: The dimension of the column space of a matrix.
- **Row Space**: The span of the rows of a matrix.

## Detailed Technical Breakdown

### Submission Instructions
- Write answers on A4 paper or type them digitally.
- Include page numbers on the top right corner.
- Use MATLAB for calculations, showing all workings clearly.
- Submit scanned images or a PDF file named by StudentNo HW2 (e.g., A123456Z HW2.pdf) to Canvas assignments.

### Problem Breakdown
1. **Problem 1**: Given vectors \( u_1, u_2, u_3, u_4 \) in \( \mathbb{R}^5 \):
   - **(a)** Show that \( V \) is a subspace and find a basis for \( V \).
   - **(b)** Determine the dimension of \( U = \text{span}\{u_1, u_2, u_3, u_4\} \).
   - **(c)** Prove that for any vectors \( u \in U \) and \( v \in V \), \( u \cdot v = 0 \).

2. **Problem 2**: For a matrix \( A \):
   - **(a)** Find the rank and nullity of \( A \).
   - **(b)** Write the reduced row echelon form of \( A \).
   - **(c)** Identify which columns of \( A \) form a basis for the column space.
   - **(d)** Find a basis for the row space of \( A \).

3. **Problem 3**: Given a set \( S \) and vectors \( v_1, v_2, v_3 \):
   - **(a)** Find a subset \( B \subseteq S \) that is a basis for \( V \).
   - **(b)** Show that \( T = \{v_1, v_2, v_3\} \) is a basis for \( V \).
   - **(c)** Calculate \( [u_4], [u_5], [u_6] \).

4. **Problem 4**: Given a basis \( S \) for a subspace \( V \):
   - **(a)** Determine \( v_1 \) based on its representation in \( S \).
   - **(b)** Calculate \( [v] \) for \( v = v_1 + v_2 \).
   - **(c)** Find \( [v_3] \) for \( v_3 = 3v_1 \).

## Implementation/Examples
```matlab
% Example MATLAB code for calculating the rank of a matrix A
A = [1 -1 0; 2 0 1; 1 1 1];
rank_A = rank(A);
disp(['Rank of A: ', num2str(rank_A)]);
```

> [!note] **Important Submission Guidelines**: Ensure all images are clear and in order when merging into a PDF. If submitting digitally, verify the PDF format before submission.

> [!warning] **MATLAB Usage**: While MATLAB can assist in calculations, all workings must be shown clearly in your submission to receive full credit.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Stacks and Queues]]