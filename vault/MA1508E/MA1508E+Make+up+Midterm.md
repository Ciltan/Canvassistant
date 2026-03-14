---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Midterm Make-up Test Overview

## Overview
This note summarizes the key components of the MA1508E Midterm Make-up Test for AY2022/2023 Semester 2. The test consists of three questions, covering essential concepts in [[Linear Algebra]], including systems of equations, matrix operations, and vector spaces. Students are required to demonstrate their understanding through problem-solving and application of theoretical principles.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Unique Solution**: A solution to a linear system where exactly one set of values satisfies all equations.
- **Infinitely Many Solutions**: A scenario where a linear system has multiple solutions, often described by parameters.
- **Elementary Row Operations**: Operations used to manipulate rows of a matrix to solve linear systems.
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space.
- **Nullspace**: The set of all vectors that, when multiplied by a given matrix, yield the zero vector.

## Detailed Technical Breakdown

### Instructions to Students
- Write your name, student number, and tutorial group.
- The test consists of 3 questions and is worth 50 marks.
- It is a closed book assessment; one A4 handwritten help sheet is allowed.
- Non-programmable calculators are permitted, but all workings must be shown.
- All questions must be answered.

### Question Breakdown

#### Question 1: Linear System Analysis
1. **System of Equations**:
   - \( x_1 + x_2 + x_3 = 1 \)
   - \( x_1 + ax_2 + a^2x_3 = 1 \)
   - \( ax_1 + ax_2 + a^3x_3 = a^2 + a^{-1} \)

   - **(a)** Values of \( a \) for no solution.
   - **(b)** Values of \( a \) for a unique solution and the solution itself.
   - **(c)** Values of \( a \) for infinitely many solutions with one parameter.
   - **(d)** Values of \( a \) for infinitely many solutions with two parameters.

   > [!important] Show all elementary row operations clearly.

#### Question 2: Basis and Solution Sets
1. **General Solution**:
   - Given \( x_1 = 2r + s - t, x_2 = r, x_3 = s, x_4 = t \) where \( r, s, t \in \mathbb{R} \).
   - Let \( V \) be the solution set.

   - **(a)** Find a \( 2 \times 4 \) matrix \( A \) with non-zero entries such that \( Ax = b \) has the given general solution.
   - **(b)** Show that \( T = \{v_1, v_2, v_3\} \) is a basis for \( V \).
   - **(c)** Find the transformations of vectors \( w_1, w_2, w_3 \) and show operations clearly.
   - **(d)** Given \( S \) is a basis for \( V \), find the transformation of a vector \( u \) in \( V \).

#### Question 3: Matrix Properties
1. **Matrix Analysis**:
   - Given matrix \( A \) and conditions for singularity.

   - **(a)** Find values of \( a \) such that \( A \) is singular using row operations.
   - **(b)** Determine \( b \) and \( c \) based on the nullspace condition.
   - **(c)** 
     - **i.** Determine the rank and nullity of \( A \).
     - **ii.** Find \( s, t \) such that a specific vector is a solution to \( Ax = b \).

## Implementation/Examples
```plaintext
1. For Question 1, apply Gaussian elimination to determine the conditions for solutions.
2. For Question 2, construct matrix \( A \) and validate the basis using linear independence.
3. For Question 3, perform row reduction to find singularity conditions.
```

> [!note] Ensure to indicate any rough work clearly on the back of the pages.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]