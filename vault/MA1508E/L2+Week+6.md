---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - L2 Week 6 Live Lecture

## Overview
This lecture focuses on key concepts in linear algebra, particularly determinants and their properties. Students are reminded of upcoming assessments and are encouraged to engage with problem-solving activities. The lecture also covers the implications of matrix properties such as invertibility and nilpotency, providing a foundation for understanding linear transformations and their applications in engineering.

## Key Concepts & Definitions
- **Determinant**: A scalar value that is a function of a square matrix, denoted as [[det(A)]].
- **Invertible Matrix**: A matrix that has an inverse, denoted as [[A^(-1)]].
- **Nilpotent Matrix**: A square matrix A such that [[A^k]] = 0 for some positive integer k.
- **Orthogonal Matrix**: A square matrix A satisfying [[A^T]] = [[A^(-1)]].
- **Diagonal Matrix**: A matrix in which the entries outside the main diagonal are all zero.
- **Gaussian Elimination**: A method for solving systems of linear equations.

## Detailed Technical Breakdown

### Announcements
- **Quizzes**: Complete quizzes 3.1 to 3.4 by February 20, 2026.
- **Problem Solving Submission**: Due by Friday at 11:59 PM; hints will be provided via Telegram.
- **Recess Week**: No lessons next week.
- **Midterm Exam**: Scheduled for March 13, 2026, from 19:00 to 20:00 at MPSH.

### Determinant Properties
1. **Determinant of a Product**:
   - For matrices A and B, [[det(AB)]] = [[det(A)det(B)]].
   
2. **Determinant of a Diagonal Matrix**:
   - If A = PDP^(-1), then [[det(A)]] = [[det(D)]].
   - If D is diagonal with entries d₁, d₂, ..., dₙ, then:
     - [[det(D)]] = d₁ * d₂ * ... * dₙ.
   - A is invertible if and only if all diagonal entries of D are nonzero.

3. **Nilpotent Matrices**:
   - If A is nilpotent, then [[det(A)]] = 0.

4. **Orthogonal Matrices**:
   - If A is orthogonal, then [[det(A)]] = ±1.

### Example Problems
- **Question 1(a)**: Show that if A = PDP^(-1), then [[det(A)]] = [[det(D)]].
  
  ```markdown
  det(A) = det(PDP^(-1)) = det(P)det(D)det(P^(-1)) = det(P)det(P^(-1))det(D) = det(D).
  ```

- **Question 1(b)**: Prove A is invertible if and only if all diagonal entries of D are nonzero.
  
  ```markdown
  det(A) = d₁ * d₂ * ... * dₙ, where dᵢ ≠ 0 for all i.
  ```

- **Question 1(c)**: Show that if A is nilpotent, then [[det(A)]] = 0.
  
  ```markdown
  0 = det(A^k) = det(A)^k ⇒ det(A) = 0.
  ```

- **Question 1(d)**: Prove that if A is orthogonal, then [[det(A)]] = ±1.
  
  ```markdown
  1 = det(A^(-1)A) = det(A^T)det(A) = det(A)^2 ⇒ det(A) = ±1.
  ```

## Implementation/Examples
### Gaussian Elimination Example
To determine if the matrix A is invertible:
```markdown
A = | -1  3 -4 |
    |  2  4  1 |
    | -4  2 -9 |

Use Gaussian elimination to find the determinant.
```

### Solution Set Notation
For the linear system:
```markdown
a + b - c - 2d = 0
2a + b - c + d = -2
-a + b - 3c + d = 4

General solution: a = -2 - 3s, b = 2 + 19s, c = 9s, d = s, s ∈ R.
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[CS1231+TUTORIAL+3]]