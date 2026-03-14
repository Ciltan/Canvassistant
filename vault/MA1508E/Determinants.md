---
tags: [MA1508E, determinants, cofactor_expansion, cramers_rule]
---

# Determinants

## Overview

The determinant is a scalar value associated with every square matrix. It encodes fundamental information about the matrix: whether it is invertible, how it scales volumes, and it provides formulas for inverses and solutions of linear systems.

## Definition

### $2 \times 2$ Determinant

$$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$

### $3 \times 3$ Determinant (Sarrus' Rule)

For a $3 \times 3$ matrix, the determinant can be computed by repeating the first two columns and taking diagonal products:

$$\det\begin{pmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{pmatrix} = a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{12}a_{21}a_{33} - a_{11}a_{23}a_{32}$$

> [!warning]
> Sarrus' rule only works for $3 \times 3$ matrices. Do **not** attempt to generalise it to larger matrices.

## Cofactor Expansion

> [!note] Definition: Minor and Cofactor
> The $(i,j)$-**minor** $M_{ij}$ is the determinant of the submatrix obtained by deleting row $i$ and column $j$.
>
> The $(i,j)$-**cofactor** is:
> $$C_{ij} = (-1)^{i+j} M_{ij}$$

> [!note] Definition: Cofactor Expansion
> The determinant of an $n \times n$ matrix $A$ can be computed by expanding along any row $i$ or column $j$:
>
> **Along row $i$:**
> $$\det(A) = \sum_{j=1}^{n} a_{ij} C_{ij} = a_{i1}C_{i1} + a_{i2}C_{i2} + \cdots + a_{in}C_{in}$$
>
> **Along column $j$:**
> $$\det(A) = \sum_{i=1}^{n} a_{ij} C_{ij} = a_{1j}C_{1j} + a_{2j}C_{2j} + \cdots + a_{nj}C_{nj}$$

> [!important] Strategy
> Always expand along the row or column with the **most zeros** to minimise computation.

### Worked Example

Compute $\det(A)$ where $A = \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 0 \\ 0 & 4 & 5 \end{pmatrix}$.

Expand along row 1 (has a zero):

$$\det(A) = 1 \cdot C_{11} + 0 \cdot C_{12} + 2 \cdot C_{13}$$

$$= 1 \cdot (+1)\det\begin{pmatrix} 1 & 0 \\ 4 & 5 \end{pmatrix} + 2 \cdot (+1)\det\begin{pmatrix} 3 & 1 \\ 0 & 4 \end{pmatrix}$$

$$= 1(5 - 0) + 2(12 - 0) = 5 + 24 = 29$$

## Properties of Determinants

> [!important] Key Properties
> Let $A$ and $B$ be $n \times n$ matrices.
>
> **Row operation effects:**
> 1. Swapping two rows **negates** the determinant: $\det(E_{ij}A) = -\det(A)$
> 2. Multiplying a row by $k$ **multiplies** the determinant by $k$: $\det(kR_i) = k\det(A)$
> 3. Adding a multiple of one row to another **does not change** the determinant.
>
> **Algebraic properties:**
> 4. $\det(AB) = \det(A)\det(B)$
> 5. $\det(A^T) = \det(A)$
> 6. $\det(A^{-1}) = \frac{1}{\det(A)}$ (when $A$ is invertible)
> 7. $\det(cA) = c^n \det(A)$ for an $n \times n$ matrix
> 8. $\det(I_n) = 1$
>
> **Triangular matrices:**
> 9. If $A$ is triangular (upper or lower), then $\det(A)$ is the product of diagonal entries.

> [!warning] Common Mistakes
> - $\det(A + B) \neq \det(A) + \det(B)$ in general!
> - $\det(cA) = c^n \det(A)$, not $c\det(A)$.

## Computing Determinants via Row Reduction

A practical method for large matrices:

1. Row reduce $A$ to an upper triangular matrix $U$, tracking row swaps and scalings.
2. $\det(A) = (-1)^s \cdot \frac{1}{\text{(product of scaling factors)}} \cdot \prod_{i} u_{ii}$

where $s$ is the number of row swaps.

### Worked Example

$$A = \begin{pmatrix} 2 & 4 & 6 \\ 1 & 3 & 1 \\ 0 & 1 & 2 \end{pmatrix}$$

$R_1 \leftrightarrow R_2$ (one swap, so sign flips):
$$\begin{pmatrix} 1 & 3 & 1 \\ 2 & 4 & 6 \\ 0 & 1 & 2 \end{pmatrix}$$

$R_2 - 2R_1 \to R_2$:
$$\begin{pmatrix} 1 & 3 & 1 \\ 0 & -2 & 4 \\ 0 & 1 & 2 \end{pmatrix}$$

$R_3 + \frac{1}{2}R_2 \to R_3$:
$$\begin{pmatrix} 1 & 3 & 1 \\ 0 & -2 & 4 \\ 0 & 0 & 4 \end{pmatrix}$$

$\det(A) = (-1)^1 \cdot (1)(-2)(4) = -(-8) = 8$

## Adjugate Matrix and Inverse Formula

> [!note] Definition: Adjugate (Classical Adjoint)
> The **adjugate** of $A$ is the transpose of the cofactor matrix:
> $$\text{adj}(A) = [C_{ij}]^T$$

> [!important] Inverse via Adjugate
> If $A$ is invertible:
> $$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

### Worked Example ($2 \times 2$)

$$A = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}, \quad \det(A) = 6 - 5 = 1$$

