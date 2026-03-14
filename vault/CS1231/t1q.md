---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 1: Propositional Logic

## Overview
This tutorial focuses on the fundamentals of [[Logic - Propositional Logic]], exploring the nature of propositions, logical equivalences, and truth tables. Students will engage with various exercises to determine the truth values of conditional statements and analyze logical relationships. The tutorial also emphasizes the importance of understanding logical constructs in mathematical reasoning.

## Key Concepts & Definitions
- **Proposition**: A declarative statement that is either true or false.
- **Logical Equivalence**: Two statements that have the same truth value in all possible scenarios.
- **Truth Table**: A table used to determine the truth value of a logical expression based on the truth values of its components.
- **Conditional Statement**: A statement of the form "If P, then Q" (P → Q).

## Detailed Technical Breakdown

### 1. Identifying Propositions
- **Propositions**: 
  - (c) There are no black flies in Maine.
  - (d) 4+x = 5.
  - (e) 2n ≥ 100.
  - (f) The moon is made of green cheese.
  
### 2. Expressing Propositions in English
- Let \( p \): "The election is decided"
- Let \( q \): "The votes have been counted"
  - (a) ¬p∧q: "The election is not decided and the votes have been counted."
  - (b) q → p: "If the votes have been counted, then the election is decided."
  - (c) p ↔ q: "The election is decided if and only if the votes have been counted."
  - (d) ¬q ∨(¬p∧q): "Either the votes have not been counted or the election is not decided and the votes have been counted."

### 3. Evaluating Conditional Propositions
- (a) False: If 1+1 = 3, then unicorns exist.
- (b) False: If 1+1 = 3, then dogs can fly.
- (c) True: If 1+1 = 2, then dogs can fly.
- (d) True: If 2+2 = 4, then 1+2 = 3.

### 4. Analyzing Complex Propositions
- Proposition: "You will get an A in this module only if either you do every exercise in the textbook or you score at least 80 marks in the final."
  - (a) True situations: Completing all exercises or scoring 80+ marks.
  - (b) False: Not doing exercise 5 and scoring 79 marks means you would not get an A.

### 5. Logical Equivalence
- (a) Not logically equivalent: (p∨q)∨(p∧r) vs (p∨q)∧r.
- (b) Not logically equivalent: (r∨p)∧(¬r∨(p∧q))∧(r∨q) vs p∧q.

### 6. Truth Table Completion
| p | q | r | p → q | ¬p → r | (p → q)∧(¬p → r) |
|---|---|---|-------|--------|------------------|
| T | T | T |   T   |   T    |        T         |
| T | T | F |   T   |   F    |        F         |
| T | F | T |   F   |   T    |        F         |
| F | T | T |   T   |   T    |        T         |
| T | F | F |   F   |   F    |        F         |
| F | T | F |   T   |   T    |        T         |
| F | F | T |   T   |   T    |        T         |
| F | F | F |   T   |   T    |        T         |

### 7. Analyzing Self-Referential Propositions
- (a) Conclusion: The nth proposition leads to a paradox.
- (b) At least n propositions being false leads to similar paradoxical conclusions.
- (c) With 101 items, the implications of part (b) become more complex.

### 8. Comments on Statements
- (a) The negation of “1 < a < 5” is “1 ≥ a or a ≥ 5”.
- (b) The statement means "if he behaves himself then he’s welcome to come along."

### 9. Simplifying Propositions
- (a) \( (p∨¬q) → q \) simplifies to \( ¬p ∨ q \) (by the implication law).
- (b) \( ¬(p∨¬q)∨(¬p∧¬q) \) simplifies to \( ¬p \) (by De Morgan's laws).
- (c) \( (p → q) → r \) simplifies to \( ¬p ∨ q → r \).

### 10. Conditional Statements in Context
- (a) Conditional statement: "If C and P, then W."
- (b) Converse: "If W, then C and P."  
  Inverse: "If not C, then not W."  
  Contrapositive: "If not W, then not C or not P."  
  Negation: "It is not the case that if C and P, then W."

### 11. Tautology Analysis
- Show that \( [(p → q)∧q] → p \) is not a tautology by providing a counterexample.

### 12. Chat Room Logic Puzzle
- Analyze the conditions to determine who is chatting based on the provided statements.

> [!note] **Important**: Understanding the structure of propositions and their logical relationships is crucial for mastering [[Logic - Propositional Logic]].
> 
> [!warning] **Caution**: Misinterpretation of logical statements can lead to incorrect conclusions in mathematical reasoning.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]