---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 10

## Overview
This tutorial focuses on the application of the [[Cayley-Hamilton theorem]] and the concept of [[Markov chains]]. It explores the computation of characteristic polynomials, the invertibility of matrices, and the behavior of systems modeled by stochastic matrices. Additionally, it addresses diagonalization of matrices and the properties of eigenvectors associated with symmetric matrices.

## Key Concepts & Definitions
- **Cayley-Hamilton theorem**: States that every square matrix satisfies its own characteristic polynomial.
- **Markov chain**: A stochastic process where the next state depends only on the current state, not on the sequence of events that preceded it.
- **Transition probability matrix**: A matrix that describes the probabilities of transitioning from one state to another in a Markov chain.
- **Stochastic matrix**: A square matrix used to describe the transitions of a Markov chain, where each column sums to 1.
- **Eigenvector**: A non-zero vector that changes by only a scalar factor when a linear transformation is applied.
- **Diagonalizable matrix**: A matrix that can be expressed in the form \( PDP^{-1} \), where \( D \) is a diagonal matrix.

## Detailed Technical Breakdown

### 1. Cayley-Hamilton Theorem
- **Problem Statement**:
  - Given \( p(X) = X^3 - 4X^2 - X + 4I \), compute \( p(X) \) for \( X = \begin{pmatrix} 1 & 1 & 2 \\ 2 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \).
  - Find the characteristic polynomial of \( X \).
  - Show that \( X \) is invertible and express its inverse as a function of \( X \).

### 2. Markov Chain
- **Example**: Ants in a maze with compartments \( a, b, c \).
  - Transition probabilities:
    - From \( a \): 20% to \( b \), 40% to \( c \).
    - From \( b \): 10% to \( a \), 30% to \( c \).
    - From \( c \): 50% to \( a \), 20% to \( b \).
  - Initial state vector: \( x_0 = \begin{pmatrix} 100 \\ 0 \\ 0 \end{pmatrix} \).
  
#### (a) Transition Probability Matrix
- Construct matrix \( A \) and verify it is a regular stochastic matrix.

#### (b) Diagonalization of \( A \)
- Find the number of ants in each compartment after 3 hours.

#### (c) MATLAB Implementation
```matlab
[P, D] = eig(A)
```
- Compare results with manual calculations.

#### (d) Long-term Behavior
- Determine where the majority of ants will be in the long run.

#### (e) Equilibrium Distribution
- Define equilibrium distribution and relate it to the long-term population distribution.

#### (f) Non-equilibrium Distribution
- Discuss the possibility of having a non-equilibrium distribution eigenvector.

### 3. Diagonalizability of Matrices
- **(a)** Show that the only diagonalizable nilpotent matrix is the zero matrix.
- **(b)** Prove that the only diagonalizable matrix with a single eigenvalue \( \lambda \) is the scalar matrix \( \lambda I \).

### 4. Matrix Properties
- **(a)** Analyze matrix \( A = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 0 & 2 \\ 1 & 0 & 3 \end{pmatrix} \) for diagonalizability and invertibility.
- **(b)** Find a matrix \( B \) such that \( B^2 = A \).

### 5. Orthogonal Diagonalization
- For symmetric matrices, find orthogonal matrices \( P \) that diagonalize \( A \).

### Supplementary Problems
- **(6)** Recursive sequence analysis.
- **(7)** Properties of stochastic matrices.
- **(8)** Tiling problem with colored tiles.
- **(9)** Orthogonality of eigenvectors associated with distinct eigenvalues.

> [!important] The Cayley-Hamilton theorem is crucial for understanding matrix behavior in linear algebra, particularly in engineering applications.
> [!note] Markov chains provide a powerful framework for modeling systems that evolve over time based on probabilistic rules.

## Related
- [[Cayley-Hamilton theorem]]
- [[Markov chains]]
- [[Stochastic matrices]]
- [[Eigenvalues and Eigenvectors]]
- [[Diagonalization of matrices]]