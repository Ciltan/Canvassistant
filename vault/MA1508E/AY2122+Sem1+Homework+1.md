---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 1 - Homework 1 Overview

## Overview
This note summarizes the key components of Homework 1 for the MA1508E course at the National University of Singapore. The homework consists of three main questions focusing on augmented matrices, linear systems, and matrix equations. Students are required to demonstrate their understanding of [[Determinants]], [[Logic - Propositional Logic]], and elementary row operations while adhering to specific submission guidelines.

## Key Concepts & Definitions
- **Augmented Matrix**: A matrix that includes the coefficients of a linear system along with the constants from the equations.
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to simplify it, including row swapping, scaling, and row addition.
- **Matrix Equation**: An equation in the form of \(Ax = b\), where \(A\) is a matrix, \(x\) is a vector of variables, and \(b\) is a result vector.
- **Consistent System**: A system of equations that has at least one solution.
- **Unique Solution**: A solution to a system of equations where exactly one set of values satisfies all equations.

## Detailed Technical Breakdown

### Submission Guidelines
- Use A4 size paper.
- Clearly write your student number and name on the top left corner of each page.
- Include page numbers on the top right corner.
- Total of 20 marks distributed across three questions.
- Submit a merged PDF of your work named as "StudentNo P1" in the LumiNUS folder.

### Question Breakdown

1. **Augmented Matrix Analysis** (8 marks)
   - Given the matrix:
     \[
     \begin{pmatrix}
     1 & 1 & 1 & a \\
     1 & a & 2-a & 0 \\
     1 & a & a+2 & 2a
     \end{pmatrix}
     \]
   - **(i)** Conditions for no solution.
   - **(ii)** Conditions for a unique solution and the solution itself.
   - **(iii)** Conditions for infinitely many solutions, including a general and particular solution.

2. **Linear System Evaluation** (6 marks)
   - Given the system:
     \[
     \begin{align*}
     x_1 - x_2 + x_3 &= -1 \\
     2x_1 - x_2 - x_3 &= 1 \\
     x_2 + 2x_3 &= 1 \\
     x_1 + 2x_2 &= 1 \\
     x_1 + x_3 &= 1
     \end{align*}
     \]
   - **(i)** Write the corresponding matrix equation \(Ax = b\) and check for consistency.
   - **(ii)** Compute \(A^TA\) and \(A^Tb\) and find a solution for \(A^TAx = A^Tb\).
   - **(b)** Write a linear system with the general solution:
     \[
     \begin{align*}
     x_1 &= -s + 2t \\
     x_2 &= s - t \\
     x_3 &= s \\
     x_4 &= t
     \end{align*}
     \]

3. **Matrix Commutativity** (5 marks)
   - Given \(A = \begin{pmatrix} 2 & 1 \\ c & d \end{pmatrix}\), find all matrices \(B\) such that \(AB = BA\).

## Implementation/Examples

```markdown
# Example of Augmented Matrix Operations
1. Start with the augmented matrix:
   \[
   \begin{pmatrix}
   1 & 1 & 1 & a \\
   1 & a & 2-a & 0 \\
   1 & a & a+2 & 2a
   \end{pmatrix}
   \]
2. Apply elementary row operations to simplify.
```

> [!note] Remember to clearly document each elementary row operation used in your calculations.
> [!important] Ensure that your PDF submission is clear and in the correct order to avoid any issues with grading.

## Related
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem1+Homework+3]]
- [[Midterm+Briefing]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]