---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Midterm Exam Overview

## Overview
This note summarizes the key components and solutions from the Midterm Exam for MA1508E - Linear Algebra for Engineering, conducted in AY2023/2024 Semester 2. The exam consisted of multiple-choice questions (MCQs) and short answer questions, focusing on linear systems, determinants, and matrix operations. The solutions provided illustrate the application of linear algebra concepts in problem-solving.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables. [[Linear Algebra]]
- **Determinant**: A scalar value that is a function of the entries of a square matrix and provides important properties about the matrix, such as whether it is invertible. [[Determinants]]
- **Row Echelon Form (REF)**: A form of a matrix where all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row. [[Row Echelon Form]]
- **Cramer's Rule**: A mathematical theorem used to solve a system of linear equations with as many equations as unknowns, using determinants. [[Cramer's Rule]]

## Detailed Technical Breakdown

### Exam Structure
- **Duration**: 1 hour 30 minutes
- **Format**: 
  - 15 Multiple Choice Questions (MCQs)
  - 3 Short Answer Questions
- **Submission**: Answers to MCQs submitted via Examplify; short answers written in a provided booklet.

### Sample Problems and Solutions

1. **Linear System Problem**
   - Given the system:
     ```
     x + ay + az = 1
     3x + 3y + 3az = 3 - 3a
     x + y + 2z = 3 - 2a
     2x + (a+1)y + (a+2)z = 4 - 2a
     ```
     If \( z = 3 \), find \( x \).
   - **Solution**: 
     - After applying row operations, we find \( x = -9 \).

2. **Quadratic System Problem**
   - Given the equations:
     ```
     x^2 + 2y^2 - z^2 + xy - xz = 1
     x^2 + y^2 + 2z^2 + xy = 11
     ```
     If \( z > 1 \), determine the conditions on \( x \) and \( y \).
   - **Solution**: 
     - The correct conclusion is \( x > 0, y < 1 \).

3. **Coin Problem**
   - A bag contains coins totaling $10 with 32 coins in total. Determine the number of 50 cent coins.
   - **Solution**: 
     - The answer is 8 coins.

4. **Matrix Product Problem**
   - Given matrices \( A \) and \( B \), determine properties of the product \( AB \).
   - **Solution**: 
     - \( AB \) is not invertible.

5. **Consistency of Linear Systems**
   - Analyze the consistency of the system:
     ```
     Ax = b
     ```
   - **Solution**: 
     - The system is consistent if the last column of the REF of \( (A | b) \) is not a pivot column.

> [!important] 
> Ensure to practice solving linear systems and understanding the implications of determinants on matrix properties.

## Implementation/Examples
```matlab
syms a;
A = [1 a a 1; 3 3 3*a 3-3*a; 1 1 2 3-2*a; 2 a+1 a+2 4-2*a];
A(2,:) = A(2,:) - 3*A(1,:);
A(3,:) = A(3,:) - A(1,:);
A(4,:) = A(4,:) - 2*A(1,:);
A(4,:) = A(4,:) - A(3,:);
A(3,:) = A(3,:) - A(2,:)/3;
rref(A)
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[MA1508E+AY2122Sem1]]