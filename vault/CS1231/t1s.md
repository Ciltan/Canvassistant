---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 1

## Overview
This tutorial focuses on the evaluation of logical propositions and their relationships through truth tables and logical equivalences. It emphasizes the importance of understanding the structure of propositions, implications, and the application of logical laws such as De Morgan's laws. The tutorial also explores the nuances of necessary and sufficient conditions in logical statements.

## Key Concepts & Definitions
- **Propositions**: Statements that can be either true or false. In this tutorial, only propositions c and f are identified as such.
- **Truth Tables**: A mathematical table used to determine the truth values of logical expressions based on their components.
- **Implication**: A logical operation where the truth of one statement (p) leads to the truth of another (q), denoted as p → q.
- **De Morgan's Laws**: Rules that relate conjunctions and disjunctions through negation.
- **Necessary and Sufficient Conditions**: Conditions that must be met for a statement to be true (necessary) and those that guarantee the truth of a statement (sufficient).

## Detailed Technical Breakdown

### Propositions and Truth Values
1. Only c and f are propositions and both are false. The rest do not have a truth value.
2. Evaluating statements:
   - (a) The election is not decided but the votes have been counted.
   - (b) If the votes have been counted, then the election is decided.
   - (c) The election is decided iff the votes have been counted.
   - (d) Either the votes have not been counted, or else the election is not decided and the votes have been counted.

### Truth Table Analysis
| p | q | r | p ∨ q | p ∧ r | s | t |
|---|---|---|-------|-------|---|---|
| T | T | T |   T   |   T   | T | T |
| T | T | F |   T   |   F   | T | F |
| T | F | T |   T   |   T   | T | T |
| T | F | F |   T   |   F   | T | F |
| F | T | T |   T   |   F   | T | T |
| F | T | F |   T   |   F   | T | F |
| F | 0 | T |   F   |   F   | F | F |
| F | F | F |   F   |   F   | F | F |

### Logical Equivalences
- **Example**: 
  - (p ∨ q) ∨ (p ∧ r) = p ∨ q
  - (r ∨ p) ∧ (¬r ∨ (p ∧ q)) = p ∧ q

### Necessary and Sufficient Conditions
1. **Statement**: W → (C ∧ P)
   - **Converse**: (C ∧ P) → W
   - **Inverse**: ¬W → ¬(C ∧ P) or ¬W → (¬C ∨ ¬P)
   - **Contrapositive**: ¬(C ∧ P) → ¬W or (¬C ∨ ¬P) → ¬W
   - **Negation**: W ∧ ¬(C ∧ P)

> [!important] Understanding the difference between necessary and sufficient conditions is crucial for logical reasoning and problem-solving in CS1231.

## Implementation/Examples
```plaintext
1. Evaluate the truth values of the following propositions:
   - p: "The sky is blue."
   - q: "It is raining."
   - r: "I will take an umbrella."

   Truth Table:
   | p | q | r | p → q | ¬p → r |
   |---|---|---|-------|--------|
   | T | T | T |   T   |   T    |
   | T | T | F |   T   |   F    |
   | T | F | T |   F   |   T    |
   | F | T | T |   T   |   T    |
   | F | F | F |   T   |   T    |
```

> [!note] The truth table is a powerful tool for visualizing the relationships between propositions and their logical outcomes.

## Related
- [[Logic - Propositional Logic]]
- [[AY2122+Sem1+Homework+3]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]