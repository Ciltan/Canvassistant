---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Midterm 1 Practice Paper

## Overview
This note summarizes the practice paper for the CS1231 Midterm 1, focusing on key concepts in logic, set theory, and quantifiers. It includes exercises on set operations, logical equivalences, and truth values, providing a comprehensive review of the material covered in the course. The solutions are structured to enhance understanding and facilitate further study.

## Key Concepts & Definitions
- **Universal Set**: The set that contains all possible elements for a particular discussion, denoted as [[U]].
- **Set Operations**: Includes operations such as intersection (∩), difference (−), and power set (P).
- **Logical Equivalence**: Two statements are logically equivalent if they have the same truth value in all possible scenarios.
- **Quantifiers**: Symbols used in logic to express the quantity of specimens in a domain, specifically universal (∀) and existential (∃).
- **Truth Table**: A mathematical table used to determine the truth values of logical expressions.

## Detailed Technical Breakdown

### 1. Set Operations
- **Given Sets**:
  - Universal Set: \( U = \{1,2,3,4,5,6,7,8,9,10\} \)
  - Set A: Represented by the bit string `1111001111`
  - Set B: Represented by the bit string `0101111000`
  
- **Tasks**:
  - (a) **Intersection \( A ∩ B \)**:
    - Bit string representation: `0101001000`
    - Elements: \( \{1, 3, 8, 9, 10\} \)
  
  - (b) **Set Difference \( A - B \)**:
    - Elements: \( \{4\} \)

### 2. Power Set Calculation
- **Set \( S = \{0,1\} \)**:
  - Find \( |P(S)| \): 
    - Answer: \( 2^n = 2^2 = 4 \)

### 3. Logical Equivalence
- **Truth Table for \( (p → q) → r \) and \( p → (q → r) \)**:
  
| p | q | r | p → q | q → r | (p → q) → r | p → (q → r) |
|---|---|---|-------|-------|--------------|---------------|
| T | T | T |   T   |   T   |      T       |       T       |
| T | T | F |   T   |   F   |      F       |       F       |
| T | F | T |   F   |   T   |      T       |       T       |
| T | F | F |   F   |   T   |      T       |       T       |
| F | T | T |   T   |   T   |      T       |       T       |
| F | T | F |   T   |   F   |      F       |       T       |
| F | F | T |   T   |   T   |      T       |       T       |
| F | F | F |   T   |   T   |      T       |       T       |

- **Conclusion**: Not logically equivalent.

### 4. Proof of Logical Equivalence
- **Statement**: \( ¬(p∨¬q)∨(¬p∧¬q) ≡ ¬p \)
- **Proof Steps**:
  1. \( ¬(p∨¬q)∨(¬p∧¬q) \)
  2. \( ≡ (¬p∧¬¬q)∨(¬p∧¬q) \)
  3. \( ≡ (¬p∧q)∨(¬p∧¬q) \)
  4. \( ≡ ¬p∧(q ∨¬q) \)
  5. \( ≡ ¬p∧C \)
  6. \( ≡ ¬p \)

### 5. Truth Values of Statements
- **Statement (i)**: \( ∀n ∈ Z,∃m ∈ Z \) such that \( n^2 < m \)
  - Truth Value: **True**
  - Justification: For any \( n \in Z \), let \( m = n^2 + 1 \).

- **Statement (ii)**: \( ∃n,m ∈ Z \) such that \( (n+m = 4)∧(n−m = 1) \)
  - Truth Value: **False**
  - Justification: Implies non-integer solutions.

### 6. Logical Expressions with Quantifiers
- **Expressions**:
  - (i) All students in CS1231 can do some questions in Tutorial 1:
    - \( ∀x ∈ C∃y ∈ Y,P(x,y) \)
  
  - (ii) Some students in CS1231 can do all questions in Tutorial 1:
    - \( ∃x ∈ C∀y ∈ Y,P(x,y) \)
  
  - (iii) There are two different students in CS1231 such that they can do all questions in Tutorial 1:
    - \( ∃x,z ∈ C∀y ∈ Y,Q(x,z)∧(P(x,y)∨P(z,y)) \)

### 7. Derivation of Conclusion
- **Hypotheses**:
  1. \( A∧B → C \)
  2. \( ¬A → D \)
  3. \( ¬B → E \)
  4. \( ¬C \)
  5. \( F → (¬D∧¬E) \)
  6. \( X → F \)

- **Derivation Steps**:
  1. From \( A∧B → C \) and \( ¬C \), conclude \( ¬(A∧B) \).
  2. Apply De Morgan’s Law to get \( ¬A∨¬B \).
  3. Continue through the hypotheses to derive \( ¬X \).

> [!note] This practice paper serves as an excellent review tool for understanding logical operations and set theory.
> [!important] Ensure to familiarize yourself with truth tables and logical equivalences as they are crucial for success in CS1231.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Test+1+Practice+Paper]]