---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 8

## Overview
This tutorial focuses on key concepts in linear algebra, particularly the computation of inner products, orthogonal complements, and the Gram-Schmidt process. It explores the properties of vector spaces, including linear independence and orthonormality, while applying MATLAB for practical computations. The exercises illustrate the fundamental theorem that every vector can be expressed as a sum of components in a subspace and its orthogonal complement.

## Key Concepts & Definitions
- **Inner Product**: The operation that takes two vectors and returns a scalar, denoted as \( v \cdot w \).
- **Orthogonal Complement**: For a subspace \( W \) of \( \mathbb{R}^n \), the orthogonal complement \( W^\perp \) is defined as \( W^\perp := \{ v \in \mathbb{R}^n \mid v \cdot w = 0 \text{ for all } w \in W \} \).
- **Linear Independence**: A set of vectors is linearly independent if no vector can be expressed as a linear combination of the others.
- **Orthonormal Set**: A set of vectors that are both orthogonal and normalized (unit length).
- **Gram-Schmidt Process**: A method for orthonormalizing a set of vectors in an inner product space.

## Detailed Technical Breakdown

### 1. MATLAB Computations
- **Vectors**: Let \( v_1 = \begin{pmatrix} 1 \\ 1 \\ -1 \\ 1 \end{pmatrix} \), \( v_2 = \begin{pmatrix} 2 \\ 0 \\ 1 \\ 0 \end{pmatrix} \).
- **Inner Products**:
  - Compute \( v_1 \cdot v_1 \), \( v_1 \cdot v_2 \), \( v_2 \cdot v_1 \), and \( v_2 \cdot v_2 \).
  
- **Matrix \( V \)**:
  - Form \( V = [v_1, v_2] \).
  - Compute \( V^T V \) and interpret its entries.

### 2. Orthogonal Complements
- **Subspace \( W \)**: Let \( W = \text{span}\{w_1, w_2, w_3\} \) where:
  - \( w_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \\ 1 \end{pmatrix} \)
  - \( w_2 = \begin{pmatrix} 1 \\ 2 \\ -1 \\ -2 \end{pmatrix} \)
  - \( w_3 = \begin{pmatrix} 1 \\ -1 \\ 1 \\ 0 \end{pmatrix} \)

- **Properties**:
  - Show that \( S = \{w_1, w_2, w_3\} \) is linearly independent.
  - Show that \( S \) is orthogonal.
  - Prove \( W^\perp \) is a subspace of \( \mathbb{R}^5 \) and determine its dimension.

### 3. Orthonormal Sets
- Normalize \( w_1, w_2, w_3 \) to obtain an orthonormal set \( T \).
- **Projection**: Given \( v = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \), find the projection of \( v \) onto \( W \).

> [!note] **Key Insight**: Every vector \( v \) in \( \mathbb{R}^5 \) can be expressed as \( v = v_W + v_{W^\perp} \), where \( v_W \in W \) and \( v_{W^\perp} \in W^\perp \).

### 4. Gram-Schmidt Process
- Apply the Gram-Schmidt process to convert a given set of vectors into an orthonormal basis for \( \mathbb{R}^4 \).

### 5. Linear Systems
- **Matrix \( A \)**: Given \( A = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 1 & 1 & 1 & 1 \end{pmatrix} \) and \( b = \begin{pmatrix} -1 \\ 1 \end{pmatrix} \).
- Show that the system \( Ax = b \) is inconsistent.
- Find a least squares solution and compute the projection of \( b \) onto the column space of \( A \).

> [!important] **Important Note**: A matrix \( A \) is orthogonal if \( A^T = A^{-1} \). This implies that the columns of \( A \) form an orthonormal basis for \( \mathbb{R}^n \).

## Implementation/Examples
```matlab
% MATLAB code for inner product computation
v1 = [1; 1; -1; 1];
v2 = [2; 0; 1; 0];
inner_product_v1_v1 = v1' * v1;
inner_product_v1_v2 = v1' * v2;
V = [v1, v2];
VTV = V' * V;
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Gram-Schmidt Process]]
- [[Linear Independence]]
- [[Orthonormal Sets]]