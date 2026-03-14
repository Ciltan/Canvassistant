---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 3: Euclidean Vector Spaces

## Overview
This chapter delves into the fundamental concepts of [[Euclidean Vector Spaces]], focusing on the properties and operations of vectors in \( \mathbb{R}^n \). It introduces the geometric interpretation of vectors, vector algebra, and the dot product, along with norms and distances. The chapter also explores linear combinations and spans, providing a comprehensive understanding of how vectors interact within a vector space.

## Key Concepts & Definitions
- **Vector**: A collection of \( n \) ordered real numbers, denoted as \( \mathbf{v} = (v_1, v_2, \ldots, v_n) \) where \( v_i \in \mathbb{R} \).
- **Euclidean n-space**: Denoted as \( \mathbb{R}^n \), it is the collection of all \( n \)-vectors.
- **Dot Product**: The inner product of vectors \( \mathbf{u} \) and \( \mathbf{v} \) defined as \( \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i \).
- **Norm**: The length or magnitude of a vector \( \mathbf{u} \), denoted as \( \|\mathbf{u}\| = \sqrt{\mathbf{u} \cdot \mathbf{u}} \).
- **Unit Vector**: A vector with a norm of 1, \( \|\mathbf{u}\| = 1 \).
- **Linear Combination**: A vector formed by \( c_1 \mathbf{u}_1 + c_2 \mathbf{u}_2 + \ldots + c_k \mathbf{u}_k \) where \( c_i \in \mathbb{R} \).
- **Span**: The set of all linear combinations of a set of vectors \( \text{span}\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_k\} \).

## Detailed Technical Breakdown

### 3.1 Euclidean Vector Spaces
- **Vectors**: Represented as arrows in \( \mathbb{R}^n \) with geometric interpretations.
- **Vector Algebra**:
  - **Addition**: \( \mathbf{u} + \mathbf{v} \) visualized geometrically.
  - **Scalar Multiplication**: Scaling a vector \( c\mathbf{u} \).

#### Theorems on Vector Properties
1. \( \mathbf{u} + \mathbf{v} \) is a vector in \( \mathbb{R}^n \).
2. Commutative: \( \mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u} \).
3. Associative: \( \mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w} \).
4. Zero Vector: \( \mathbf{0} + \mathbf{v} = \mathbf{v} \).
5. Negative Vector: \( -\mathbf{v} \) such that \( \mathbf{v} + (-\mathbf{v}) = \mathbf{0} \).
6. Scalar Multiplication: \( a\mathbf{v} \) is a vector in \( \mathbb{R}^n \).

### 3.2 Dot Product, Norm, Distance
- **Dot Product**: Defined for vectors \( \mathbf{u}, \mathbf{v} \in \mathbb{R}^n \).
- **Norm**: 
  - In \( \mathbb{R}^2 \): \( \text{distance} = \sqrt{x^2 + y^2} \).
  - In \( \mathbb{R}^3 \): \( \text{distance} = \sqrt{x^2 + y^2 + z^2} \).
- **Distance Between Vectors**: \( d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\| \).

> [!note] **Important**: The inner product is crucial for defining angles between vectors, where \( \cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|} \).

### 3.3 Linear Combinations and Linear Spans
- **Linear Combinations**: Formed by combining vectors with scalars.
- **Span**: The collection of all possible linear combinations of a set of vectors.

> [!warning] **Caution**: If the number of vectors exceeds the dimension of the space, the span may not cover the entire space.

## Implementation/Examples
```markdown
### Example of Dot Product
Let \( \mathbf{u} = (1, 2, -1) \) and \( \mathbf{v} = (2, 2, 2) \).
The dot product is calculated as:
\[
\mathbf{u} \cdot \mathbf{v} = (1)(2) + (2)(2) + (-1)(2) = 4.
\]
```

```markdown
### Example of Linear Combination
Consider vectors \( \mathbf{u}_1 = (1, 1) \) and \( \mathbf{u}_2 = (2, 1) \).
A linear combination could be:
\[
c_1 \mathbf{u}_1 + c_2 \mathbf{u}_2 = c_1(1, 1) + c_2(2, 1).
\]
```

## Related
- [[Logic - Propositional Logic]]
- [[Determinants]]
- [[Stacks and Queues]]
- [[Matlab+for+Engineering]]
- [[Chapter+2]]