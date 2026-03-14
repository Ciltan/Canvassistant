---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Make-up Midterm Exam Solutions

## Overview
This note provides a comprehensive breakdown of the solutions to the make-up midterm exam for MA1508E, focusing on key concepts in [[Linear Algebra]]. The exam consists of six questions covering systems of equations, matrix theory, and vector spaces. Each question is analyzed in detail, with solutions provided for various scenarios, including inconsistent systems and the determination of bases for vector spaces.

## Key Concepts & Definitions
- **Row Echelon Form (REF)**: A matrix form where all non-zero rows are above any rows of all zeros, and leading coefficients (the first non-zero number from the left) of a non-zero row are to the right of the leading coefficient of the previous row.
- **Reduced Row Echelon Form (RREF)**: A further refinement of REF where each leading coefficient is 1 and is the only non-zero entry in its column.
- **Nullspace**: The set of all vectors x such that Ax = 0 for a given matrix A.
- **Column Space**: The span of the columns of a matrix, representing all possible linear combinations of its columns.
- **Basis**: A set of vectors that are linearly independent and span a vector space.

## Detailed Technical Breakdown

### Question 1: System of Equations
1. **Inconsistent System**: The system is inconsistent if \( a = 1 \) and \( b \neq 0 \).
2. **Unique Solution**: The system has a unique solution if \( a \neq 0, 1 \) with the solution given by:
   - \( x_1 = 0 \)
   - \( x_2 = \frac{a - 2b}{a} \)
   - \( x_3 = \frac{b}{a - 1} \)
   - \( x_4 = 1 \)
3. **Infinitely Many Solutions**:
   - **One Parameter**: If \( a = 0, b \neq 0 \) or \( a = 1, b = 0 \).
   - **Two Parameters**: If \( a = b = 0 \).

### Question 2: Matrix Properties
- **Nullspace Basis**: Derived from RREF, the basis for the nullspace of A is:
  - \( \{ \begin{pmatrix} 1 \\ 2 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \\ 1 \end{pmatrix} \} \)
- **Column Space Basis**: The column space of A is the whole \( \mathbb{R}^3 \) since rank(A) = 3.

### Question 3: Linear Dependence and Nullity
- **Example Matrix**: 
  - \( A = \begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 1 & 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} \)
- **Nullity**: By the rank-nullity theorem, nullity(A) = 1.

### Question 4: Matrix Exponentiation
- **Matrix A**: 
  - \( A = \begin{pmatrix} \alpha & \beta & 0 \\ 0 & 0 & \alpha \\ \end{pmatrix} \)
- **Result**: 
  - \( A^{1508E} = \begin{pmatrix} (\alpha^2 + \beta^2)^{754E} & 0 \\ 0 & (\alpha^2 + \beta^2)^{754E} \end{pmatrix} \)

### Question 5: Subspace Determination
- **Subspace Analysis**:
  - (a) S is a subspace with basis \( \{ e_1, e_2 \} \) and dimension 2.
  - (b) S is not a subspace.
  - (c) S is not a subspace.
  - (d) S is a subspace with dimension 5.
  - (e) S is a subspace with dimension 0.

### Question 6: Linear System Problem
- **System**: 
  - \( x + y + z = 100 \)
  - \( 1x + 4y + 7z = 100 \)
- **Solutions**: 
  - \( x = 40 + t, y = 60 - t, z = t \) for \( t = 0, 5, 10, 15 \).

> [!important] Ensure to review the concepts of [[Row Echelon Form]] and [[Nullspace]] for a deeper understanding of the solutions provided.
> 
> [!note] The solutions to the midterm exam highlight the importance of understanding the properties of matrices and vector spaces in linear algebra.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]