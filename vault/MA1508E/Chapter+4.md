---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 4: Subspaces Associated to a Matrix

## Overview
This chapter delves into the fundamental concepts of subspaces associated with matrices, specifically focusing on the [[Column Space]], [[Row Space]], and [[Nullspace]]. It provides definitions, theorems, and examples that illustrate how these subspaces are constructed and their significance in linear algebra. Understanding these concepts is crucial for solving systems of linear equations and analyzing the properties of matrices.

## Key Concepts & Definitions
- **Column Space**: The subspace of [[R^m]] spanned by the columns of a matrix A, denoted as [[Col(A)]].
- **Row Space**: The subspace of [[R^n]] spanned by the rows of a matrix A, denoted as [[Row(A)]].
- **Nullspace**: The solution space to the homogeneous system [[Ax=0]], denoted as [[Null(A)]].
- **Rank**: The dimension of the column space or row space of a matrix, denoted as [[rank(A)]].
- **Nullity**: The dimension of the nullspace of a matrix, denoted as [[nullity(A)]].

## Detailed Technical Breakdown

### 4.1 Column Space, Row Space, and Nullspace
- **Definitions**:
  - Let \( A \) be an \( m \times n \) matrix:
    \[
    A = \begin{pmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m1} & a_{m2} & \cdots & a_{mn}
    \end{pmatrix}
    \]
  - **Row Space**:
    \[
    \text{Row}(A) = \text{span}\{ \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \end{pmatrix}, \begin{pmatrix} a_{21} & a_{22} & \cdots & a_{2n} \end{pmatrix}, \ldots, \begin{pmatrix} a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix} \}
    \]
  - **Column Space**:
    \[
    \text{Col}(A) = \text{span}\{ \begin{pmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{pmatrix}, \begin{pmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{pmatrix}, \ldots, \begin{pmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{pmatrix} \}
    \]

### 4.2 Finding Basis for Row Space
- **Theorem**: If a matrix \( R \) is in reduced row-echelon form, then the nonzero rows of \( R \) form a basis for its row space.
- **Proof Sketch**:
  - Each nonzero row has a leading 1, which is the only nonzero entry in that column, ensuring linear independence.

### 4.3 Rank-Nullity Theorem
- **Theorem**: For any matrix \( A \), the sum of its rank and nullity equals the number of columns:
  \[
  \text{rank}(A) + \text{nullity}(A) = n
  \]

## Implementation/Examples
### Example 1: Column and Row Space
Let \( A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 0 \\ 1 & 1 & 2 \end{pmatrix} \).
```plaintext
Col(A) = span{(1, 0, 1), (0, 1, 1), (2, 0, 2)}
Row(A) = span{(1, 0, 2), (0, 1, 0), (1, 1, 2)}
```

### Example 2: Nullspace
Let \( A = \begin{pmatrix} 2 & 1 & 4 \\ 4 & 2 & 2 \\ 2 & 1 & -2 \end{pmatrix} \).
```plaintext
Null(A) = { x ∈ R^3 | Ax = 0 }
```

> [!note] **Key Insight**: The row operations do not change the row space of a matrix, which is crucial for understanding the equivalence of matrices in linear algebra.

> [!important] **Important Theorem**: The rank of a matrix is invariant under transpose, meaning \( \text{rank}(A) = \text{rank}(A^T) \).

## Related
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]
- [[Logic - Propositional Logic]]
- [[Chapter+2]]