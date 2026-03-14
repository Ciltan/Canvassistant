---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 1: Propositional Logic

## Overview
This chapter introduces the foundational concepts of [[Propositional Logic]], focusing on the nature of propositions, their truth values, and the logical operations that can be performed on them. It covers essential definitions, including negation, conjunction, disjunction, and conditional propositions, along with their truth tables. The chapter also explores the concepts of tautology, contradiction, predicates, and quantifiers, providing a comprehensive understanding of logical reasoning.

## Key Concepts & Definitions
- **Proposition**: A declarative sentence that is either true (T) or false (F). The truth value of a proposition is its quality of being true or false.
- **Negation**: The negation of a proposition \( p \) is denoted as \( \neg p \) and indicates "not \( p \)".
- **Conjunction**: The conjunction of two propositions \( p \) and \( q \) is denoted as \( p \land q \) and is true only when both \( p \) and \( q \) are true.
- **Disjunction**: The disjunction of two propositions \( p \) and \( q \) is denoted as \( p \lor q \) and is false only when both \( p \) and \( q \) are false.
- **Conditional Proposition**: A conditional proposition \( p \rightarrow q \) is false only when \( p \) is true and \( q \) is false.
- **Biconditional Proposition**: A biconditional proposition \( p \leftrightarrow q \) is true when both \( p \) and \( q \) have the same truth values.
- **Tautology**: A compound proposition that is always true.
- **Contradiction**: A compound proposition that is always false.
- **Predicate**: A sentence containing variables that becomes a proposition when the variables are specified.
- **Quantifiers**: Symbols used to express the quantity of elements in a domain that satisfy a predicate, including universal quantifier \( \forall \) and existential quantifier \( \exists \).

## Detailed Technical Breakdown

### Propositions
- **True Propositions**: Example: \( 1 + 1 = 2 \)
- **False Propositions**: Example: \( 4 + 5 = 6 \)
- **Non-Propositions**: Examples include questions and commands, such as "How is the lecture?" or "Stop talking!"

### Logical Operations
- **Negation**: 
  - \( p \) | \( \neg p \)
  - T | F
  - F | T

- **Conjunction**:
  - \( p \land q \) truth table:
  
  | \( p \) | \( q \) | \( p \land q \) |
  |---------|---------|-----------------|
  | T       | T       | T               |
  | T       | F       | F               |
  | F       | T       | F               |
  | F       | F       | F               |

- **Disjunction**:
  - \( p \lor q \) truth table:
  
  | \( p \) | \( q \) | \( p \lor q \) |
  |---------|---------|-----------------|
  | T       | T       | T               |
  | T       | F       | T               |
  | F       | T       | T               |
  | F       | F       | F               |

### Conditional Propositions
- **Truth Table** for \( p \rightarrow q \):
  
  | \( p \) | \( q \) | \( p \rightarrow q \) |
  |---------|---------|------------------------|
  | T       | T       | T                      |
  | T       | F       | F                      |
  | F       | T       | T                      |
  | F       | F       | T                      |

### Tautology and Contradiction
- **Tautology**: Example: \( p \lor \neg p \)
- **Contradiction**: Example: \( p \land \neg p \)

### Predicates & Quantifiers
- **Universal Quantifier**: \( \forall x \in D, P(x) \) is true if \( P(x) \) holds for all \( x \) in domain \( D \).
- **Existential Quantifier**: \( \exists x \in D, P(x) \) is true if there is at least one \( x \) in domain \( D \) such that \( P(x) \) holds.

## Implementation/Examples
```plaintext
Let P(x) be the predicate "x is a student at NUS" with domain the residents of Clementi.
When you replace x by John Tan who is a resident of Clementi, it becomes a proposition.
```

> [!note] **Important**: Understanding the difference between tautologies, contradictions, and contingencies is crucial for logical reasoning in mathematics and computer science.
> 
> [!warning] **Caution**: Be careful with the use of quantifiers; misinterpretation can lead to incorrect logical expressions.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]