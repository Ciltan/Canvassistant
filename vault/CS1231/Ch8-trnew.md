---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 8: Relations

## Overview
This chapter delves into the concept of [[relations]] in set theory, defining binary relations and their properties. It explores various types of relations, including reflexive, symmetric, antisymmetric, and transitive relations, along with their representations through arrow diagrams, matrices, and digraphs. Understanding these concepts is crucial for grasping more complex mathematical structures and their applications.

## Key Concepts & Definitions
- **Binary Relation**: A subset of the Cartesian product of two sets A and B, denoted as R on A × B.
- **Related Elements**: We say an element \( a \) is related to \( b \) if \( (a, b) \in R \).
- **Reflexive Relation**: A relation R on a set A is reflexive if \( \forall x \in A, (x, x) \in R \).
- **Symmetric Relation**: A relation R is symmetric if \( \forall x, y \in A, (x, y) \in R \implies (y, x) \in R \).
- **Antisymmetric Relation**: A relation R is antisymmetric if \( \forall x, y \in A, (x, y) \in R \land (y, x) \in R \implies x = y \).
- **Transitive Relation**: A relation R is transitive if \( \forall x, y, z \in A, (x, y) \in R \land (y, z) \in R \implies (x, z) \in R \).

## Detailed Technical Breakdown

### Definitions of Relations
1. **Binary Relation**: 
   - Let \( A, B \) be sets. A binary relation \( R \) on \( A \times B \) is defined as a subset of \( A \times B \).
   - Notation: \( xRy \) if \( (x, y) \in R \) and \( xR/y \) if \( (x, y) \notin R \).

2. **Examples of Relations**:
   - Let \( A = \{0, 1, 2\} \) and \( B = \{1, 2, 3\} \). Define \( xRy \) if \( x < y \). Then:
     - \( R = \{(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)\} \)
   - Let \( E \) be the relation on \( \mathbb{Z} \) defined by \( E = \{(x, y) : x \equiv y \mod 2\} \).

### Properties of Relations
- **Reflexive**: \( (x, x) \in R \) for all \( x \in A \).
- **Symmetric**: If \( (x, y) \in R \), then \( (y, x) \in R \).
- **Antisymmetric**: If \( (x, y) \in R \) and \( (y, x) \in R \), then \( x = y \).
- **Transitive**: If \( (x, y) \in R \) and \( (y, z) \in R \), then \( (x, z) \in R \).

### Representation of Relations
1. **Arrow Diagram**: 
   - A visual representation where an arrow from \( a \) to \( b \) indicates \( (a, b) \in R \).
   - Example: For \( R = \{(1, x), (1, y), (2, x), (2, y), (2, z), (3, z), (4, z)\} \).

2. **Matrix Representation**:
   - A relation can be represented as a matrix \( M \) where the entry \( M_{ij} = 1 \) if \( (a_i, a_j) \in R \) and \( 0 \) otherwise.
   - Theorems regarding matrix properties:
     - \( R \) is symmetric if \( M \) is symmetric.
     - \( R \) is reflexive if all diagonal entries are 1.
     - \( R \) is antisymmetric if \( M_{ij} + M_{ji} \leq 1 \) for all \( i \neq j \).

3. **Digraph Representation**:
   - A directed graph where vertices represent elements of \( A \) and directed edges represent the relation \( R \).
   - Properties:
     - Reflexive if every vertex has a loop.
     - Symmetric if for every directed edge \( (a, b) \), there is also \( (b, a) \).
     - Antisymmetric if \( (a, b) \) implies no \( (b, a) \) unless \( a = b \).
     - Transitive if \( (a, b) \) and \( (b, c) \) imply \( (a, c) \).

> [!note] **Important**: Understanding these properties is essential for analyzing complex structures in mathematics and computer science, particularly in graph theory and database relations.

> [!warning] **Caution**: Misidentifying the properties of a relation can lead to incorrect conclusions in proofs and applications.

## Implementation/Examples
```python
# Example of a simple relation in Python
A = {0, 1, 2}
B = {1, 2, 3}
R = {(x, y) for x in A for y in B if x < y}
print(R)  # Output: {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
```

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]