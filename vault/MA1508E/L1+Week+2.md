---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Week 2 Lecture Notes

## Overview
This lecture focuses on solving linear systems using various methods, including the formation of augmented matrices and the application of row operations. Key concepts such as consistency of linear systems and the implications of row-echelon forms are discussed. MATLAB is introduced as a tool for performing these operations efficiently.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Augmented Matrix**: A matrix that includes the coefficients of the variables and the constants from the equations.
- **Row-Echelon Form (REF)**: A form of a matrix where all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row.
- **Reduced Row-Echelon Form (RREF)**: A form of a matrix where it is in REF and all leading coefficients are 1 and are the only non-zero entries in their column.
- **Gaussian Elimination**: A method for solving linear systems by transforming the augmented matrix into REF.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that transforms the matrix into RREF.

## Detailed Technical Breakdown

### Steps to Solve Linear Systems
1. **Standard Form**: Write the linear system in its standard form.
2. **Augmented Matrix**: Form the augmented matrix of the linear system.
3. **Row Reduction**:
   - Reduce the augmented matrix to REF or RREF using Gaussian or Gauss-Jordan elimination.
4. **Consistency Check**:
   - If the last column is a pivot column, the system is inconsistent.
   - If not, assign non-pivot column variables as parameters.
5. **Solution Extraction**:
   - If in RREF, read solutions directly.
   - If in REF, perform back substitution.
6. **General Solution**: Write down the general solution to the system.

### Consistency of Linear Systems
- **No Solution**: A row of zeros in the coefficient matrix with a non-zero constant.
- **Unique Solution**: All columns of the coefficient matrix are pivot columns.
- **Infinitely Many Solutions**: Presence of non-pivot columns in the augmented matrix.

### Row Operations in MATLAB
- Input the augmented matrix: 
  ```matlab
  R = [1 2 3 4; 2 1 1 -1; 1 2 -1 0];
  ```
- Perform row operations:
  - Subtract rows: 
    ```matlab
    R(2,:) = R(2,:) - 2 * R(1,:);
    ```
  - Swap rows: 
    ```matlab
    R([2,3],:) = R([3,2],:);
    ```
  - Scale rows: 
    ```matlab
    R(3,:) = (-1/3) * R(3,:);
    ```

> [!note] **Important**: Always check the consistency of the system after performing row operations to ensure accurate results.

## Implementation/Examples
### Example Problem
Solve the system:
\[
\begin{align*}
x_1 + 3x_3 &= 13 \\
-x_1 - x_2 - x_3 &= -8 \\
3x_1 + x_2 + 2x_3 &= 14 \\
2x_1 + 3x_2 &= 11
\end{align*}
\]
1. Form the augmented matrix:
   ```matlab
   R = [1 0 3 13; -1 -1 -1 -8; 3 1 2 14; 2 3 0 11];
   ```
2. Perform row operations to reach REF or RREF.

> [!important] **Caution**: Ensure that the parameters assigned to non-pivot columns are correctly interpreted in the context of the solution.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Logic - Propositional Logic]]