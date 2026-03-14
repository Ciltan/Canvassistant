---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 5 Solutions

## Overview
This note summarizes the solutions to Tutorial 5 for the MA1508E course, focusing on concepts of linear spans, subspaces, linear independence, and the geometric interpretation of vector spaces. The tutorial explores the relationships between different spans and their geometric representations, as well as the conditions for subspaces and linear independence.

## Key Concepts & Definitions
- **Span**: The set of all linear combinations of a given set of vectors. For example, span{u1, u2, u3} represents all vectors that can be formed by linear combinations of u1, u2, and u3.
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication.
- **Linear Independence**: A set of vectors is linearly independent if no vector in the set can be expressed as a linear combination of the others.
- **Geometric Interpretation**: The visualization of spans and subspaces in terms of lines, planes, and higher-dimensional analogs in R^n.

## Detailed Technical Breakdown

### Problem 1: Span Relationships
1. **Determine Span Relationships**:
   - For vectors \( u_1, u_2, u_3 \) and \( v_1, v_2 \):
     - **(i)** \( \text{span}\{v_1, v_2\} \not\subseteq \text{span}\{u_1, u_2, u_3\} \)
     - **(ii)** \( \text{span}\{u_1, u_2, u_3\} \not\subseteq \text{span}\{v_1, v_2\} \)

2. **Geometric Description**:
   - Both spans represent planes in R³ that intersect in a line through the origin.

### Problem 2: Subspaces
- **Set S**: 
  - **(a)** \( S = \{ \begin{pmatrix} p \\ q \\ p \\ q \end{pmatrix} \} \) is a subspace, expressed as \( S = \text{span}\{ \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \end{pmatrix} \} \).
  - **(b)** \( S \) is not a subspace since it does not satisfy closure under addition.
  - **(c)** \( S \) is a subspace, expressed as \( S = \text{span}\{ \begin{pmatrix} 4 \\ 3 \\ 0 \\ 0 \end{pmatrix} \} \).
  - **(d)** \( S \) is not a subspace due to the presence of the zero vector.
  - **(e)** \( S \) is a subspace, expressed as \( S = \text{span}\{ \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix} \} \).

### Problem 3: Linear Independence
- **Set S**:
  - **(a)** Linearly dependent since it contains 4 vectors in R³.
  - **(b)** Linearly independent as it contains only two non-multiplicative vectors.
  - **(c)** Linearly dependent due to the zero vector.
  - **(d)** Linearly independent.

### Problem 4: Basis for Subspaces
- **Subspace V**:
  - **(a)** Basis: \( \{ \begin{pmatrix} 1 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \\ 1 \end{pmatrix} \} \).
  - **(b)** Basis: \( \{ \begin{pmatrix} 1 \\ -1 \\ 0 \\ 1 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 3 \\ -1 \end{pmatrix} \} \).

### Problem 5: Linear Combinations
- **Expressing u**:
  - Two distinct ways to express \( u \) as a linear combination of \( v_1, v_2, v_3, v_4 \).

> [!important] The solution set to any homogeneous linear system is a subspace of R^n, containing the trivial solution and closed under linear combinations.

> [!note] If a linear system has two distinct solutions, it must have infinitely many solutions due to the presence of a nontrivial solution to the corresponding homogeneous system.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]