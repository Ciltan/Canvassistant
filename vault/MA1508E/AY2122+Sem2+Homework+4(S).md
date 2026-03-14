---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 4 - Solutions Overview

## Overview
This note summarizes key solutions and methodologies from the MA1508E course, focusing on linear algebra concepts such as orthonormal bases, projections, diagonalization, and eigenvalues. The material includes detailed calculations and examples that illustrate the application of these concepts in engineering contexts. The solutions provided are essential for understanding the theoretical underpinnings and practical applications of linear algebra.

## Key Concepts & Definitions
- **Orthonormal Basis**: A set of vectors that are both orthogonal and normalized. 
- **Projection**: The process of mapping a vector onto a subspace.
- **Diagonalization**: The process of finding a diagonal matrix that is similar to a given matrix.
- **Eigenvalues and Eigenvectors**: Scalars and vectors associated with a linear transformation that describe the scaling factor and direction of transformation, respectively.
- **RREF (Reduced Row Echelon Form)**: A form of a matrix that simplifies solving linear equations.

## Detailed Technical Breakdown

### 1. Orthonormal Basis Conversion
- Given set \( S = \{ u_1, u_2, u_3 \} \):
  - \( u_1 = \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}, u_2 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix} \)
- Convert \( S \) into an orthonormal basis for \( V \):
  - Calculate \( v_1, v_2, v_3 \) using the Gram-Schmidt process.

### 2. Projection onto Subspace
- Given vector \( \begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix} \):
  - Projection formula: 
  \[
  \text{proj}_V(\mathbf{b}) = A(A^TA)^{-1}A^T\mathbf{b}
  \]
- Calculate the projection using matrix \( A \).

### 3. Diagonalization of Matrix \( A \)
- Given matrix:
\[
A = \begin{pmatrix} 0.5 & 0.4 & 0.2 \\ 0.4 & 0.5 & 0.2 \\ 0.1 & 0.1 & 0.6 \end{pmatrix}
\]
- Find eigenvalues by solving \( \text{det}(xI - A) = 0 \).
- Compute eigenvectors for each eigenvalue.

### 4. Differential System Solution
- Given system:
\[
\begin{align*}
y_1' &= 3y_1 + y_2 + y_4 \\
y_2' &= y_1 + y_2 + y_3 \\
y_3' &= y_2 + 3y_3 \\
y_4' &= y_1 + y_2 + y_4
\end{align*}
\]
- Use eigenvalues and eigenvectors to solve the system with initial conditions \( y_1(0) = y_2(0) = y_3(0) = y_4(0) = 1 \).

## Implementation/Examples

### Example: Orthonormal Basis Calculation
```markdown
1. Calculate \( v_1 = \frac{u_1}{\|u_1\|} \)
2. Calculate \( v_2 = \frac{u_2 - \text{proj}_{v_1}(u_2)}{\|u_2 - \text{proj}_{v_1}(u_2)\|} \)
3. Calculate \( v_3 = \frac{u_3 - \text{proj}_{v_1}(u_3) - \text{proj}_{v_2}(u_3)}{\|u_3 - \text{proj}_{v_1}(u_3) - \text{proj}_{v_2}(u_3)\|} \)
```

### Example: Projection Calculation
```markdown
Let A = \begin{pmatrix} -1 & 1 & 0 \\ 1 & 0 & 2 \\ 0 & 1 & 2 \end{pmatrix}
Projection = A(A^TA)^{-1}A^T \begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix}
```

> [!note] Ensure all calculations are shown clearly to facilitate understanding.
> [!important] Review eigenvalue problems and their applications in engineering contexts.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Diagonalization]]
- [[Eigenvalues and Eigenvectors]]