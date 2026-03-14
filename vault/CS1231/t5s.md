---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 5

## Overview
This tutorial focuses on various properties of functions, including injectivity, surjectivity, and the relationships between sets. It explores the implications of these properties through examples and mathematical proofs, emphasizing the importance of understanding mappings and their characteristics in the context of set theory and functions.

## Key Concepts & Definitions
- **Injective Function**: A function \( f \) is injective (or one-to-one) if \( f(a) = f(b) \) implies \( a = b \).
- **Surjective Function**: A function \( f \) is surjective (or onto) if for every element \( y \) in the codomain, there exists an element \( x \) in the domain such that \( f(x) = y \).
- **Preimage**: The preimage of a set \( C \) under a function \( f \) is the set of all elements in the domain that map to \( C \).
- **Set Intersection**: The intersection of two sets \( A \) and \( B \), denoted \( A \cap B \), is the set of elements that are in both \( A \) and \( B \).
- **Set Union**: The union of two sets \( A \) and \( B \), denoted \( A \cup B \), is the set of elements that are in either \( A \) or \( B \).

## Detailed Technical Breakdown

### Function Properties
1. **Injectivity and Surjectivity**
   - **Example 1**: 
     - (a) Not injective: \( f(1) = f(-1) \).
     - (b) Surjective: For \( y \in \mathbb{R} - \{1\} \), \( f(x) = y \) has a solution.
   - **Example 2**: 
     - (a) Onto: Any \( n \in \mathbb{Z} \) has a preimage.
     - (b) No preimage for certain values.

### Set Operations
- **Intersection and Union Properties**
  - If \( x \in A \cap B \), then \( k(x) \cdot k(x) = 1 \).
  - If \( x \notin A \cup B \), then \( k(x) = 0 \).

### Mathematical Proofs
- **Proof of Surjectivity**:
  - Let \( g(a) = g(b) \). Then \( f(g(a)) = f(g(b)) \) implies \( a = b \).
- **Proof of Set Relationships**:
  - \( x \in f^{-1}(C \cap D) \) if and only if \( x \in f^{-1}(C) \cap f^{-1}(D) \).

## Implementation/Examples
```math
1. f(x) = \frac{(2x-1)}{(1-x)} \text{ is not equal to } -2.
2. \sum_{x \in S} k(x) = |S| - |A| - |B| + |A \cap B|.
```

> [!note] **Important Definitions**: Understanding the definitions of injective and surjective functions is crucial for analyzing function properties in set theory.
> 
> [!warning] **Common Pitfalls**: Be cautious of confusing injectivity with surjectivity; they are distinct properties that can affect the behavior of functions differently.

## Related
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[Midterm+Briefing]]