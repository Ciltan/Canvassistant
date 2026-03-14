---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 11

## Overview
This tutorial focuses on the application of linear differential equations in modeling biological systems, specifically the interaction between two fish species competing for resources. It also explores the conversion of second-order differential equations into first-order systems, providing a structured approach to solving these equations. Additionally, the tutorial includes MATLAB applications for solving linear differential equations, emphasizing the importance of computational tools in engineering mathematics.

## Key Concepts & Definitions
- **Linear Differential Equations**: Equations involving derivatives of a function that can be expressed in a linear form.
- **System of Differential Equations**: A set of equations that describe multiple interdependent variables.
- **Fundamental Set of Solutions**: A set of solutions to a homogeneous linear differential equation that can be combined to form the general solution.
- **Wronskian**: A determinant used to test the linear independence of a set of solutions.
- **MATLAB**: A high-level programming language and environment used for numerical computing.

## Detailed Technical Breakdown

### 1. Application of Linear Differential Equations
- **Modeling Fish Populations**:
  - Let \( a(t) \) and \( b(t) \) represent the populations of species A and B, respectively.
  - Growth rates:
    - Without species B: \( a'(t) = 4a(t) \)
    - With species B: \( a'(t) = 4a(t) - 2b(t) \)
    - Without species A: \( b'(t) = 3b(t) \)
    - With species A: \( b'(t) = 3b(t) - a(t) \)

#### (a) System of Linear Differential Equations
- The system can be expressed as:
  \[
  \begin{align*}
  a'(t) &= 4a(t) - 2b(t) \\
  b'(t) &= 3b(t) - a(t)
  \end{align*}
  \]

#### (b) Matrix Representation
- Representing the system as \( x'(t) = Ax(t) \):
  \[
  x(t) = \begin{pmatrix} a(t) \\ b(t) \end{pmatrix}, \quad A = \begin{pmatrix} 4 & -2 \\ -1 & 3 \end{pmatrix}
  \]

#### (c) Initial Conditions
- Solve with \( a(0) = 60, b(0) = 120 \).

### 2. Second Order Systems
- **Conversion to First Order**:
  - Introduce new variables:
    \[
    y_{n+1}(t) = y'(t), \quad y_{n+2}(t) = y'(t)
    \]
  - The system can be expressed as:
    \[
    Y' = \begin{pmatrix} 0 & I \\ A_1 & A_2 \end{pmatrix} Y
    \]

#### Example Equations
- (a) \( y'' + 2y' + 5y = 0 \)
- (b) \( y'' = 2y + y + y' + y' \)

### 3. Homogeneous Systems of Differential Equations
- For each system:
  - (i) Find a fundamental set of solutions.
  - (ii) Use the Wronskian to verify linear independence.
  - (iii) Write down the general solution.
  - (iv) Solve the initial value problem.

### Supplementary Problems
#### MATLAB Applications
- **Characteristic Polynomial**:
  ```matlab
  syms x
  p = charpoly(A, x);
  factor(p, x);
  ```

- **Solving Initial Value Problems**:
  ```matlab
  syms y1(t) y2(t) y3(t) y4(t) y5(t);
  y = [y1; y2; y3; y4; y5];
  conds = [y1(0) == 1, y2(0) == 1, y3(0) == 1, y4(0) == 1, y5(0) == 1];
  [Sy1, Sy2, Sy3, Sy4, Sy5] = dsolve(diff(y, t) == A*y, conds);
  ```

> [!note] Remember to verify the solutions obtained through MATLAB with analytical methods for consistency.
> [!important] Understanding the conversion of second-order systems to first-order systems is crucial for solving complex differential equations effectively.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Stacks and Queues]]