---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - L1 Week 4 Live Lecture

## Overview
This lecture focuses on the properties of invertible matrices, specifically the matrix \( I - A \) where \( A \) is a square matrix. Key concepts include nilpotent matrices, the use of polynomial identities to demonstrate invertibility, and the application of row operations to reduce matrices to their row-echelon forms. The session also covers practical examples and problem-solving techniques relevant to linear algebra.

## Key Concepts & Definitions
- **Invertible Matrix**: A matrix \( A \) is invertible if there exists a matrix \( B \) such that \( AB = I \).
- **Nilpotent Matrix**: A square matrix \( A \) is nilpotent if there exists a positive integer \( n \) such that \( A^n = 0 \).
- **Row-Echelon Form**: A matrix is in row-echelon form if all nonzero rows are above any rows of all zeros, and the leading coefficient of a nonzero row is always to the right of the leading coefficient of the previous row.
- **Elementary Matrix**: A matrix obtained by performing a single elementary row operation on an identity matrix.

## Detailed Technical Breakdown

### Announcements
- Attempt quizzes 2.3 to 2.5, due on **Friday, 6 February 2026**.
- Homework 1 is due on **15 February**.

### Invertibility of \( I - A \)
1. **Question 1(a)**: Show that if \( A^2 = 0 \), then \( I - A \) is invertible with inverse \( I + A \).
   - To prove this, check that:
     \[
     (I - A)(I + A) = I^2 - A^2 = I
     \]

2. **Question 1(b)**: If \( A^3 = 0 \), is \( I - A \) invertible?
   - Using the polynomial identity:
     \[
     (I - A)(I + A + A^2) = I - A^3 = I
     \]
   - Thus, \( I - A \) is invertible with inverse \( I + A + A^2 \).

3. **Question 1(c)**: Show that if \( A \) is nilpotent, then \( I - A \) is invertible.
   - The inverse can be derived from the geometric series:
     \[
     (I - A)^{-1} = I + A + \cdots + A^{n-1}
     \]

### Matrix Reduction
1. **Question 2**: Reduce the following matrix \( A \) to its reduced row-echelon form \( R \).
   - **Elementary Row Operations**:
     - \( R_1 \) operations lead to the following transformations:
       - \( E_1, E_2, E_3 \) are the corresponding elementary matrices.
   - **Final Form**:
     \[
     A = E_1 E_2 E_3 R
     \]

### Example Problems
- **Question 3**: Find a cubic polynomial that passes through given points.
  - Set up the augmented matrix and reduce to find the polynomial coefficients.

### Electrical Circuit Laws
- **Ohm’s Law**: \( E = IR \)
- **Kirchhoff’s Laws**:
  - Current Law: The sum of currents entering a junction equals the sum of currents leaving.
  - Voltage Law: The sum of voltage rises equals the sum of voltage drops in a closed loop.

> [!important] **Key Takeaway**: Understanding the properties of matrices and their applications in solving linear systems is crucial for engineering applications.

## Related
- [[Logic - Propositional Logic]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Midterm+Briefing]]
- [[AY2122+Sem1+Homework+3]]