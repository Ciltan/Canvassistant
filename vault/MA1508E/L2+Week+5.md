---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - L2 Week 5 Live Lecture

## Overview
This lecture covers key concepts in linear algebra, focusing on matrix invertibility and Gaussian elimination. Students are reminded of upcoming deadlines for quizzes and homework, and the importance of checking submissions to avoid penalties. The session also includes practical examples of determining matrix invertibility and finding inverses using Gaussian elimination.

## Key Concepts & Definitions
- **Matrix Invertibility**: A matrix is invertible if there exists another matrix such that their product is the identity matrix. 
- **Gaussian Elimination**: A method for solving systems of linear equations, determining the rank of a matrix, and finding the inverse of an invertible matrix.
- **Determinant**: A scalar value that can be computed from the elements of a square matrix, which provides important information about the matrix, including whether it is invertible.

## Detailed Technical Breakdown

### Announcements
- **Quizzes**: Complete quizzes 2.6 to 2.9 by February 13, 2026.
- **Homework**: Homework 1 is due on February 15, 2026. Ensure the submitted file is correct.
- **Lecture Schedule**: No lecture next week due to Chinese New Year; students will watch recordings and submit problem-solving tasks by Friday at 11:59 PM.
- **Midterm Exam**: Scheduled for March 13, 2026, from 19:00 to 20:00 at MPSH.

### Example Problems

#### Question 1(a)
- **Problem**: Determine if the matrix 
  \[
  \begin{pmatrix}
  -1 & 3 \\
  3 & -2
  \end{pmatrix}
  \]
  is invertible using Gaussian elimination.
- **Solution**: 
  - Apply Gaussian elimination to the augmented matrix:
  \[
  \begin{pmatrix}
  -1 & 3 & | & 1 \\
  3 & -2 & | & 0
  \end{pmatrix}
  \]
  - Result: The matrix is invertible, and its inverse is calculated.

#### Question 1(b)
- **Problem**: Determine if the matrix 
  \[
  \begin{pmatrix}
  -1 & 3 & -4 \\
  2 & 4 & 1 \\
  -4 & 2 & -9
  \end{pmatrix}
  \]
  is invertible.
- **Solution**: 
  - Apply Gaussian elimination. The matrix is found to be not invertible.

#### Question 2(a)
- **Problem**: Write down conditions for the matrix 
  \[
  \begin{pmatrix}
  1 & 1 & 1 \\
  a & b & c \\
  a^2 & b^2 & c^2
  \end{pmatrix}
  \]
  to be invertible.
- **Conditions**: The points \(a\), \(b\), and \(c\) must be distinct.

### Implementation/Examples
```matlab
% MATLAB code to check matrix invertibility
A = [-1 3; 3 -2];
if det(A) ~= 0
    disp('Matrix is invertible');
else
    disp('Matrix is not invertible');
end
```

> [!note] **Important**: Always verify your matrix submissions to avoid penalties for late submissions.
> [!warning] **Caution**: Ensure that the conditions for invertibility are met before proceeding with calculations.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Gaussian Elimination]]