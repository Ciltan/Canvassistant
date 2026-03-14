---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Final Exam Overview

## Overview
This note summarizes the final exam for MA1508E, focusing on key concepts and problem-solving techniques in linear algebra. The exam consists of multiple-choice questions (MCQs) and short answer questions that assess students' understanding of vector spaces, matrix operations, and differential equations. Students are encouraged to systematically lay out their solutions and utilize any offline calculators during this open-book assessment.

## Key Concepts & Definitions
- **Vector Space**: A collection of vectors that can be added together and multiplied by scalars.
- **Eigenvalue**: A scalar associated with a linear transformation represented by a matrix, indicating the factor by which the eigenvector is scaled.
- **Null Space**: The set of all vectors that, when multiplied by a given matrix, yield the zero vector.
- **Row Space**: The space spanned by the rows of a matrix.
- **Projection**: The operation of projecting a vector onto a subspace, often calculated using orthogonal components.
- **Characteristic Polynomial**: A polynomial which is derived from the determinant of a matrix and used to find eigenvalues.

## Detailed Technical Breakdown

### Exam Structure
- **Duration**: 2 hours
- **Format**: Open book, non-secure block internet assessment
- **Content**:
  - 15 Multiple Choice Questions (MCQs)
  - 5 Short Answer Questions

### Sample Problems
1. **Vector Solutions**:
   - Given vectors \( a_1, a_2, a_3 \) in \( \mathbb{R}^3 \) and a matrix \( A \), determine solutions to \( Ax = b \) where \( b \) is a linear combination of the vectors.
   - **Solution**: Identify that \( b \) can be expressed as \( A \) multiplied by a vector in the null space.

2. **Population Distribution**:
   - Analyze migration patterns between three cities using a probability transition matrix.
   - **Solution**: Calculate the equilibrium distribution using eigenvalues and eigenvectors.

3. **Basis for Vector Spaces**:
   - Determine a basis for a given vector space defined by polynomial equations.
   - **Solution**: Use linear independence criteria to select appropriate vectors.

4. **Projection onto Subspaces**:
   - Find the projection of a vector onto a defined vector space.
   - **Solution**: Utilize the formula for projection involving dot products and normalization.

5. **Row Space Identification**:
   - Identify which vectors belong to the row space of a given matrix.
   - **Solution**: Use row reduction techniques to analyze the row space.

### Implementation/Examples
```matlab
% Example MATLAB code for calculating eigenvalues and eigenvectors
A = [0.95 0.05 0.02; 0.03 0.94 0.05; 0.02 0.01 0.93];
[P, D] = eig(A);
equilibrium_distribution = P(:,1) / sum(P(:,1));
```

> [!note] **Important**: Ensure to write answers clearly and systematically in the provided answer booklet. 
> [!warning] **Caution**: Do not exit the Examplify platform until instructed, as this may affect your submission.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[MA1508E+AY2122Sem1]]
- [[Tutorial+1+Solution]]