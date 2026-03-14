---
tags: [MA1508E, lecture-notes, academic]
---

# Introduction to MATLAB

## Overview
This note provides a comprehensive introduction to MATLAB, focusing on installation, basic operations, functions, and solving algebraic equations. It serves as a foundational guide for students at the National University of Singapore, detailing essential commands and functionalities that facilitate mathematical computations and programming within the MATLAB environment.

## Key Concepts & Definitions
- **MATLAB**: A high-performance language for technical computing.
- **Installation**: Steps to install MATLAB on personal computers using NUS credentials.
- **Basic Operations**: Fundamental arithmetic operations and their syntax in MATLAB.
- **Functions**: Built-in functions for mathematical computations, including trigonometric and logarithmic functions.
- **Algebraic Equations**: Methods to solve single and multi-variable equations using MATLAB commands.

## Detailed Technical Breakdown

### 1. Installation
- **License**: NUS provides a Total Academic Headcount license for MATLAB.
- **VPN Requirement**: Use VPN if not on NUS network.
- **Steps**:
  1. Sign in to VPN.
  2. Download MATLAB from the NUS portal.
  3. Create a MathWorks account with your NUS email.
  4. Download and install MATLAB.

### 2. Basic Operations
- **Environment**: MATLAB acts as a complex calculator.
- **Arithmetic Operators**:
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Exponentiation: `^`
- **Example**:
  ```matlab
  >> 123 + 321
  ans = 444
  ```

### 3. Basic Functions
- **Square Root**: `sqrt(x)`
- **Format Control**:
  - `format long`: Displays 16 decimal digits.
  - `format rat`: Displays rational approximation.
- **Trigonometric Functions**: `sin(x)`, `cos(x)`, `tan(x)`, etc.

### 4. Solving Basic Algebraic Equations
- **Single Variable**:
  ```matlab
  >> syms x;
  >> solve(x^2 + x - 1 == 0, x)
  ```
- **Multi-Variable**:
  ```matlab
  >> syms x y;
  >> [Sx, Sy] = solve([3*x + y == 10, x + y == 20], [x, y])
  ```

### 5. Sums
- **Arithmetic Sequence**:
  ```matlab
  >> symsum(a + (k-1)*d, k, [1, n])
  ```
- **Geometric Sequence**:
  ```matlab
  >> symsum(a*r^(k-1), k, [1, n])
  ```

### 6. Vectors
- **Definition**: A vector can be defined as `[a, b, c]`.
- **Operations**:
  - Addition: `u + v`
  - Dot Product: `dot(u, v)`
  - Cross Product: `cross(u, v)`

### 7. Functions
- **Standard Function**:
  ```matlab
  >> f = @(x) x^2;
  ```
- **Piecewise Function**:
  ```matlab
  >> f = piecewise(x >= 0, x, x < 0, -x);
  ```

### 8. Curve Plotting
- **Standard Function Plotting**:
  ```matlab
  >> fplot(f, [-100, 100]);
  ```
- **Multiple Curves**:
  ```matlab
  >> hold on;
  >> fplot(g, [-2*pi, 2*pi]);
  >> hold off;
  ```

### 9. Limits
- **Limit Calculation**:
  ```matlab
  >> limit(f(x), x, a)
  ```

### 10. Derivative
- **Using `diff`**:
  ```matlab
  >> diff(f, x)
  ```

### 11. Integral
- **Indefinite Integral**:
  ```matlab
  >> int(f, x)
  ```

> [!note] Remember to always check the MATLAB documentation for the latest updates and additional functionalities.
> [!important] Ensure that you have the correct permissions and licenses when installing and using MATLAB on personal devices.

## Related
- [[Matlab+for+Engineering]]
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]