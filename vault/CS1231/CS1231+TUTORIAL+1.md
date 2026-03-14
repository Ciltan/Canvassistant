---
tags: [CS1231, lecture-notes, academic]
---

# CS1231: Discrete Structures - Tutorial 1

## Overview
This tutorial introduces fundamental concepts in discrete structures, focusing on the distinction between propositions and non-propositions, logical operations, and truth tables. Key topics include the translation of logical symbols, the concepts of tautology and contradiction, and the laws of logical equivalence. Understanding these concepts is essential for further studies in logic and mathematics.

## Key Concepts & Definitions
- **Proposition**: A statement that is either true or false. 
- **Non-proposition**: Includes questions, commands, or sentences with undefined terms.
- **Logical Operations**: 
  - Negation (¬)
  - Conjunction (∧)
  - Disjunction (∨)
  - Implication (→)
  - Biconditional (↔)
- **Truth Table**: A table used to determine the truth value of logical expressions.
- **Tautology**: A formula that is true in every possible interpretation.
- **Contradiction**: A formula that is false in every possible interpretation.
- **Logically Equivalent**: Two statements that have the same truth value in every model.

## Detailed Technical Breakdown

### Propositions vs. Non-Propositions
- **Examples of Propositions**:
  - "There are no black flies in Maine." (True/False)
  - "The moon is made of green cheese." (False)
- **Examples of Non-Propositions**:
  - "Do not go." (Command)
  - "Can you answer the question?" (Question)

### Logical Operations and Precedence
- **Order of Precedence**:
  1. Negation (¬)
  2. Conjunction (∧), Disjunction (∨)
  3. Implication (→), Biconditional (↔)

### Truth Tables
- **Example**: Truth table for implication (p → q)
  
| p   | q   | p → q |
|-----|-----|-------|
| T   | T   | T     |
| T   | F   | F     |
| F   | T   | T     |
| F   | F   | T     |

### Logical Equivalence Laws
- **Distributive Law**: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)
- **Idempotent Law**: p ∨ p ≡ p
- **Absorption Law**: p ∨ (p ∧ q) ≡ p

## Implementation/Examples
### Example of Logical Expressions
```plaintext
Let p = "The election is decided"
Let q = "The votes have been counted"

1. ¬p ∧ q: "The election is not decided and the votes have been counted."
2. q → p: "If the votes have been counted, then the election is decided."
3. p ↔ q: "The election is decided iff the votes have been counted."
```

> [!note] **Important**: Understanding the distinction between propositions and non-propositions is crucial for logical reasoning and mathematical proofs.

> [!warning] **Caution**: Misinterpreting logical symbols can lead to incorrect conclusions in logical arguments.

## Related
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[CS1231+TUTORIAL+3]]