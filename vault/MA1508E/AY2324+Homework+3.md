---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 3

## Overview
This document outlines the requirements and tasks for Homework 3 in the MA1508E course at the National University of Singapore. The homework involves various mathematical problems, including finding orthonormal sets, analyzing telecommunication subscriber dynamics, and solving a differential system. Students are expected to demonstrate their workings clearly and utilize MATLAB for calculations where applicable.

## Key Concepts & Definitions
- **Orthonormal Set**: A set of vectors that are both orthogonal and normalized. [[Orthonormality]]
- **Projection**: The process of projecting a vector onto a subspace. [[Projection]]
- **Eigenvalue**: A scalar associated with a linear transformation represented by a matrix, indicating how much a corresponding eigenvector is stretched or compressed. [[Eigenvalue]]
- **Differential System**: A set of differential equations that describe the behavior of a system over time. [[Differential Equations]]
- **Upper Triangular Matrix**: A type of matrix where all entries below the main diagonal are zero. [[Upper Triangular Matrix]]

## Detailed Technical Breakdown

### Submission Guidelines
- Answers must be written on A4 size papers or typed digitally.
- Each page should have the page number on the top right corner.
- MATLAB may be used for calculations, but all workings must be shown clearly.
- If handwritten, scan or photograph the work and merge into a single PDF.
- If typed, print to PDF.
- Name the PDF file as `StudentNo HW3.pdf` (e.g., `A1234567Z HW3.pdf`).
- Submit the PDF file to Canvas assignments under Homework 3.

### Problem Breakdown

#### Problem 1: Orthonormal Set and Projections
1. **Finding Orthonormal Set** (5 points)
   - Given vectors \( a_1, a_2, a_3, a_4 \), find an orthonormal set \( \{q_1, q_2, q_3, q_4\} \) such that:
     \[
     \text{span}\{a_1, a_2, a_3, a_4\} = \text{span}\{q_1, q_2, q_3, q_4\}
     \]
   - Show all workings clearly.

2. **Matrix Decomposition** (5 points)
   - Let \( A = [a_1, a_2, a_3, a_4] \) and \( Q = [q_1, q_2, q_3, q_4] \). Write \( A = QR \) for some upper triangular matrix \( R \).
   - Explain the derivation of your answer.

3. **Projection Calculation** (2 points)
   - Find the projection of \( \begin{pmatrix} 3 \\ 1 \\ 1 \end{pmatrix} \) onto \( V = \text{span}\{q_1, q_2, q_3, q_4\} \).
   - Show all workings clearly.

#### Problem 2: Telecommunication Subscribers
1. **Subscriber Proportions After 5 Years** (3 points)
   - Given the transition rates between telcos A, B, and C, calculate the proportion of subscribers after 5 years, starting with \( \frac{1}{3} \) of the population for each telco.
   - Explain your derivation.

2. **Long-term Subscriber Distribution** (5 points)
   - Determine which telco will have the most subscribers in the long run and explain your reasoning.

#### Problem 3: Differential System
1. **Complex Eigenvalue** (4 points)
   - Show that \( 2+i \) is a complex eigenvalue of matrix \( A \). Use this eigenvalue to find a complex solution to the differential system.

2. **Independent Real Solutions** (2 points)
   - Construct 2 independent real solutions from the complex solution found in part (a).

3. **Eigenvector Verification** (2 points)
   - Show that \( \begin{pmatrix} 1 \\ 1 \end{pmatrix} \) is an eigenvector of \( A \) and identify the associated eigenvalue.

4. **Generalized Eigenvector** (4 points)
   - Use the eigenvalue from part (c) to find a generalized eigenvector. Show workings clearly.

5. **Final Solution to Initial Value Problem** (6 points)
   - Use the results from parts (a) to (e) to solve the initial value problem. Show all workings clearly.

> [!important] Remember to clearly label all parts of your submission and ensure that your calculations are easy to follow.  
> [!note] Utilize MATLAB effectively to assist with calculations, but do not rely solely on it for your answers.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Differential Equations]]
- [[Eigenvalue]]