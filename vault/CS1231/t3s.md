---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 3

## Overview
This tutorial focuses on logical reasoning and argument validation through propositional logic. It explores various argument forms, including valid and invalid deductions, and provides examples of logical proofs. The tutorial emphasizes the importance of understanding logical structures and their implications in mathematical reasoning.

## Key Concepts & Definitions
- **Propositional Logic**: A branch of logic that deals with propositions and their relationships.
- **Modus Tollens**: A form of argument where if a conditional statement is accepted, and the consequent does not hold, then the antecedent must also not hold.
- **Modus Ponens**: A form of argument that states if a conditional statement is accepted, and the antecedent holds, then the consequent must also hold.
- **Conjunction**: A logical operation that combines two propositions and is true only if both propositions are true.
- **Disjunction**: A logical operation that combines two propositions and is true if at least one of the propositions is true.
- **Counter-example**: An example that disproves a statement or proposition.

## Detailed Technical Breakdown

### Truth Tables
- **Argument Validity**:
  - For premises \( P_1 \) and \( P_2 \) leading to conclusion \( C \):
    - Valid if whenever \( P_1 \) and \( P_2 \) are true, \( C \) is also true.
    - Invalid if there exists a case where \( P_1 \) and \( P_2 \) are true, but \( C \) is false.

| p | q | r | P | P | C | Q | Q | C |
|---|---|---|---|---|---|---|---|---|
| T | T | T | T | T | T | F | F |   |
| T | T | F | F | F | T | T | T |   |
| T | F | T | T | T | T | T | F |   |
| T | F | F | F | T | F | F | T |   |
| F | T | T | T | T | T | F | T |   |
| F | T | F | T | F | F | T | T |   |
| F | F | T | T | T | T | T | T |   |
| F | F | F | T | T | T | T | T |   |

### Logical Deductions
1. **Example of Modus Tollens**:
   - Premises:
     1. \( p \rightarrow t \)
     2. \( \neg t \)
   - Conclusion: \( \neg p \)

2. **Generalization**:
   - From \( \neg p \), conclude \( \neg p \lor q \).

3. **Invalid Argument Example**:
   - Premises:
     - \( p \lor q \rightarrow r \)
     - \( \neg p \land \neg q \)
   - Conclusion: \( \neg r \) (invalid due to inverse error).

### Proof Techniques
- **Direct Proof**:
  - For any two odd integers \( n \) and \( m \):
    - \( n = 2k + 1 \), \( m = 2p + 1 \)
    - Product \( nm = 2q + 1 \) is odd.

- **Proof by Contraposition**:
  - If \( a, b \) are both odd, then \( a^2 + b^2 \neq c^2 \).

> [!important] Understanding the validity of logical arguments is crucial in mathematical reasoning and proofs. Always check for counter-examples to validate your deductions.

> [!note] Remember that a valid argument does not necessarily mean the premises are true; it only means that if the premises are true, the conclusion must also be true.

## Implementation/Examples
```plaintext
1. Let p = "Sandra knows Java".
2. Let q = "Sandra knows C++".
3. Premise: p ∧ q
4. Conclusion: ∴ q (valid by specialization)
```

## Related
- [[Logic - Propositional Logic]]
- [[AY2122+Sem1+Homework+3]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]