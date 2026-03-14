---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 8: Relations

## Overview
This chapter delves into the concept of relations in set theory, defining relations as subsets of Cartesian products. It explores various types of relations, including equivalence relations and partial orderings, and provides examples to illustrate these concepts. The chapter emphasizes the significance of relations in mathematical structures and their applications in computer science.

## Key Concepts & Definitions
- **Relation**: A relation \( R \) from set \( A \) to set \( B \) is defined as a subset of \( A \times B \). We denote \( xRy \) if \( (x,y) \in R \) and \( xR/y \) if \( (x,y) \notin R \).
- **Domain**: The domain of a relation \( R \) is the set of all \( a \in A \) such that there exists \( b \in B \) with \( aRb \).
- **Range**: The range of a relation \( R \) is the set of all \( b \in B \) such that there exists \( a \in A \) with \( aRb \).
- **Inverse Relation**: The inverse of a relation \( R \), denoted \( R^{-1} \), is defined as \( R^{-1} = \{(b,a) \in B \times A | aRb\} \).
- **Equivalence Relation**: A relation \( R \) on a set \( A \) is an equivalence relation if it is reflexive, symmetric, and transitive.
- **Partial Order**: A relation \( R \) on a set \( A \) is a partial order if it is reflexive, antisymmetric, and transitive.

## Detailed Technical Breakdown

### 8.1 Definition of Relations
- **Example 1**: Let \( A = \{0,1,2\} \) and \( B = \{1,2,3\} \). Define \( xRy \) if \( x < y \). Then:
  - \( R = \{(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)\} \)
- **Example 2**: Let \( E \) be the relation on \( \mathbb{Z} \times \mathbb{Z} \) defined by \( E = \{(x,y) : x \equiv y \mod 2\} \).

### 8.2 Representing Relations
- **Arrow Diagram**: A visual representation where an arrow from \( a \) to \( b \) indicates \( (a,b) \in R \).
  
| A | B |
|---|---|
| 1 | x |
| 1 | y |
| 2 | x |
| 2 | y |
| 2 | z |
| 3 | z |
| 4 | z |

### 8.3 Equivalence Relations
- **Properties**:
  - **Reflexive**: \( \forall x \in A, (x,x) \in R \)
  - **Symmetric**: \( \forall x,y \in A, (x,y) \in R \Rightarrow (y,x) \in R \)
  - **Transitive**: \( \forall x,y,z \in A, (x,y) \in R, (y,z) \in R \Rightarrow (x,z) \in R \)

### 8.4 Partial Orderings
- **Definition**: A relation \( R \) on a set \( A \) is a partial order if it is reflexive, antisymmetric, and transitive.
- **Examples**:
  - \( (A, \leq) \) where \( A \subseteq \mathbb{R} \)
  - \( (S, |) \) where \( S \subseteq \mathbb{N} \)

## Implementation/Examples
```markdown
# Example of an Arrow Diagram
R = {(1,x),(1,y),(2,x),(2,y),(2,z),(3,z),(4,z)}
```

> [!note] **Reflexivity in Relations**: A relation is reflexive if every element is related to itself, which is crucial for defining equivalence relations.

> [!important] **Transitivity**: A relation is transitive if the relation holds across a chain of elements, which is essential for both equivalence relations and partial orders.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]