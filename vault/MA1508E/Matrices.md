---
tags: [MA1508E, matrices, matrix_operations, inverse_matrix, LU_decomposition]
---

# Matrices

## Overview

Matrices are rectangular arrays of numbers that provide a powerful framework for representing and solving linear systems. This chapter covers matrix algebra, special matrix types, matrix inverses, and matrix factorisations.

## Basic Definitions

> [!note] Definition: Matrix
> An $m \times n$ **matrix** is a rectangular array of real numbers with $m$ rows and $n$ columns:
> $$A = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{pmatrix}$$
> We write $A = [a_{ij}]_{m \times n}$ where $a_{ij}$ is the entry in row $i$, column $j$.

**Special matrices**:
- **Square matrix**: $m = n$
- **Zero matrix**: All entries are 0, denoted $O$ or $\mathbf{0}$
- **Identity matrix**: $n \times n$ matrix with 1's on the diagonal and 0's elsewhere, denoted $I_n$
- **Diagonal matrix**: Square matrix with $a_{ij} = 0$ for $i \neq j$
- **Upper triangular**: $a_{ij} = 0$ for $i > j$
- **Lower triangular**: $a_{ij} = 0$ for $i < j$
- **Symmetric matrix**: $A^T = A$ (i.e., $a_{ij} = a_{ji}$)
- **Skew-symmetric**: $A^T = -A$

## Matrix Operations

### Addition and Scalar Multiplication

For $m \times n$ matrices $A = [a_{ij}]$ and $B = [b_{ij}]$, and scalar $c$:

$$A + B = [a_{ij} + b_{ij}], \quad cA = [ca_{ij}]$$

> [!warning]
> Matrices must have the **same dimensions** to be added.

### Matrix Multiplication

> [!note] Definition: Matrix Product
> If $A$ is $m \times n$ and $B$ is $n \times p$, then $AB$ is the $m \times p$ matrix whose $(i,j)$-entry is:
> $$(AB)_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj} = a_{i1}b_{1j} + a_{i2}b_{2j} + \cdots + a_{in}b_{nj}$$

Equivalently, column $j$ of $AB$ is $A$ times column $j$ of $B$:
$$A\mathbf{b}_j = A \begin{pmatrix} b_{1j} \\ b_{2j} \\ \vdots \\ b_{nj} \end{pmatrix}$$

### Worked Example

$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}\begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1(5)+2(7) & 1(6)+2(8) \\ 3(5)+4(7) & 3(6)+4(8) \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

> [!warning] Matrix Multiplication Is NOT Commutative
> In general, $AB \neq BA$. Even when both products are defined, they may differ. Also:
> - $AB = O$ does **not** imply $A = O$ or $B = O$.
> - $AB = AC$ does **not** imply $B = C$ (cancellation law fails in general).

### Properties of Matrix Operations

For matrices of compatible sizes and scalars $r, s$:

| Property | Statement |
|---|---|
| Associativity (addition) | $A + (B + C) = (A + B) + C$ |
| Commutativity (addition) | $A + B = B + A$ |
| Additive identity | $A + O = A$ |
| Associativity (multiplication) | $A(BC) = (AB)C$ |
| Left distributive | $A(B + C) = AB + AC$ |
| Right distributive | $(A + B)C = AC + BC$ |
| Scalar compatibility | $r(sA) = (rs)A$ |
| Scalar distributive | $r(A + B) = rA + rB$ |
| Identity | $I_n A = A = A I_n$ |

## Transpose

> [!note] Definition: Transpose
> The **transpose** of an $m \times n$ matrix $A$ is the $n \times m$ matrix $A^T$ obtained by interchanging rows and columns:
> $$(A^T)_{ij} = a_{ji}$$

**Properties of transpose**:
1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(cA)^T = cA^T$
4. $(AB)^T = B^T A^T$ (note the **reversal of order**)

## Matrix–Vector Product and $A\mathbf{x} = \mathbf{b}$

The linear system from [[Systems of Linear Equations]] can be written as:

$$A\mathbf{x} = \mathbf{b}$$

where $A$ is the **coefficient matrix**, $\mathbf{x}$ is the vector of unknowns, and $\mathbf{b}$ is the right-hand side vector.

The product $A\mathbf{x}$ can be viewed as a **linear combination of columns of $A$**:

$$A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n$$

> [!important] Equivalence
> The following statements are equivalent:
> 1. The system $A\mathbf{x} = \mathbf{b}$ has a solution.
> 2. $\mathbf{b}$ is a linear combination of the columns of $A$.
> 3. $\mathbf{b} \in \text{Col}(A)$ (the column space of $A$).

