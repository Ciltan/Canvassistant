---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 2 - Solutions Overview

## Overview
This note summarizes the solutions to various problems from the MA1508E course, focusing on matrix operations, determinants, and linear systems. Key concepts such as [[elementary row operations]], [[determinants]], and [[matrix inversion]] are explored through detailed examples. The solutions illustrate the application of linear algebra techniques in engineering contexts.

## Key Concepts & Definitions
- **Matrix A**: A rectangular array of numbers arranged in rows and columns.
- **Determinant**: A scalar value that is a function of a square matrix, providing important properties about the matrix, such as invertibility.
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to simplify it, including row swapping, scaling, and row addition.
- **Inverse of a Matrix**: A matrix that, when multiplied by the original matrix, yields the identity matrix.
- **Cofactor Expansion**: A method for calculating the determinant of a matrix by expanding along a row or column.

## Detailed Technical Breakdown

### Problem 1: Matrix A Calculation
Given the matrix:
```
A = |  2  2  2 |
    | -3  1 -1 |
    |  0  2  0 |
    | -1 -1 -1 |
    |  1  8  2 |
    | -1  2  0 |
```
- **Block Multiplication**: 
  - The matrix can be expressed as a sum of its components.
  - Result: 
    ```
    A = A1 + A2
    ```

### Problem 2: Inverse of Matrix A
1. **Elementary Row Operations**:
   - Perform 5 operations to compute the inverse.
   - Example operations:
     - \( R_3 \leftarrow R_3 - R_2 \)
     - \( R_2 \leftarrow R_2 - R_1 \)
   - Resulting inverse:
   ```
   A^{-1} = | 0  -1/3  1/3 |
             | 0  -2/3 -1/3 |
   ```

2. **Determinant Calculation**:
   - Using the product of the elementary row operations:
   ```
   det(A) = (1)(1)(-3)(1)(-1) = 3
   ```

3. **Linear System Solution**:
   - Given the system:
   ```
   x1 + x2 + x3 = 1
   -x2 - x3 = 3
   2x2 - x3 = 3
   ```
   - Matrix equation:
   ```
   A * x = b
   ```
   - Solution:
   ```
   x = A^{-1} * b
   ```

### Problem 3: Determinant Calculation via Cofactor Expansion
1. **Matrix A**:
   ```
   A = | 2  -2  -2  1 |
       | a   1   0 -1 |
       | 1   a   0  1 |
       | 1   2   0  0 |
   ```
2. **Cofactor Expansion**:
   - Expand along the third column:
   ```
   det(A) = -2 * det(M) + ... = 2(a + 1)
   ```

3. **Determinant of Transformed Matrix**:
   - Given \( det(B) = 18 \):
   ```
   det(3A^T B^{-1}) = 9(a + 1)
   ```

> [!note] The importance of understanding matrix operations cannot be overstated, as they form the foundation for solving complex engineering problems.
> 
> [!important] Always verify the properties of matrices, such as invertibility, before proceeding with calculations.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Logic - Propositional Logic]]