---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 5: Functions and Their Properties

## Overview
This tutorial focuses on the analysis of functions, including their properties such as being one-to-one (1-1), onto, and bijective. It also covers the determination of domains and ranges, as well as the application of characteristic functions. The exercises provided aim to deepen understanding of these concepts through practical examples and proofs.

## Key Concepts & Definitions
- **Function**: A relation that assigns exactly one output for each input from a given set.
- **Domain**: The set of all possible input values for a function.
- **Range**: The set of all possible output values of a function.
- **Bijection**: A function that is both one-to-one and onto.
- **Characteristic Function**: A function that indicates membership of an element in a subset.

## Detailed Technical Breakdown

### 1. Determining Functions
- **Task**: Determine whether \( f : \mathbb{Z} \to \mathbb{R} \) is a function.
  - (a) \( f(n) = \pm n \) 
  - (b) \( f(n) = n^2 + 1 \) 
  - (c) \( f(n) = \frac{1}{n^2 - 4} \) 
  - (d) \( f(n) = \sin n \)

### 2. Domain and Range
- **Functions**:
  - (a) Last digit of a nonnegative integer.
  - (b) Next largest integer to a positive integer.
  - (c) Number of one bits in a bit string.
  - (d) Number of bits in a bit string.

### 3. Floor and Ceiling Functions
- **Values**:
  - (a) \( \lfloor 1.1 \rfloor \)
  - (b) \( \lceil 1.1 \rceil \)
  - (c) \( \lfloor -0.1 \rfloor \)
  - (d) \( \lceil -0.1 \rceil \)
  - (e) \( \lfloor 1 + \lceil 3 \rceil \rfloor \)
  - (f) \( \lceil 1 + \lfloor 3 \rfloor \rceil \)

### 4. Onto Functions
- **Task**: Determine if \( f : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z} \) is onto.
  - (a) \( f(m,n) = 2m - n \)
  - (b) \( f(m,n) = m^2 - n^2 \)

### 5. Bijections and Inverses
- **Task**: Identify bijections and find inverse functions.
  - (a) \( f : \mathbb{R} \to \mathbb{R} \) where \( f(x) = -3x^2 + 7 \)
  - (b) \( f : \mathbb{R} - \{-2\} \to \mathbb{R} - \{1\} \) where \( f(x) = \frac{x+1}{x+2} \)

### 6. Characteristic Functions
- **Definition**: For a set \( A \subseteq S \), the characteristic function \( k : S \to \mathbb{Z} \) is defined as:
  - \( k(x) = \begin{cases} 
    1 & \text{if } x \in A \\ 
    0 & \text{if } x \notin A 
    \end{cases} \)
- **Properties**:
  - (a) \( k_A(x) = k_A(x) \cdot k_B(x) \)
  - (b) \( k_A(x) = (1 - k_A(x))(1 - k_B(x)) \)
  - (c) \( k_A(x) = (1 - k_A(x))k_B(x) \)
  - (d) Deduce \( |A \cup B| = |A| + |B| - |A \cap B| \)

### 7. Composition of Functions
- **Question**: If \( f \circ g \) is 1-1, does it follow that \( g \) is 1-1?

### 8. Function Inverses
- **True or False**:
  - (a) \( f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D) \)
  - (b) \( f^{-1}(C - D) = f^{-1}(C) - f^{-1}(D) \)

### 9. Function on Bit Strings
- **Task**: Define \( f : S \to \mathbb{Z} \) where \( f(s) = \) number of 0's minus number of 1's in \( s \). Is \( f \) 1-1 or onto?

### 10. Proving Properties of Functions
- **Definitions**:
  - \( F(n,m) = 3n^5m \)
  - \( G(n,m) = 3n^6m \)
- **Prove or Disprove**:
  - (a) \( F \) is 1-1.
  - (b) \( G \) is 1-1.

### 11. Counting Multiples
- **Task**: How many integers in \([100, 1000]\) are multiples of 6?

### 12. Floor Function Proof
- **Prove**: \( \lfloor 3x \rfloor = \lfloor x \rfloor + \lfloor x + 1 \rfloor + \lfloor x + 2 \rfloor \)

> [!note] **Important**: Understanding the properties of functions is crucial for further studies in discrete mathematics and computer science.
> 
> [!warning] **Caution**: Be careful with the definitions of onto and one-to-one functions, as they are foundational for understanding more complex concepts in set theory and function analysis.

## Related
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[Midterm+Briefing]]
- [[Chapter+2]]