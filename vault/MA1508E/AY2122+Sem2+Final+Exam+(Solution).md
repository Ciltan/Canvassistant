---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering (Semester 2 : AY2021/2022)

## Overview
This document outlines the key concepts and solutions from the MA1508E final examination, focusing on linear algebra principles applied in engineering contexts. The exam consists of four questions covering topics such as vector spaces, eigenvalues, and differential equations. Each question is designed to assess the understanding and application of linear algebra techniques.

## Key Concepts & Definitions
- **Vector Space**: A collection of vectors that can be added together and multiplied by scalars.
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space.
- **Dimension**: The number of vectors in a basis for a vector space.
- **Eigenvalue**: A scalar associated with a linear transformation represented by a matrix, indicating how much a corresponding eigenvector is stretched or compressed.
- **Generalized Eigenvector**: A vector that satisfies the equation \((A - \lambda I)^k v = 0\) for some integer \(k > 1\).
- **Projection**: The operation of projecting a vector onto a subspace.

## Detailed Technical Breakdown

### Question 1: Vector Spaces and Basis
1. **Given Set**: 
   \[
   S = \begin{bmatrix}
   -4 & 0 & 2 & -3 & 1 & 1 & 1 \\
   2 & 0 & -1 & 3 & 4 & 7 & -2 \\
   4 & 1 & -2 & 2 & 3 & 5 & -2 \\
   6 & 1 & -3 & 2 & -2 & -3 & -1
   \end{bmatrix}
   \]
   - **Find Basis**: Identify a subset \(S' \subset S\) that forms a basis for \(V\) and determine the dimension of \(V\).
   - **RREF**: The reduced row echelon form (RREF) indicates the pivot columns, leading to the basis vectors.

2. **Basis Verification**:
   - **Set \(T\)**: Show that \(T\) is a basis for \(V\) by checking linear independence and spanning properties.

3. **Projection**:
   - **Projection of \(w\)**: Calculate the projection of a vector \(w\) onto the subspace \(V\) using the formula:
   \[
   p = A(A^TA)^{-1}A^Tw
   \]

### Question 2: Markov Chains
1. **Transition Matrix**:
   - Define the transition matrix \(A\) based on the probabilities of broadcasting messages.
   \[
   A = \begin{bmatrix}
   0.3 & 0.3 & 0.4 \\
   0.3 & 0.3 & 0.4 \\
   0.4 & 0.4 & 0.2
   \end{bmatrix}
   \]

2. **Eigenvalues and Eigenvectors**:
   - Calculate the eigenvalues and eigenvectors of \(A\) to analyze long-term behavior.

3. **Long-term Probabilities**:
   - Determine the steady-state probabilities as \(n \to \infty\).

### Question 3: Differential Systems
1. **Eigenvalue Problem**:
   - Show that \(\lambda = 1\) is a repeated eigenvalue and find associated eigenvectors.

2. **Fundamental Set of Solutions**:
   - Construct a fundamental set of solutions for the differential system using the eigenvalues and eigenvectors.

### Question 4: Matrix Inverses
1. **Conditions for Left Inverse**:
   - Determine conditions on \(a\) and \(b\) such that the matrix \(A\) has a left inverse.

2. **General Solution**:
   - Write down the general solution for the system based on the conditions derived.

## Implementation/Examples
```matlab
% MATLAB code for calculating the projection of w onto V
A = [ ... ]; % Define matrix A based on basis vectors
w = [ ... ]; % Define vector w
p = A * (A' * A)^{-1} * A' * w; % Projection calculation
```

> [!note] **Important**: Ensure to systematically lay out all steps in calculations during examinations.
> [!warning] **Caution**: Always verify the consistency of systems before concluding about the existence of solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]