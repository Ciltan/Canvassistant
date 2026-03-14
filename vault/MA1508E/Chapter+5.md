---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 5: Orthogonality, Projection, and Least Square Solution

## Overview
This chapter delves into the concepts of [[orthogonality]], [[projection]], and the [[least square solution]] in the context of linear algebra. It begins with the definition of orthogonal vectors and extends to orthogonal and orthonormal sets, exploring their properties and implications. The chapter also discusses the orthogonal projection of vectors onto subspaces and the significance of orthogonal complements in vector spaces.

## Key Concepts & Definitions
- **Orthogonality**: Two vectors \( u \) and \( v \) in \( \mathbb{R}^n \) are orthogonal if their inner product \( u \cdot v = 0 \).
- **Inner Product**: The inner product of vectors \( u \) and \( v \) is defined as \( u \cdot v = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n \).
- **Norm**: The norm of a vector \( u \) is given by \( \|u\| = \sqrt{u \cdot u} \).
- **Angle Between Vectors**: The angle \( \theta \) between nonzero vectors \( u \) and \( v \) is given by \( \theta = \cos^{-1} \left( \frac{u \cdot v}{\|u\| \|v\|} \right) \).
- **Orthonormal Set**: A set \( S = \{v_1, v_2, \ldots, v_k\} \) is orthonormal if \( v_i \cdot v_j = 0 \) for \( i \neq j \) and \( v_i \cdot v_i = 1 \).
- **Orthogonal Complement**: The orthogonal complement of a subspace \( V \) is the set of all vectors that are orthogonal to every vector in \( V \), denoted as \( V^\perp \).

## Detailed Technical Breakdown

### 5.1 Orthogonality
- **Definition**: Two vectors \( u, v \in \mathbb{R}^n \) are orthogonal if \( u \cdot v = 0 \).
- **Cases**:
  - Case 1: Either \( u = 0 \) or \( v = 0 \).
  - Case 2: If both are non-zero, then \( \theta = \pi \), indicating they are perpendicular.

#### Examples
1. \( \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \cdot \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} = 0 \)
2. \( \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \cdot \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = 0 \)

### 5.2 Orthogonal and Orthonormal Sets
- **Orthogonal Set**: A set \( S \) is orthogonal if \( v_i \cdot v_j = 0 \) for all \( i \neq j \).
- **Orthonormal Set**: A set \( S \) is orthonormal if it is orthogonal and each vector has unit length.

#### Example Analysis
- **Set S**: \( \{ \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} \} \) is orthonormal.

### 5.3 Orthogonal Projection
- **Orthogonal Projection Theorem**: Every vector \( w \) in \( \mathbb{R}^n \) can be decomposed uniquely as \( w = w_p + w_n \), where \( w_p \) is in \( V \) and \( w_n \) is orthogonal to \( V \).

#### Example
Let \( V \) be defined by \( z = 0 \) in \( \mathbb{R}^3 \) and \( w = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \). The projection \( w_p \) onto \( V \) can be calculated as:
```plaintext
w_p = (w \cdot v_1)v_1 + (w \cdot v_2)v_2
```

> [!note] **Key Insight**: The orthogonal projection is independent of the choice of orthonormal basis for the subspace.

> [!important] **Theorem**: The orthogonal complement of a subspace \( V \) is the nullspace of the matrix formed by the spanning set of \( V \).

## Related
- [[Chapter+4+How+Designers+Think]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]
- [[Logic - Propositional Logic]]