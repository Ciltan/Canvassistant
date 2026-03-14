---
tags: [CS1231, lecture-notes, academic]
---

# Understanding Propositional Logic

## Overview
This note delves into the fundamental concepts of [[Logic - Propositional Logic]], focusing on implications and their various forms. It outlines the meanings of conditional statements, including implications, converses, inverses, and contrapositives. Understanding these concepts is crucial for mastering logical reasoning in computer science and mathematics.

## Key Concepts & Definitions
- **Implication**: The statement “If p then q” is represented as \( p \rightarrow q \).
- **Only If**: The phrase “p only if q” also translates to \( p \rightarrow q \) or equivalently \( \neg q \rightarrow \neg p \).
- **Contrapositive**: The contrapositive of \( p \rightarrow q \) is \( \neg q \rightarrow \neg p \). Notably, the contrapositive of \( \neg q \rightarrow \neg p \) is \( p \rightarrow q \).
- **Converse**: The converse of \( p \rightarrow q \) is \( q \rightarrow p \).
- **Inverse**: The inverse of \( p \rightarrow q \) is \( \neg p \rightarrow \neg q \).

> [!important] Understanding these logical forms is essential for constructing valid arguments and proofs in computer science.

## Detailed Technical Breakdown
### Implications
- **Definition**: An implication \( p \rightarrow q \) asserts that if \( p \) is true, then \( q \) must also be true.
- **Truth Table**:
  | p     | q     | \( p \rightarrow q \) |
  |-------|-------|-----------------------|
  | T     | T     | T                     |
  | T     | F     | F                     |
  | F     | T     | T                     |
  | F     | F     | T                     |

### Forms of Implications
- **Contrapositive**: 
  - If \( p \rightarrow q \) is true, then \( \neg q \rightarrow \neg p \) is also true.
- **Converse**: 
  - The truth of \( p \rightarrow q \) does not guarantee the truth of \( q \rightarrow p \).
- **Inverse**: 
  - Similarly, \( \neg p \rightarrow \neg q \) does not follow from \( p \rightarrow q \).

> [!note] Remember that while the contrapositive is logically equivalent to the original implication, the converse and inverse are not.

## Implementation/Examples
```plaintext
Example 1:
Let p = "It is raining."
Let q = "The ground is wet."
Then:
- p → q: If it is raining, then the ground is wet.
- ¬q → ¬p: If the ground is not wet, then it is not raining.

Example 2:
Let p = "You will pass the exam."
Let q = "You studied."
Then:
- p → q: If you pass the exam, then you studied.
- q → p: If you studied, then you will pass the exam (not necessarily true).
```

## Related
- For further exploration, see [[AY2122+Sem1+Homework+3]], [[AY2122+Sem2+Homework+3]], and [[CS1231_TUTORIAL+4]] for practical applications of these concepts.