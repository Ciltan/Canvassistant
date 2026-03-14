---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Midterm Test Overview

## Overview
The Midterm Test for MA1508E - Linear Algebra for Engineering consists of five questions, covering key concepts in linear algebra. Students are required to demonstrate their understanding of linear systems, matrix operations, and determinants within a closed-book format. The test emphasizes problem-solving skills and the application of theoretical knowledge to practical scenarios.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables. [[Logic - Propositional Logic]]
- **Unique Solution**: A solution to a linear system where exactly one set of values satisfies all equations. [[Determinants]]
- **Infinitely Many Solutions**: A scenario where there are multiple sets of values that satisfy the equations, often dependent on one or more parameters. [[Stacks and Queues]]
- **Elementary Row Operations**: Operations used to manipulate the rows of a matrix to solve linear systems. [[Matlab+for+Engineering]]
- **Determinant**: A scalar value that is a function of the entries of a square matrix, providing important properties of the matrix. [[Determinants]]

## Detailed Technical Breakdown

### Instructions to Students
- Write your name, student number, and tutorial group.
- The exam consists of 5 questions and is worth 50 marks.
- Closed book assessment with one A4 handwritten help sheet allowed.
- Non-programmable calculators permitted; workings must be shown.
- All questions must be answered.

### Question Breakdown
1. **Linear System Analysis**
   - **(a)** Conditions for no solution.
   - **(b)** Conditions for a unique solution and its derivation.
   - **(c)** Conditions for infinitely many solutions with one parameter.
   - **(d)** Conditions for infinitely many solutions with two parameters.

2. **Matrix Operations**
   - **(a)** Solve the equation \( Ax = b \).
   - **(b)** Find the inverse of matrix \( A \).

3. **Elementary Matrices**
   - **(a)** Identify matrices \( A \) and \( B \).
   - **(b)** Find elementary matrices that relate \( A \) and \( B \).

4. **Determinants and Solutions**
   - **(a)** Calculate \( \text{det}(A) \).
   - **(b)** Solve a system of equations involving parameters.

5. **Vector Spaces**
   - **(a)** Determine which vectors belong to the span \( V \).
   - **(b)** Express \( V \) as a solution set to a linear system.

## Implementation/Examples

```plaintext
1. Given the linear system:
   x1 + ax2 + bx3 + (a−b)x4 = 1
   x1 + x2 + bx3 − (b−a)x4 = 2
   -x1 − ax2 = −1
   x1 + x2 + bx3 + ax4 = 2

   (a) No solution when determinant is zero.
   (b) Unique solution when determinant is non-zero.
   (c) Infinitely many solutions with one parameter when rank < number of variables.
   (d) Infinitely many solutions with two parameters when rank < number of variables - 1.
```

> [!note] Remember to show all workings clearly, including any elementary row operations used in your calculations.

> [!important] Ensure you understand the conditions for different types of solutions in linear systems, as this is crucial for solving the exam questions effectively.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[CS1231+TUTORIAL+3]]