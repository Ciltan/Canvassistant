---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 1

## Overview
This tutorial focuses on solving linear systems using Gaussian and Gauss-Jordan elimination methods. It includes practical applications of linear algebra in chemical equations and temperature distribution modeling. Students are encouraged to perform elementary row operations manually and explore the implications of different parameter values in linear systems.

## Key Concepts & Definitions
- **Gaussian Elimination**: A method for solving linear systems by transforming the system's augmented matrix into row echelon form.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that reduces the matrix to reduced row echelon form.
- **Homogeneous System**: A system of linear equations where all constant terms are zero.
- **Linear System**: A collection of one or more linear equations involving the same set of variables.
- **Chemical Equation**: A symbolic representation of a chemical reaction, showing the reactants and products.

## Detailed Technical Breakdown

### 1. Solving Linear Systems
- **Task**: Solve the following systems using Gaussian or Gauss-Jordan elimination.
  
  #### (a)
  \[
  \begin{align*}
  3x_1 + 2x_2 - 4x_3 &= 3 \\
  2x_1 + 3x_2 + 3x_3 &= 15 \\
  5x_1 - 3x_2 + x_3 &= 14
  \end{align*}
  \]

  #### (b)
  \[
  \begin{align*}
  a + b - c - 2d &= 0 \\
  2a + b - c + d &= -2 \\
  -a + b - 3c + d &= 4
  \end{align*}
  \]

  #### (c)
  \[
  \begin{align*}
  x - 4y + 2z &= -2 \\
  x + 2y - 2z &= -3 \\
  x - y &= 4
  \end{align*}
  \]

### 2. Reducing Matrices
- **Task**: Reduce the following matrix to its reduced row echelon form.
  
  \[
  \begin{pmatrix}
  2 & 6 & 5 & 0 \\
  1 & 0 & 4 & 0 \\
  1 & 4 & 5 & 0
  \end{pmatrix}
  \]

### 3. Parameter Values in Linear Systems
- **Task**: Determine values of \( a \) and \( b \) for the system:
  
  \[
  \begin{align*}
  ax + bz &= 2 \\
  ax + ay + 4z &= 4 \\
  ay + 2z &= b
  \end{align*}
  \]
  
  - (a) No solution
  - (b) One solution
  - (c) Infinitely many solutions with one arbitrary parameter
  - (d) Infinitely many solutions with two arbitrary parameters

### 4. Applications
- **Chemical Reactions**: Balancing chemical equations using linear systems.
  
  Example: 
  \[
  CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O
  \]

- **Temperature Distribution**: Estimating temperature on a square plate using averaging rules.

### 5. MATLAB Applications
- **Traffic Flow**: Analyzing a network of one-way streets using linear systems.
  
  - **Task**: Determine traffic volumes and assess road closures.

### 6. Supplementary Problems
- **Temperature Estimation**: Setting up a linear system for a finer mesh of temperature nodes.

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [2 6 5 0; 1 0 4 0; 1 4 5 0];
b = [0; 0; 0];
x = A\b; % Solving the system
```

> [!note] **Important**: Ensure you can perform elementary row operations manually, as this is crucial for understanding the underlying principles of linear algebra.
> 
> [!warning] **Caution**: Be mindful of the implications of parameter values in linear systems, as they can drastically change the nature of the solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[Matlab+for+Engineering]]