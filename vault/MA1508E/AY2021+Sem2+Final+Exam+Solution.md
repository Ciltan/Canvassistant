---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Final Exam Solutions

## Overview
This note summarizes the solutions to the final examination for MA1508E, focusing on key concepts in [[Linear Algebra]], including systems of equations, polynomial interpolation, and differential equations. The exam consists of six questions, each addressing different aspects of linear algebra, with a particular emphasis on problem-solving techniques and theoretical understanding.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Unique Solution**: A situation where a linear system has exactly one solution.
- **Infinitely Many Solutions**: Occurs when a linear system has more than one solution, often parameterized by one or more variables.
- **Polynomial Interpolation**: The process of determining a polynomial that passes through a given set of points.
- **Eigenvalues and Eigenvectors**: Scalars and vectors associated with a linear transformation that describe the scaling factor and direction of transformation, respectively.
- **Differential Equations**: Equations involving derivatives that describe how a quantity changes over time.

## Detailed Technical Breakdown

### Question 1: Linear Systems
- **System of Equations**:
  \[
  \begin{align*}
  x_1 + 3x_3 + x_4 &= 2 \\
  3x_1 + ax_2 + 9x_3 &= 6 \\
  2x_1 + (a+6)x_3 + ax_4 &= b+2 \\
  2x_1 + 6x_3 + bx_4 &= b+2
  \end{align*}
  \]

- **Conditions**:
  - **No Solution**: \( a = 0, b \neq 2 \)
  - **Unique Solution**: \( a \neq 0, b \neq 2 \) with solution \( x = \frac{1 + 3a - b}{a}, x_2 = 3, x_3 = b - a, x_4 = 1 \)
  - **Infinitely Many Solutions (1 parameter)**: \( a \neq 0, b = 2 \) with general solution \( x_1 = 2 + 2a - 6s, x_2 = 3s, x_3 = 2 - as, x_4 = s, s \in \mathbb{R} \)
  - **Infinitely Many Solutions (2 parameters)**: \( a = 0, b = 2 \) with general solution \( x_1 = 2 - 3t, x_2 = s, x_3 = t, x_4 = 0, s,t \in \mathbb{R} \)

### Question 2: Polynomial Interpolation
- **Degree 5 Polynomial**:
  \[
  p(x) = 2x^5 - 3x^4 + x^3 + 2x^2 - 7x - 5
  \]

- **Degree 4 Polynomial**:
  - **Existence**: Not possible for 7 points.
  - **Minimization**: Find \( q(x) \) such that \( \sum_{i=1}^{7} (q(x_i) - y_i)^2 \) is minimized.

### Question 3: Subspaces and Basis
- **Subspace Verification**: Show spanning set for \( V \).
- **Basis**: \( S = \{(0, 0, 1), (0, 4, -2), (1, 6, -3)\} \) is a basis for \( V \).

### Question 4: Matrix Inverses
- **Left Inverse**: Exists for matrix \( B \).
- **Right Inverse**: Exists for matrix \( A \).
- **Determinant**: \( \text{det}(AB) = -27 \).

### Question 5: Eigenvalues and Differential Equations
- **Eigenvalues**: \( -1, 3 \) (multiplicity).
- **Diagonalization**: \( A = PDP^{-1} \) with \( P \) and \( D \) defined.

### Question 6: Differential Equations
- **Fundamental Set of Solutions**: \( e^{2t}, e^{2t}(t + \frac{1}{4}) \).
- **General Solution**: \( y(t) = c_1 e^{2t} + c_2 e^{2t}(t + \frac{1}{4}) \).

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [1 0 3 1; 0 a 0 -3; 0 0 a a-2; 0 0 0 b-2];
b = [2; 6; b+2; b+2];
x = A\b; % Solve Ax = b
```

> [!note] Ensure to check the conditions for solutions in linear systems.
> [!important] Remember to clearly document all steps in your calculations during exams.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[CS1231+TUTORIAL+3]]