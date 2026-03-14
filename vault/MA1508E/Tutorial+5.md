---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 5

## Overview
This tutorial focuses on the concepts of vector spans, subspaces, linear independence, and linear combinations within the context of linear algebra. Students will explore geometric interpretations of spans, determine subspaces, and analyze sets of vectors for linear independence. The tutorial also includes supplementary problems that reinforce the understanding of homogeneous linear systems and their properties.

## Key Concepts & Definitions
- **Span**: The set of all possible linear combinations of a given set of vectors. [[span]]
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. [[subspace]]
- **Linear Independence**: A set of vectors is linearly independent if no vector can be expressed as a linear combination of the others. [[linear-independence]]
- **Homogeneous Linear System**: A system of linear equations that can be expressed in the form \(Ax = 0\). [[homogeneous-linear-system]]

## Detailed Technical Breakdown

### 1. Span Relationships
- **Problem 1**: Determine if \( \text{span}\{u_1, u_2, u_3\} \subseteq \text{span}\{v_1, v_2\} \) and/or \( \text{span}\{v_1, v_2\} \subseteq \text{span}\{u_1, u_2, u_3\} \).
  - **Vectors**:
    - (i) \( u_1 = \begin{pmatrix} 2 \\ -2 \\ 0 \end{pmatrix}, u_2 = \begin{pmatrix} -1 \\ 1 \\ -1 \end{pmatrix}, u_3 = \begin{pmatrix} 0 \\ 9 \\ 1 \end{pmatrix}, v_1 = \begin{pmatrix} -1 \\ 0 \\ 1 \end{pmatrix}, v_2 = \begin{pmatrix} 1 \\ -5 \\ 0 \end{pmatrix} \)
    - (ii) \( u_1 = \begin{pmatrix} 6 \\ 4 \\ 2 \end{pmatrix}, u_2 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} 4 \\ -1 \\ 5 \end{pmatrix}, v_1 = \begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, v_2 = \begin{pmatrix} 8 \\ -5 \\ 9 \end{pmatrix} \)

### 2. Geometric Interpretation of Span
- Describe the geometric nature of \( \text{span}\{u_1, u_2, u_3\} \) and \( \text{span}\{v_1, v_2\} \).
- If either span forms a plane, derive the equation of that plane.

### 3. Subspace Determination
- **Problem 2**: Identify which of the following sets are subspaces and express them as linear spans if applicable:
  - (a) \( S = \{ \begin{pmatrix} p \\ q \\ p \\ q \end{pmatrix} | p, q \in \mathbb{R} \} \)
  - (b) \( S = \{ \begin{pmatrix} a \\ b \\ c \end{pmatrix} | a \geq b \text{ or } b \geq c \} \)
  - (c) \( S = \{ \begin{pmatrix} x \\ y \\ z \\ w \end{pmatrix} | 4x = 3y \text{ and } 2x = -3w \} \)
  - (d) \( S = \{ \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} | \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} = 0 \} \)
  - (e) \( S = \{ \begin{pmatrix} w \\ x \\ y \\ z \end{pmatrix} | w + x = y + z \} \)
  - (f) \( S = \{ \begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} | ab = cd \} \)
  - (g) \( S \) is the solution set of \( Ax = 0 \) where \( A \) is defined as above.

### 4. Linear Independence Analysis
- **Problem 3**: For each set of vectors \( S \):
  - (i) Determine if \( S \) is linearly independent.
  - (ii) If dependent, express one vector as a linear combination of others.

### 5. Basis for Subspaces
- **Problem 4**: For each subspace \( V \), provide a basis:
  - (a) \( V = \{ \begin{pmatrix} a+b \\ a+c \\ c+d \\ b+d \end{pmatrix} | a, b, c, d \in \mathbb{R} \} \)
  - (b) \( V = \text{span}\{ \begin{pmatrix} 1 \\ 0 \\ -1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 2 \\ 3 \\ -1 \end{pmatrix} \} \)
  - (c) Solution space of a homogeneous linear system.

### 6. Linear Combinations
- **Problem 5**: Express \( u \) as a linear combination of \( v_1, v_2, v_3, v_4 \) in two distinct ways and analyze the uniqueness of this representation.

## Implementation/Examples
```matlab
% MATLAB code for problem 6(d)
A = magic(10);
b = ones(10, 1);
```

> [!note] **Key Insight**: A vector \( u \in \text{span}\{v_1, v_2, \ldots, v_k\} \) has a unique linear combination expression if and only if the set \( \{v_1, v_2, \ldots, v_k\} \) is linearly independent.

> [!important] **Homogeneous Systems**: The solution set to any homogeneous linear system \( S = \{ v \in \mathbb{R}^n | Av = 0 \} \) is a subspace.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Matlab+for+Engineering]]
- [[Determinants]]