---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Week 2 Lecture Notes

## Overview
This lecture focuses on solving linear systems using various methods, including the formation of augmented matrices and the application of Gaussian elimination techniques. Key concepts such as the consistency of linear systems and the implications of row-echelon forms are discussed. Additionally, MATLAB operations for matrix manipulation are introduced, providing practical tools for engineering applications.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Augmented Matrix**: A matrix that includes the coefficients and constants of a linear system.
- **Row-Echelon Form (REF)**: A form of a matrix where each leading entry of a row is to the right of the leading entry of the previous row.
- **Reduced Row-Echelon Form (RREF)**: A further simplified version of REF where each leading entry is 1 and is the only non-zero entry in its column.
- **Gaussian Elimination**: A method for solving linear systems by transforming the augmented matrix into REF.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that reduces the matrix to RREF.

## Detailed Technical Breakdown

### Steps to Solve Linear Systems
1. **Standard Form**: Write the linear system in standard form.
2. **Augmented Matrix**: Form the augmented matrix of the linear system.
3. **Row Reduction**: Reduce the augmented matrix to REF or RREF using Gaussian or Gauss-Jordan elimination.
4. **Consistency Check**:
   - If the last column is a pivot column, the system is inconsistent.
   - If not, assign non-pivot variables as parameters.
5. **Solution Extraction**:
   - If in RREF, read solutions directly.
   - If in REF, perform back substitution.
6. **General Solution**: Write down the general solution.

### Consistency of Linear Systems
- **No Solution**: A row of zeros in the coefficient matrix with a non-zero constant.
- **Unique Solution**: All columns of the coefficient matrix are pivot columns.
- **Infinitely Many Solutions**: At least one non-pivot column exists in the augmented matrix.

### MATLAB Row Operations
- Input the augmented matrix:
  ```matlab
  R = [1 2 3 4; 2 1 1 -1; 1 2 -1 0];
  ```
- Perform row operations:
  - Subtract rows: `R(2,:) = R(2,:) - 2*R(1,:);`
  - Swap rows: `R([2,3],:) = R([3,2],:);`
  - Scale rows: `R(3,:) = (-1/3)*R(3,:);`
- Display formats:
  - `format rat` for fractions.
  - `format short` for 4 decimal places.

> [!important] **Note**: Always check the consistency of the system after performing row operations.

## Implementation/Examples
### Example Problem
Solve the system:
\[
\begin{align*}
x_1 + 3x_2 &= 13 \\
-x_1 - x_2 - x_3 &= -8 \\
3x_1 + x_2 + 2x_3 &= 14 \\
2x_1 + 3x_2 &= 11
\end{align*}
\]
1. Form the augmented matrix:
   ```matlab
   R = [1 3 0 13; -1 -1 -1 -8; 3 1 2 14; 2 3 0 11];
   ```
2. Perform row operations to reach REF or RREF.

> [!note] **Caution**: Ensure to track the changes in the matrix carefully during row operations.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Stacks and Queues]]