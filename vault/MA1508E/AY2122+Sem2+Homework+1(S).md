---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 1 - Homework Solutions

## Overview
This note summarizes the solutions to a series of linear systems presented in the MA1508E course. It explores conditions for the existence of solutions, including cases of no solution, unique solutions, and infinitely many solutions. The note also includes matrix representations and elementary row operations used in the solution process.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Augmented Matrix**: A matrix that includes the coefficients of the variables and the constants from the equations.
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to simplify it, including row swapping, scaling, and row addition.
- **RREF (Reduced Row Echelon Form)**: A form of a matrix where each leading entry is 1 and is the only non-zero entry in its column.

## Detailed Technical Breakdown

### Problem 1: Linear System Analysis
1. **Given System**:
   \[
   \begin{align*}
   x_1 + (a-1)x_2 + x_3 + x_4 &= a + 1 \\
   (a-2)x_2 + (a+2)x_3 + 2x_4 &= a + 1 \\
   (a-2)x_2 + x_3 + x_4 &= a \\
   x_1 + x_2 + (a+2)x_3 + 2x_4 &= a + 2
   \end{align*}
   \]

2. **Conditions for Solutions**:
   - **No Solution**: Occurs when the system is inconsistent.
   - **Unique Solution**: Exists when the determinant of the coefficient matrix is non-zero.
   - **Infinitely Many Solutions**: Occurs when there are free variables in the system.

3. **Elementary Row Operations**:
   - Row operations are applied to transform the augmented matrix into RREF.

### Problem 2: Matrix Equation and Consistency
1. **Matrix Representation**:
   \[
   A = \begin{pmatrix}
   1 & 1 & 1 \\
   0 & 2 & -2 \\
   0 & 1 & -2 \\
   -1 & -1 & -2
   \end{pmatrix}, \quad b = \begin{pmatrix}
   0 \\
   -1 \\
   1 \\
   1
   \end{pmatrix}
   \]

2. **Consistency Check**:
   - The system is inconsistent if the RREF leads to a row of the form \([0 \, 0 \, 0 \, | \, c]\) where \(c \neq 0\).

### Problem 3: Matrix Commutativity
1. **Matrix Equation**:
   \[
   AB = BA
   \]
   - Solve for matrices \(B\) that satisfy this equation.

2. **General Solution**:
   - The solution involves finding parameters \(s\) and \(t\) that define the matrix \(B\).

## Implementation/Examples
```plaintext
# Example of Row Operations
1. R2 = R2 - R1
2. R3 = R3 - R1
3. R4 = R4 + R1
```

> [!note] **Key Takeaway**: Understanding the conditions for the existence of solutions in linear systems is crucial for solving engineering problems effectively.

> [!important] **Reminder**: Always check the consistency of a linear system before attempting to find solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Logic - Propositional Logic]]