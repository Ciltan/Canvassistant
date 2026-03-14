---
module: MA1522
course: MA1522 Linear Algebra for Computing [2520]
date: 2026-03-14
source: Tutorial14.pdf
tags: [ma1522, lecture-notes, auto-generated]
up: "[[MOD_INDEX]]"
---

# Coordinates and Orthogonal Projections in Linear Algebra

> [!info] Navigation
> ↑ Back to [[MOD_INDEX]]

## Summary
This lecture focuses on understanding coordinates relative to an orthogonal basis, orthogonal projections onto subspaces, and applying the Gram-Schmidt process to obtain orthogonal sets. These concepts are essential for simplifying computations and understanding vector spaces within the context of linear algebra, especially regarding applications in computing.

## Key Concepts
- Orthogonal Basis — A basis where all vectors are [[orthogonal]] to each other.
- Orthogonal Projection — A vector projection onto a subspace spanned by orthogonal vectors.
- Gram-Schmidt Process — A method to convert a set of vectors into an [[orthogonal basis]].

## Detailed Notes

### Coordinates Relative to an Orthogonal Basis
Given an orthogonal subset $S = \{u_1, u_2, \ldots, u_k\} \subset \mathbb{R}^n$ where $u_i \neq 0$ for all $i$, $S$ is linearly independent and can act as a basis for $\text{span}(S)$. A vector $v \in \text{span}(S)$ can be represented as:

$$
v = \frac{v \cdot u_1}{\|u_1\|^2} u_1 + \frac{v \cdot u_2}{\|u_2\|^2} u_2 + \cdots + \frac{v \cdot u_k}{\|u_k\|^2} u_k
$$

The coordinate vector of $v$ relative to $S$ is $\left[\frac{v \cdot u_1}{\|u_1\|^2}, \frac{v \cdot u_2}{\|u_2\|^2}, \ldots, \frac{v \cdot u_k}{\|u_k\|^2}\right]^T$.

### Orthogonal Projection onto a Subspace
For $S = \{u_1, u_2, \ldots, u_k\}$, the orthogonal projection of $v \in \mathbb{R}^n$ onto $\text{span}(S)$ is:

$$
v_p = \frac{v \cdot u_1}{\|u_1\|^2} u_1 + \frac{v \cdot u_2}{\|u_2\|^2} u_2 + \cdots + \frac{v \cdot u_k}{\|u_k\|^2} u_k
$$

**Theorem**: 
1. $v \in \text{span}(S)$ if and only if $v = v_p$.
2. For $u \in \text{span}(S)$, $u=v \Leftrightarrow \|v\|^2 = \|v-u\|^2+\|u\|^2 \Leftrightarrow (v-u) \cdot u_i = 0$ for all $i$.

### Gram-Schmidt Process
The Gram-Schmidt Process generates an orthogonal basis for $\text{span}(S)$. Let $S = \{u_1, u_2, \ldots, u_k\}$. Define:
- $v_1 = u_1$
- $v_i = u_i - \sum_{j=1}^{i-1} \frac{u_i \cdot v_j}{\|v_j\|^2} v_j$

The process recursively removes components along existing vectors to ensure orthogonality.

## Worked Examples

### Example 1 - Orthogonal Basis
Given $S = \{v_1, v_2, v_3, v_4\}$, verify $S$ is orthogonal:
- $v_1 = (1,2,2,-1)$, $v_2 = (1,1,-1,1)$, $v_3 = (-1,1,-1,-1)$, $v_4 = (-2,1,1,2)$
- Check: All dot products $v_i \cdot v_j = 0$ for $i \neq j$.
- Thus, $S$ is orthogonal and forms a basis for $\mathbb{R}^4$.

### Example 2 - Projection Calculation
For $S = \{w_1, w_2, w_3\}$ and $v = (2,0,1,1,-1)$:
- $w_1 = (1,1,1,1,1)$, $w_2 = (1,2,-1,-2,0)$, $w_3 = (1,-1,1,-1,0)$
- Compute projection $p$ onto $\text{span}(S)$:
  - Calculate: $p = \sum_{i=1}^3 \frac{v \cdot w_i}{\|w_i\|^2} w_i$
- Verify $v-p$ is orthogonal to $S$.

### Example 3 - Gram-Schmidt Transformation
Transform the set $\{u_1, u_2, u_3, u_4\}$ into an orthogonal set:
- Use Gram-Schmidt to recursively remove parallel components.

## Exam Relevance
> [!warning] Exam Topics
> - Definition and properties of orthogonal bases
> - Computing coordinates relative to an orthogonal basis
> - Calculating orthogonal projections
> - Applying the Gram-Schmidt process
> - Understanding the implications of orthogonality in vector spaces

The next lesson will cover sections 5.4 and 5.5.