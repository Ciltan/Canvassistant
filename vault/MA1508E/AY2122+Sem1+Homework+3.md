---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 3 - Homework Overview

## Overview
This document outlines the essential components of Homework 3 for the MA1508E course at the National University of Singapore. It includes instructions for submission, a series of mathematical problems related to vector spaces, and the requirements for demonstrating understanding of key concepts in linear algebra. The homework emphasizes the importance of clarity in presentation and adherence to academic standards.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. 
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space.
- **Dimension**: The number of vectors in a basis for a vector space, indicating its size.
- **Span**: The set of all possible linear combinations of a given set of vectors.
- **Orthogonal Set**: A set of vectors that are perpendicular to each other.

## Detailed Technical Breakdown

### Submission Instructions
- Write answers on A4 size papers.
- Clearly write your student number and name on the top left corner of each page.
- Include page numbers on the top right corner of each page.
- Submit answers by scanning or photographing your work, merging images into a single PDF named by StudentNo P3 (e.g., A123456Z P3).
- Upload the PDF to the LumiNUS folder for Practice 3 submission.

### Problem Breakdown
1. **Problem 1**: Let \( A = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \) and \( B = \begin{pmatrix} w & x \\ y & z \end{pmatrix} \).
   - **(a)** Show that \( V \) is a subspace by demonstrating it is the solution set to a homogeneous system. [3 marks]
   - **(b)** Find a basis for \( V \) and determine its dimension. [2 marks]
   - **(c)** Let \( S = \left\{ \begin{pmatrix} -2 \\ 2 \\ -1 \end{pmatrix}, \begin{pmatrix} -4 \\ 4 \\ -5 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ 4 \end{pmatrix} \right\} \). Show that \( \text{span}(S) \subseteq V \) and determine if \( S \) is a basis for \( V \). [3 marks]

2. **Problem 2**: Let \( V = \text{span}(S) \), where \( S = \left\{ \begin{pmatrix} -2 \\ 3 \\ 1 \end{pmatrix}, \begin{pmatrix} 1 \\ 1 \\ -2 \end{pmatrix}, \begin{pmatrix} 3 \\ 0 \\ -2 \end{pmatrix} \right\} \).
   - **(a)** Show that \( S \) is a basis for \( V \). [2 marks]
   - **(b)** Show that \( T = \left\{ \begin{pmatrix} 0 \\ 1 \\ -7 \end{pmatrix}, \begin{pmatrix} 3 \\ -2 \\ -3 \end{pmatrix}, \begin{pmatrix} 1 \\ -1 \\ -5 \end{pmatrix} \right\} \) is also a basis for \( V \). [3 marks]
   - **(c)** Let \( v_1 = \begin{pmatrix} -2 \\ 6 \\ 1 \end{pmatrix} \) and \( v_2 = \begin{pmatrix} 7 \\ 2 \\ 3 \end{pmatrix} \). Determine if \( v_i \) belongs to \( V \) and find \( (v_i)^T \) for those that do. [3 marks]

3. **Problem 3**: Let \( v_1 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, v_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}, v_3 = \begin{pmatrix} 0 \\ -1 \\ -1 \end{pmatrix} \).
   - **(a)** Check if \( \{v_1, v_2, v_3\} \) is an orthogonal set. [2 marks]
   - **(b)** Determine if \( \{v_1, v_2, v_3\} \) is orthonormal. If not, normalize it if possible. [2 marks]

## Implementation/Examples
```plaintext
# Example of checking orthogonality
v1 = [0, 1, 0]
v2 = [1, 1, 1]
v3 = [0, -1, -1]

# Check dot products
dot_product_v1_v2 = np.dot(v1, v2)
dot_product_v1_v3 = np.dot(v1, v3)
dot_product_v2_v3 = np.dot(v2, v3)
```

> [!note] Ensure all calculations are shown clearly in your answer scripts to receive full credit.
> [!important] Remember to check the dimensions of your vector spaces when determining bases and spans.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[MA1508E+AY2122Sem1]]
- [[Determinants]]
- [[Stacks and Queues]]
- [[Logic - Propositional Logic]]