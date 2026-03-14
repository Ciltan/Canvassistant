---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Final Exam Overview

## Overview
This note summarizes the final exam for MA1508E, focusing on key concepts and solutions related to linear algebra. The exam consists of five questions covering topics such as subspaces, dimensions, least squares solutions, eigenvalues, and eigenvectors. Each question is structured to assess understanding of fundamental principles and problem-solving skills in linear algebra.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. [[Subspace]]
- **Dimension**: The number of vectors in a basis for a vector space, indicating the space's size. [[Dimension]]
- **Basis**: A set of linearly independent vectors that span a vector space. [[Basis]]
- **Eigenvalue**: A scalar associated with a linear transformation that indicates how much a corresponding eigenvector is stretched or compressed. [[Eigenvalue]]
- **Eigenvector**: A non-zero vector that changes by only a scalar factor when a linear transformation is applied. [[Eigenvector]]
- **Least Squares Solution**: A method to find the best approximation to a solution of an overdetermined system. [[LeastSquares]]

## Detailed Technical Breakdown

### Question 1: Subspaces and Dimensions
1. **Subspace V**:
   - Given vectors \( V \) and \( U \), show that \( V \) is a subspace of \( \mathbb{R}^4 \).
   - Find a spanning set \( S \) such that \( V = \text{span}(S) \).
   - Show that \( \text{dim}(V) = 2 \) using elementary row operations.

2. **Dimension of U**:
   - Check for linear dependency in the spanning set of \( U \).
   - Conclude that \( \text{dim}(U) = 2 \).

3. **Basis for W**:
   - Combine bases from \( V \) and \( U \) to find a basis for \( W \).
   - Show that \( \text{dim}(W) = 3 \).

4. **Basis Verification**:
   - Verify that a given set \( T \) is a basis for \( W \) by checking linear independence and spanning properties.

5. **Coordinate Representation**:
   - Find coordinates of a vector \( w \) relative to the basis \( T \).

### Question 2: Matrix Operations
1. **Matrix Squaring**:
   - Compute \( A^2 \) for a given matrix \( A \).

2. **Consistency of Ax = b**:
   - Determine if the system \( Ax = b \) is consistent based on the relationship between rows of \( A \).

3. **Least Squares Solutions**:
   - Solve for least squares solutions using the normal equations \( A^TAx = A^Tb \).

4. **Projection**:
   - Find a vector \( d \) that minimizes the distance \( \|d - b\| \).

### Question 3: Diagonalization
- Find an orthogonal matrix \( P \) and a diagonal matrix \( D \) such that \( P^TAP = D \).

### Question 4: Eigenvalues and Diagonalization
1. **Eigenvalues**:
   - Show that the only eigenvalues of matrix \( A \) are 0 and 1, and determine their algebraic multiplicities.

2. **Diagonalizability**:
   - Assess whether \( A \) is diagonalizable based on the geometric and algebraic multiplicities of its eigenvalues.

3. **Generalized Eigenvectors**:
   - Find a generalized eigenvector associated with eigenvalue 1.

4. **Matrix Transformation**:
   - Verify the transformation \( P^{-1}AP \) for a constructed matrix \( P \).

5. **Matrix Powers**:
   - Compute \( A^5 \) using the diagonalization result.

### Question 5: Initial Value Problem
- Solve the initial value problem \( y'''(t) + y''(t) - 2y(t) = 0 \) with specified initial conditions.

## Implementation/Examples
```markdown
# Example of finding a basis for W
Let V = span{(1, 2, 1), (0, 1, -1)} and U = span{(1, 2, 1), (0, 1, 1)}.
W = V + U = span{(1, 2, 1), (0, 1, -1), (1, 2, 1), (0, 1, 1)}.
```

> [!note] **Important**: Always show your workings clearly, especially when performing elementary row operations.
> [!warning] **Caution**: Ensure that all vectors are linearly independent when forming a basis.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[MA1508E+AY2122Sem1]]