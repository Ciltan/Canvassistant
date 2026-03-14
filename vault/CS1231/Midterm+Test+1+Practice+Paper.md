---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Midterm 1 Practice Paper

## Overview
This note summarizes the key concepts and problems presented in the CS1231 Midterm 1 Practice Paper. It covers topics such as set operations, logical equivalences, and quantifiers in logic. The practice paper is designed to test understanding of fundamental concepts in propositional logic and set theory, essential for success in the course.

## Key Concepts & Definitions
- **Universal Set**: The set that contains all possible elements for a particular discussion, denoted as [[U]].
- **Subset**: A set that contains elements from another set, denoted as [[A]] and [[B]].
- **Bit String**: A sequence of bits (0s and 1s) used to represent sets.
- **Intersection (A∩B)**: The set containing all elements that are in both sets [[A]] and [[B]].
- **Set Difference (A−B)**: The set containing elements in [[A]] that are not in [[B]].
- **Power Set (P(S))**: The set of all subsets of a set [[S]].
- **Logical Equivalence**: Two statements that have the same truth value in all possible scenarios.
- **Quantifiers**: Symbols used in logic to express the quantity of specimens in a domain, such as ∀ (for all) and ∃ (there exists).

## Detailed Technical Breakdown

### Problem 1: Set Operations
1. **Given**: Universal set U = {1,2,3,4,5,6,7,8,9,10}
   - A = 1111001111
   - B = 0101111000
   - **(a)** Find A∩B.
   - **(b)** Find A−B.

### Problem 2: Power Set
- **Let S = {0,1}**: Find |P(S)|.

### Problem 3: Logical Equivalence
- **Determine if** (p → q) → r **and** p → (q → r **are logically equivalent** by completing the truth table.

| p | q | r | p → q | q → r | (p → q) → r | p → (q → r) |
|---|---|---|-------|-------|--------------|---------------|
| T | T | T |   T   |   T   |      T       |       T       |
| T | T | F |   T   |   F   |      F       |       F       |
| T | F | T |   F   |   T   |      T       |       T       |
| T | F | F |   F   |   F   |      T       |       F       |
| F | T | T |   T   |   T   |      T       |       T       |
| F | T | F |   T   |   F   |      F       |       F       |
| F | F | T |   T   |   T   |      T       |       T       |
| F | F | F |   T   |   F   |      F       |       F       |

- **Answer**: Yes / No

### Problem 4: Logical Equivalence Proof
- Prove the logical equivalence: ¬(p∨¬q)∨(¬p∧¬q) ≡ ¬p.

### Problem 5: Truth Values
1. **(i)** ∀n ∈ Z,∃m ∈ Z such that n² < m.
   - **Truth Value**: 
   - **Justification**: 

2. **(ii)** ∃n,m ∈ Z such that (n+m = 4)∧(n−m = 1).
   - **Truth Value**: 
   - **Justification**: 

### Problem 6: Logical Expressions with Quantifiers
- **Translate into logical expressions**:
  1. All students in CS1231 can do some questions in Tutorial 1.
  2. Some students in CS1231 can do all questions in Tutorial 1.
  3. There are two different students in CS1231 such that they can work together to do all questions in Tutorial 1.

### Problem 7: Deriving Conclusions
- Derive the conclusion ¬X from the following hypotheses:
  1. A∧B → C
  2. ¬A → D
  3. ¬B → E
  4. ¬C
  5. F → (¬D∧¬E)
  6. X → F

> [!important] Ensure to practice these concepts thoroughly as they are fundamental to understanding logic in computer science.
> [!note] Review the truth tables and logical equivalences regularly to reinforce your understanding.

## Related
- [[Logic - Propositional Logic]]
- [[Midterm+Briefing]]
- [[CS1231_TUTORIAL+4]]
- [[AY2122+Sem1+Homework+1(S)]]