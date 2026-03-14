---
tags: [CS1231, lecture-notes, academic]
---

# CS1231: Discrete Structures - Tutorial 3

## Overview
This tutorial focuses on the evaluation of argument forms using [[truth tables]] to determine their validity. It emphasizes the importance of identifying premises and conclusions, constructing truth tables, and applying logical rules to assess argument validity. Key concepts such as [[Modus Ponens]], [[Modus Tollens]], and [[Generalization]] are explored through practical examples.

## Key Concepts & Definitions
- **Valid Argument Form**: An argument is valid if the conclusion logically follows from the premises.
- **Truth Table**: A mathematical table used to determine the truth values of logical expressions based on their components.
- **Modus Ponens**: If \( p \rightarrow q \) and \( p \) is true, then \( q \) must also be true.
- **Modus Tollens**: If \( p \rightarrow q \) and \( \neg q \) is true, then \( \neg p \) must also be true.
- **Generalization**: If \( p \) is true, then \( p \lor q \) is also true for any \( q \).
- **Specialization**: If \( p \land q \) is true, then both \( p \) and \( q \) must be true.

## Detailed Technical Breakdown

### Testing for Valid Argument Forms
1. **Identify the Premises and Conclusion**: Clearly define what the premises and conclusion of the argument are.
2. **Construct a Truth Table**: Create a truth table that includes all possible truth values for the premises.
3. **Evaluate Validity**: 
   - If there exists a row where all premises are true and the conclusion is false, the argument is invalid.
   - If no such row exists, the argument is valid.

### Example Truth Table
| p   | q   | r   | \( p \rightarrow r \) | \( q \rightarrow r \) | \( p \lor q \) | \( p \lor q \rightarrow r \) |
|-----|-----|-----|-----------------------|-----------------------|----------------|-------------------------------|
| T   | T   | T   | T                     | T                     | T              | T                             |
| T   | T   | F   | F                     | T                     | T              | F                             |
| T   | F   | T   | T                     | T                     | T              | T                             |
| T   | F   | F   | F                     | T                     | T              | F                             |
| F   | T   | T   | T                     | T                     | T              | T                             |
| F   | T   | F   | T                     | F                     | T              | F                             |
| F   | F   | T   | T                     | T                     | F              | T                             |
| F   | F   | F   | T                     | T                     | F              | T                             |

> [!note] **Important**: Always ensure that the premises are clearly stated before constructing the truth table.

### Validity of Argument Forms
- **Example (a)**: \( p \rightarrow r, q \rightarrow r \) implies \( p \lor q \rightarrow r \) is valid.
- **Example (b)**: \( p \rightarrow q \lor r, \neg q \lor \neg r \) implies \( \neg p \lor \neg r \) is invalid.

## Implementation/Examples
```plaintext
1. Given premises: \( p \rightarrow r, q \rightarrow r \)
   Conclusion: \( p \lor q \rightarrow r \)
   Truth Table confirms validity.

2. Given premises: \( p \rightarrow q \lor r, \neg q \lor \neg r \)
   Conclusion: \( \neg p \lor \neg r \)
   Truth Table confirms invalidity.
```

> [!warning] **Caution**: Misidentifying premises can lead to incorrect conclusions. Always double-check your premises.

## Related
- [[Logic - Propositional Logic]]
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[CS1231_TUTORIAL+4]]
- [[Midterm+Briefing]]