$$\text{adj}(A) = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}, \quad A^{-1} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$$

## Cramer's Rule

> [!note] Theorem: Cramer's Rule
> Let $A$ be an invertible $n \times n$ matrix. The unique solution of $A\mathbf{x} = \mathbf{b}$ is:
> $$x_i = \frac{\det(A_i(\mathbf{b}))}{\det(A)}, \quad i = 1, 2, \ldots, n$$
> where $A_i(\mathbf{b})$ is the matrix obtained by replacing column $i$ of $A$ with $\mathbf{b}$.

### Worked Example

Solve using Cramer's rule:
$$\begin{cases} 2x_1 + x_2 = 5 \\ x_1 + 3x_2 = 7 \end{cases}$$

$$\det(A) = \det\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix} = 5$$

$$x_1 = \frac{\det\begin{pmatrix} 5 & 1 \\ 7 & 3 \end{pmatrix}}{5} = \frac{15 - 7}{5} = \frac{8}{5}$$

$$x_2 = \frac{\det\begin{pmatrix} 2 & 5 \\ 1 & 7 \end{pmatrix}}{5} = \frac{14 - 5}{5} = \frac{9}{5}$$

> [!warning]
> Cramer's rule is theoretically elegant but computationally expensive for large systems. Use Gaussian elimination for practical computation.

## Geometric Interpretation

For a $2 \times 2$ matrix $A = [\mathbf{a}_1 \ \mathbf{a}_2]$, $|\det(A)|$ equals the **area** of the parallelogram spanned by $\mathbf{a}_1$ and $\mathbf{a}_2$.

For a $3 \times 3$ matrix $A = [\mathbf{a}_1 \ \mathbf{a}_2 \ \mathbf{a}_3]$, $|\det(A)|$ equals the **volume** of the parallelepiped spanned by the three column vectors.

The sign of $\det(A)$ indicates orientation (positive = same orientation as standard basis).

## Related Notes

- [[Systems of Linear Equations]] - Solving systems that Cramer's rule addresses
- [[Matrices]] - The Invertible Matrix Theorem uses $\det(A) \neq 0$
- [[Eigenvalues and Eigenvectors]] - Characteristic polynomial uses determinants
- [[Vector Spaces]] - Determinant relates to volume and dimension
