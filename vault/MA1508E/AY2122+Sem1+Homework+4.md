---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 4

## Overview
This note summarizes the key components of Homework 4 for the MA1508E course at the National University of Singapore. It outlines the submission guidelines, problem statements, and the focus on orthogonal diagonalization and differential equations. The tasks are designed to reinforce concepts in [[Linear Algebra]] and [[Differential Equations]].

## Key Concepts & Definitions
- **Orthogonal Diagonalization**: The process of diagonalizing a matrix using an orthogonal matrix.
- **Initial Value Problem**: A differential equation along with specified values at a given point.
- **Differential System**: A set of differential equations that describe the relationship between functions and their derivatives.

## Detailed Technical Breakdown

### Submission Guidelines
- Write answers on A4 size papers.
- Clearly write your student number and name on the top left corner of each page.
- Include the page number on the top right corner of each page.
- There are three questions totaling 20 marks.
- Submit your answers by scanning or photographing your work, merging images into a single PDF named as `StudentNo P4` (e.g., `A123456Z P4`), and upload to the LumiNUS folder for Practice 4 submission.

### Problem Statements
1. **Orthogonally Diagonalize the Matrix**  
   Given the matrix:
   \[
   A = \begin{pmatrix}
   5 & 1 & 1 \\
   1 & 5 & 1 \\
   1 & 1 & 5
   \end{pmatrix}
   \]
   - **Marks**: 8
   - **Note**: Leave your answer in surds.

2. **Solve the Initial Value Problem**  
   The system of equations is:
   \[
   \begin{align*}
   y_1' &= y_1 - y_3 \\
   y_2' &= y_1 + 3y_2 - 2y_3 \\
   y_3' &= y_1 + y_3
   \end{align*}
   \]
   with initial conditions:
   \[
   y_1(0) = 1, \quad y_2(0) = 1, \quad y_3(0) = -1
   \]
   - **Marks**: 8

3. **Find a General Solution to the Differential System**  
   The system is defined as:
   \[
   \begin{align*}
   y_1' &= 2y_1 + y_2 \\
   y_2' &= -y_1
   \end{align*}
   \]
   - **Marks**: 4

## Implementation/Examples
```markdown
# Example of Orthogonal Diagonalization
1. Compute the eigenvalues of matrix A.
2. Find the corresponding eigenvectors.
3. Form the orthogonal matrix Q and diagonal matrix D.
```

> [!note] **Important**: Ensure that all images submitted are clear and legible to avoid any issues with grading.

> [!warning] **Reminder**: Double-check the order of pages in your PDF before submission to ensure clarity and organization.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Differential Equations]]
- [[Linear Algebra]]