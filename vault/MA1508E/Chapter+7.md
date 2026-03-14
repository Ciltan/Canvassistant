---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 7: System of Linear Differential Equations

## Overview
This chapter delves into the fundamentals of first-order linear systems of differential equations, emphasizing their representation in both standard and matrix forms. It categorizes these systems into homogeneous and non-homogeneous types, with a focus on constant coefficients. The chapter also explores the solutions to these systems, including the initial value problems (IVPs) and the significance of eigenvalues and eigenvectors in determining the general solutions.

## Key Concepts & Definitions
- **First Order Linear System of Differential Equations**: A system characterized by equations of the form \( y'(t) = A(t)y(t) + g(t) \).
- **Homogeneous System**: A system where the forcing term \( g(t) = 0 \).
- **Constant Coefficient**: A system where the coefficients in matrix \( A(t) \) are constants.
- **Initial Value Problem (IVP)**: A differential equation along with specified initial conditions.
- **Eigenvalues and Eigenvectors**: Fundamental concepts in linear algebra that play a crucial role in solving differential equations.

## Detailed Technical Breakdown

### 7.1 First Order Linear System of Differential Equations
- **Standard Form**:
  \[
  \begin{align*}
  y_1'(t) &= a_{11}(t)y_1(t) + \ldots + a_{1n}(t)y_n(t) + g_1(t) \\
  y_2'(t) &= a_{21}(t)y_1(t) + \ldots + a_{2n}(t)y_n(t) + g_2(t) \\
  &\vdots \\
  y_n'(t) &= a_{n1}(t)y_1(t) + \ldots + a_{nn}(t)y_n(t) + g_n(t)
  \end{align*}
  \]

- **Matrix Form**:
  \[
  \begin{pmatrix}
  y_1'(t) \\
  y_2'(t) \\
  \vdots \\
  y_n'(t)
  \end{pmatrix}
  =
  \begin{pmatrix}
  a_{11}(t) & \ldots & a_{1n}(t) \\
  a_{21}(t) & \ldots & a_{2n}(t) \\
  \vdots & \ddots & \vdots \\
  a_{n1}(t) & \ldots & a_{nn}(t)
  \end{pmatrix}
  \begin{pmatrix}
  y_1(t) \\
  y_2(t) \\
  \vdots \\
  y_n(t)
  \end{pmatrix}
  +
  \begin{pmatrix}
  g_1(t) \\
  g_2(t) \\
  \vdots \\
  g_n(t)
  \end{pmatrix}
  \]

- **Compact Vector Notation**:
  \[
  y'(t) = A(t)y(t) + g(t)
  \]

### Classification of Systems
- **Homogeneous**: \( g(t) = 0 \) leads to \( y'(t) = A(t)y(t) \).
- **Constant Coefficient**: \( A(t) \) is a constant matrix.

### Examples
1. **Non-homogeneous, Non-constant Coefficient**:
   \[
   \begin{align*}
   y_1'(t) &= \cos(t)y_1(t) - \sin(t)y_2(t) + t^2 \\
   y_2'(t) &= \sin(t)y_1(t) + \cos(t)y_2(t) + 2t
   \end{align*}
   \]

2. **Homogeneous, Constant Coefficient**:
   \[
   \begin{align*}
   y_1'(t) &= y_1(t) + y_2(t) \\
   y_2'(t) &= 2y_1(t) - y_2(t)
   \end{align*}
   \]

### Solutions to System of Differential Equations
- A function-valued vector \( x(t) \) is a solution if it satisfies \( x'(t) = Ax(t) \).
- **Initial Condition**: Specifies the value of the solution at \( t = t_0 \).

> [!note] **Initial Value Problem (IVP)**: Finding a function \( x(t) \) that satisfies both the differential equation and the initial condition.

### Theorem: Superposition Principle
If \( x_1(t) \) and \( x_2(t) \) are solutions, then \( \alpha x_1(t) + \beta x_2(t) \) is also a solution for any \( \alpha, \beta \in \mathbb{R} \).

## Implementation/Examples
```markdown
# Example of Solving an IVP
Consider the system:
\[
\begin{align*}
y_1'(t) &= y_1(t) \\
y_2'(t) &= 2y_2(t)
\end{align*}
\]
with initial conditions \( y_1(0) = 1 \) and \( y_2(0) = 1 \).

The solution can be expressed as:
\[
x(t) = 
\begin{pmatrix}
e^t \\
e^{2t}
\end{pmatrix}
\]
```

> [!important] **Eigenvalues and Eigenvectors**: The solutions can be expressed as linear combinations of eigenvectors multiplied by exponential functions of their corresponding eigenvalues.

## Related
- [[Logic - Propositional Logic]]
- [[Determinants]]
- [[Midterm Briefing]]
- [[AY2122+Sem1+Homework+3]]