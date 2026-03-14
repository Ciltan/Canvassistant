---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 3 - Solutions Overview

## Overview
This note summarizes the solutions to key problems in the MA1508E course, focusing on the properties of vector spaces, bases, and orthogonality. It provides a structured approach to understanding subspaces, linear independence, and the process of normalization in vector sets. The solutions illustrate the application of linear algebra concepts in engineering contexts.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. [[Subspace]]
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space. [[Basis]]
- **Dimension**: The number of vectors in a basis for a vector space. [[Dimension]]
- **Span**: The set of all possible linear combinations of a given set of vectors. [[Span]]
- **Orthogonal Set**: A set of vectors that are mutually perpendicular. [[Orthogonal Set]]
- **Normalization**: The process of converting a vector into a unit vector. [[Normalization]]

## Detailed Technical Breakdown

### Problem 1: Subspace and Basis
1. **Given**: 
   - Let \( A = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \) and \( B = \begin{pmatrix} w \\ x \\ y \\ z \end{pmatrix} \).
   - Show that \( V = AB = BA \).

2. **(a)** Show that \( V \) is a subspace:
   - To prove \( V \) is a subspace, demonstrate it is the solution set to a homogeneous system:
     - \( x + y = 0 \)
     - \( w + 2x + z = 0 \)
     - \( -w + 2y + z = 0 \)

3. **(b)** Find a basis for \( V \) and its dimension:
   - The basis can be derived from the reduced row echelon form of the coefficient matrix:
     - \( \text{dim}(V) = 2 \)

4. **(c)** Let \( S = \{ \begin{pmatrix} 2 \\ 4 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ 5 \\ 4 \end{pmatrix} \} \):
   - Show that \( \text{span}(S) \subseteq V \) and determine if \( S \) is a basis for \( V \):
     - Since \( S \) contains 3 vectors in a 2-dimensional space, it cannot be linearly independent.

### Problem 2: Basis Verification
1. **Given**: \( S = \{ \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \} \)
   - **(a)** Show that \( S \) is a basis for \( V \):
     - Check linear independence through row reduction.

2. **(b)** Show that \( T = \{ \begin{pmatrix} 0 \\ 3 \\ 1 \end{pmatrix}, \begin{pmatrix} -1 \\ -2 \\ 1 \end{pmatrix}, \begin{pmatrix} -7 \\ -3 \\ -5 \end{pmatrix} \} \) is also a basis for \( V \):
   - Confirm that \( \text{dim}(V) = \text{dim}(S) = \text{dim}(T) = 3 \).

3. **(c)** Determine if \( v_i \) belongs to \( V \):
   - For \( v_1 = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} \) and \( v_2 = \begin{pmatrix} 7 \\ 7 \\ 7 \end{pmatrix} \), check consistency.

### Problem 3: Orthogonality and Normalization
1. **Given**: \( v_1 = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, v_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, v_3 = \begin{pmatrix} 1 \\ 3 \\ 0 \end{pmatrix} \)
   - **(a)** Check orthogonality:
     - \( v_1 \cdot v_2 = 0 \), \( v_1 \cdot v_3 = 0 \), \( v_2 \cdot v_3 = 0 \).

2. **(b)** Normalize the vectors:
   - The set is not orthonormal; normalize to obtain:
     - \( \{ \frac{1}{\sqrt{3}} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \frac{1}{\sqrt{7}} \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \} \).

> [!note] The solutions provided illustrate the application of linear algebra concepts in engineering contexts, emphasizing the importance of understanding vector spaces and their properties.
> 
> [!important] Ensure to practice these concepts through additional problems to solidify understanding and application in real-world scenarios.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]