---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Final Exam Overview

## Overview
This note summarizes the final examination for the MA1508E course at the National University of Singapore, focusing on key concepts in [[Linear Algebra]]. The exam consists of four questions covering topics such as vector spaces, eigenvalues, and differential systems. Students are allowed to use MATLAB and calculators, emphasizing the importance of systematic problem-solving and clear presentation of work.

## Key Concepts & Definitions
- **Vector Space**: A collection of vectors that can be added together and multiplied by scalars, forming the basis for linear algebra.
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space.
- **Eigenvalue**: A scalar associated with a linear transformation represented by a matrix, indicating how much a corresponding eigenvector is stretched or compressed.
- **Orthogonal Complement**: The set of all vectors that are orthogonal to every vector in a given subspace.
- **Projection**: The operation of projecting a vector onto a subspace, yielding a vector in that subspace.

## Detailed Technical Breakdown

### Examination Instructions
- **Duration**: 2 hours
- **Format**: Open book, proctored via Zoom
- **Materials Allowed**: MATLAB, scientific or graphing calculators
- **Submission**: Candidates must submit a PDF of their work after the exam.

### Questions Breakdown
1. **Question 1**: Vector spaces and basis
   - Find a basis for a given vector set and determine its dimension.
   - Show that a specific vector is not in the span of the set.
   - Calculate projections and orthogonal complements.

2. **Question 2**: Markov chains and probabilities
   - Construct a transition matrix for a system of messages.
   - Find orthogonal and diagonal matrices for the transition matrix.
   - Analyze long-term probabilities of message broadcasts.

3. **Question 3**: Eigenvalues and differential systems
   - Show that a specific eigenvalue is repeated and find associated eigenvectors.
   - Solve a differential system using the fundamental set of solutions.

4. **Question 4**: Conditions for solutions of linear systems
   - Determine conditions under which a linear system has no solution or multiple parameters.
   - Explore conditions for the existence of left inverses for a matrix.

## Implementation/Examples

### Example of Finding a Basis
```matlab
% MATLAB code to find a basis for a vector space
S = [-4 0 2 -3 1 1 1; 2 0 -1 3 4 7 -2; 4 1 -2 2 3 5 -2; 6 1 -3 2 -2 -3 -1];
[~, ~, r] = svd(S); % Singular Value Decomposition
basis = S(:, 1:r); % Basis for the column space
```

> [!note] **Important**: Ensure to clearly label your work and follow the submission guidelines to avoid penalties.
> [!warning] **Reminder**: Double-check your calculations and ensure clarity in your presentation, especially when using MATLAB.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]