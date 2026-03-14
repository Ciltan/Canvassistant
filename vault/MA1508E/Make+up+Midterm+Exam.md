---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Make-up Midterm Exam Overview

## Overview
The make-up midterm exam for MA1508E consists of six questions, totaling 60 marks, and is designed to assess students' understanding of key concepts in linear algebra. The exam covers systems of equations, matrix properties, subspaces, and applications of linear transformations. Students are required to demonstrate their problem-solving skills and theoretical knowledge within a 1.5-hour timeframe.

## Key Concepts & Definitions
- **Row Echelon Form (REF)**: A matrix form where all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row. See [[AY2122+Sem1+Homework+3]].
- **Nullspace**: The set of all vectors that, when multiplied by a given matrix, yield the zero vector. Refer to [[Determinants]] for related concepts.
- **Column Space**: The span of the columns of a matrix, representing all possible linear combinations of its column vectors. See [[Stacks and Queues]] for applications.
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. Explore more in [[ch2]].
- **Homogeneous System**: A system of linear equations that equates to zero. This is crucial in understanding solutions to systems, as discussed in [[Logic - Propositional Logic]].

## Detailed Technical Breakdown

### Exam Structure
- **Total Questions**: 6
- **Total Marks**: 60
- **Time Allowed**: 1 hour 30 minutes

### Question Breakdown
1. **System of Equations** (15 points)
   - Analyze the system for conditions of inconsistency, unique solutions, and infinite solutions.
   - Derive values for parameters \(a\) and \(b\).

2. **Matrix Analysis** (10 points)
   - Given a 3x5 matrix in REF, find bases for the nullspace and column space.
   - Determine a right inverse of the matrix.

3. **Homogeneous Systems** (10 points)
   - Provide examples of matrices with non-trivial solutions.
   - Calculate the basis for Row space and nullity.

4. **Matrix Powers** (5 points)
   - Compute \(A^{1508E}\) for a given matrix \(A\) without direct computation in MATLAB.

5. **Subspace Determination** (15 points)
   - Assess various sets for subspace properties and find bases where applicable.

6. **Euler's Problem** (5 points)
   - Solve a classic problem involving the purchase of livestock under specific constraints.

## Implementation/Examples

### Example of a System of Equations
```markdown
Consider the system:
1. \(x_1 + ax_2 + (a-1)x_3 + bx_4 = a\)
2. \(x_1 + 2ax_2 + (a-1)x_3 + (2b-a)x_4 = a-b\)
3. \(x_1 + ax_2 + bx_4 = a-b\)
4. \(x_1 + 2ax_2 + (a-1)x_3 + 2bx_4 = 2a-b\)

To find values of \(a\) and \(b\):
- (a) Inconsistent: Set conditions leading to no solutions.
- (b) Unique solution: Identify specific values of \(a\) and \(b\).
- (c) Infinite solutions with 1 parameter: Derive general solution.
- (d) Infinite solutions with 2 parameters: Derive general solution.
```

> [!important] Ensure to write answers on separate pages and submit scripts at the end of the exam.

> [!note] Remember, you cannot exit Examplify until provided with the exit password.

## Related
- [[MA1508E+AY2122Sem1]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[AY2122+Sem2+Homework+3(S)]]
- [[Lab+Seating+Allocations]]