## Inverse of a Matrix

> [!note] Definition: Invertible Matrix
> An $n \times n$ matrix $A$ is **invertible** (or **nonsingular**) if there exists an $n \times n$ matrix $A^{-1}$ such that:
> $$AA^{-1} = A^{-1}A = I_n$$
> If no such matrix exists, $A$ is **singular**.

### Formula for $2 \times 2$ Inverse

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \implies A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

provided $\det(A) = ad - bc \neq 0$.

### Finding $A^{-1}$ by Row Reduction

To find $A^{-1}$, row reduce the augmented matrix $[A \mid I_n]$. If $A$ is invertible, this reduces to $[I_n \mid A^{-1}]$.

### Worked Example

Find the inverse of $A = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$.

$$[A \mid I] = \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1 \end{array}\right] \xrightarrow{R_2 - 3R_1} \left[\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & -3 & 1 \end{array}\right] \xrightarrow{R_1 - 2R_2} \left[\begin{array}{cc|cc} 1 & 0 & 7 & -2 \\ 0 & 1 & -3 & 1 \end{array}\right]$$

$$A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}$$

### Properties of Inverse

1. $(A^{-1})^{-1} = A$
2. $(AB)^{-1} = B^{-1}A^{-1}$ (reversal of order)
3. $(A^T)^{-1} = (A^{-1})^T$
4. $(cA)^{-1} = \frac{1}{c}A^{-1}$ for $c \neq 0$

## The Invertible Matrix Theorem

> [!important] The Invertible Matrix Theorem (IMT)
> Let $A$ be an $n \times n$ matrix. The following are **equivalent**:
> 1. $A$ is invertible.
> 2. $A$ is row equivalent to $I_n$.
> 3. $A$ has $n$ pivot positions.
> 4. $A\mathbf{x} = \mathbf{0}$ has only the trivial solution.
> 5. The columns of $A$ are linearly independent.
> 6. $A\mathbf{x} = \mathbf{b}$ has a unique solution for every $\mathbf{b} \in \mathbb{R}^n$.
> 7. The columns of $A$ span $\mathbb{R}^n$.
> 8. There exists $C$ such that $CA = I_n$.
> 9. There exists $D$ such that $AD = I_n$.
> 10. $A^T$ is invertible.
> 11. $\det(A) \neq 0$.
> 12. $\text{Col}(A) = \mathbb{R}^n$.
> 13. $\text{Nul}(A) = \{\mathbf{0}\}$.
> 14. $\text{rank}(A) = n$.
> 15. The eigenvalues of $A$ are all nonzero.

## Elementary Matrices

> [!note] Definition: Elementary Matrix
> An **elementary matrix** $E$ is a matrix obtained by performing a single elementary row operation on $I_n$.

Key property: Performing an elementary row operation on $A$ is the same as multiplying $A$ on the left by the corresponding elementary matrix.

Every invertible matrix can be written as a product of elementary matrices:
$$A = E_1 E_2 \cdots E_k$$

## LU Decomposition

> [!note] Definition: LU Factorisation
> An $m \times n$ matrix $A$ has an **LU factorisation** if $A = LU$ where:
> - $L$ is an $m \times m$ lower triangular matrix with 1's on the diagonal (unit lower triangular)
> - $U$ is an $m \times n$ matrix in row echelon form

An LU factorisation exists when $A$ can be reduced to REF using only row replacement operations (no row interchanges).

### Solving $A\mathbf{x} = \mathbf{b}$ via LU

1. **Forward substitution**: Solve $L\mathbf{y} = \mathbf{b}$ for $\mathbf{y}$.
2. **Back substitution**: Solve $U\mathbf{x} = \mathbf{y}$ for $\mathbf{x}$.

This is efficient when solving $A\mathbf{x} = \mathbf{b}$ for multiple right-hand sides $\mathbf{b}$, since $L$ and $U$ only need to be computed once.

### Worked Example

$$A = \begin{pmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{pmatrix}$$

Row reduce (recording multipliers):
- $R_2 - 2R_1$: multiplier $= 2$
- $R_3 - 4R_1$: multiplier $= 4$
- $R_3 - 3R_2$: multiplier $= 3$

$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{pmatrix}$$

## Related Notes

- [[Systems of Linear Equations]] - Solving systems via row reduction
- [[Determinants]] - Determinant as a test for invertibility
- [[Vector Spaces]] - Column space and null space of a matrix
- [[Eigenvalues and Eigenvectors]] - Matrix diagonalisation
