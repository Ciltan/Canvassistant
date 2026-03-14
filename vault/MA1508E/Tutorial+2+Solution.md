---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 2 Solutions

## Overview
This note summarizes the solutions to Tutorial 2 for the MA1508E course, focusing on key concepts in linear algebra, including the properties of nilpotent matrices, reduced row-echelon forms, polynomial interpolation, and applications in electrical networks. The solutions provided illustrate the application of theoretical concepts through practical examples and MATLAB implementations.

## Key Concepts & Definitions
- **Nilpotent Matrix**: A square matrix \( A \) is nilpotent if there exists a positive integer \( n \) such that \( A^n = 0 \).
- **Invertible Matrix**: A matrix \( B \) is invertible if there exists a matrix \( C \) such that \( BC = I \), where \( I \) is the identity matrix.
- **Reduced Row-Echelon Form (RREF)**: A matrix is in RREF if it meets specific criteria, including leading 1s and zeros in all other positions of the column.
- **Vandermonde Matrix**: A matrix with the powers of a vector, used in polynomial interpolation.

## Detailed Technical Breakdown

### 1. Properties of Nilpotent Matrices
#### (a) Show that \( I - A \) is invertible if \( A^2 = 0 \)
- To prove \( I - A \) is invertible, we check:
  \[
  (I - A)(I + A) = I^2 - A^2 = I
  \]
  Thus, the inverse is \( I + A \).

#### (b) Is \( I - A \) invertible if \( A^3 = 0 \)?
- Using the polynomial identity:
  \[
  (I - A)(I + A + A^2) = I - A^3 = I
  \]
  Therefore, \( I - A \) is also invertible.

#### (c) General case for nilpotent matrices
- If \( A \) is nilpotent, then:
  \[
  (I - A)(I + A + \ldots + A^{n-1}) = I - A^n = I
  \]
  Hence, \( I - A \) is invertible with the inverse given by the sum.

### 2. Reduced Row-Echelon Form
#### (a) Reduce the following matrices to RREF
- **Matrix A**:
  \[
  A = \begin{pmatrix}
  5 & -2 & 6 & 0 \\
  -2 & 1 & 3 & 1 \\
  -1 & 3 & -4 & 2 \\
  -4 & 2 & -9 & 1
  \end{pmatrix}
  \]
  - **Elementary Row Operations**:
    - \( E_1, E_2, \ldots, E_n \) correspond to each operation performed.

#### (b) Example of Elementary Matrices
- The elementary matrices corresponding to the operations can be constructed and applied to obtain RREF.

### 3. Polynomial Interpolation
#### (a) Find a cubic polynomial through given points
- Given points: \( (1, 3), (2, -2), (3, -5), (4, 0) \)
- The augmented matrix is:
  \[
  \begin{pmatrix}
  1 & 1 & 1 & 1 & 3 \\
  1 & 2 & 4 & 8 & -2 \\
  1 & 3 & 9 & 27 & -5 \\
  1 & 4 & 16 & 64 & 0
  \end{pmatrix}
  \]
- The RREF yields the polynomial \( x^3 - 5x^2 + 3x + 4 \).

#### (b) MATLAB Implementation
```matlab
v = [1; 2; 3; 4; 5; 6; 7; 8];
A = fliplr(vander(v));
b = [12; 70; 1244; 10500; 54268; 205682; 630540; 1657024];
coefficients = A\b;
```

### 4. Electrical Networks
- **Ohm's Law**: \( E = IR \)
- **Kirchhoff's Laws**:
  - KCL: Sum of currents at a node is zero.
  - KVL: Sum of voltage rises and drops in a loop is zero.

#### Example Circuit Analysis
- Set up linear systems based on KCL and KVL, solve using Gaussian elimination.

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [1 -1 0; 0 1 -1; 5 10 0];
b = [0; 0; 10];
I = A\b; % Solve for currents
```

> [!note] **Important**: Always verify the assumptions made in circuit analysis, especially regarding current directions and voltage drops.
> [!warning] **Caution**: Misinterpretation of circuit elements can lead to incorrect results; ensure clarity in defining variables.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Logic - Propositional Logic]]