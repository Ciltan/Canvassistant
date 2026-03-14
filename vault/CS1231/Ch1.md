---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 1: Propositional Logic

## Overview
This chapter introduces the foundational concepts of [[Propositional Logic]], focusing on the definition of propositions, their truth values, and the methods for constructing new propositions. Key logical operations such as negation, conjunction, disjunction, and conditional propositions are explored, along with their truth tables and implications. The chapter also covers predicates and quantifiers, providing a comprehensive understanding of logical expressions and their applications.

## Key Concepts & Definitions
- **Proposition**: A declarative sentence that is either true (T) or false (F).
- **Truth Value**: The quality of being true or false.
- **Negation**: The negation of a proposition \( p \) is denoted as \( \neg p \).
- **Conjunction**: The conjunction of two propositions \( p \) and \( q \) is denoted as \( p \land q \).
- **Disjunction**: The disjunction of two propositions \( p \) and \( q \) is denoted as \( p \lor q \).
- **Conditional Proposition**: Denoted as \( p \rightarrow q \), it is false only when \( p \) is true and \( q \) is false.
- **Biconditional Proposition**: Denoted as \( p \leftrightarrow q \), it is true when both propositions have the same truth value.
- **Predicate**: A sentence containing variables that becomes a proposition when the variables are specified.
- **Universal Quantifier**: Denoted as \( \forall x \), it asserts that a property holds for all elements in a domain.
- **Existential Quantifier**: Denoted as \( \exists x \), it asserts that there is at least one element in a domain for which a property holds.

## Detailed Technical Breakdown

### Propositions
- **True Propositions**: Example: \( 1 + 1 = 2 \)
- **False Propositions**: Example: \( 4 + 5 = 6 \)
- **Non-Propositions**: Questions, commands, or ambiguous statements.

### Logical Operations
#### Negation
- **Definition**: \( \neg p \) is true when \( p \) is false.
  
| \( p \) | \( \neg p \) |
|---------|--------------|
| T       | F            |
| F       | T            |

#### Conjunction
- **Definition**: \( p \land q \) is true only when both \( p \) and \( q \) are true.

| \( p \) | \( q \) | \( p \land q \) |
|---------|---------|------------------|
| T       | T       | T                |
| T       | F       | F                |
| F       | T       | F                |
| F       | F       | F                |

#### Disjunction
- **Definition**: \( p \lor q \) is false only when both \( p \) and \( q \) are false.

| \( p \) | \( q \) | \( p \lor q \) |
|---------|---------|-----------------|
| T       | T       | T               |
| T       | F       | T               |
| F       | T       | T               |
| F       | F       | F               |

#### Conditional Proposition
- **Definition**: \( p \rightarrow q \) is false only when \( p \) is true and \( q \) is false.

| \( p \) | \( q \) | \( p \rightarrow q \) |
|---------|---------|------------------------|
| T       | T       | T                      |
| T       | F       | F                      |
| F       | T       | T                      |
| F       | F       | T                      |

#### Biconditional Proposition
- **Definition**: \( p \leftrightarrow q \) is true when both \( p \) and \( q \) have the same truth values.

| \( p \) | \( q \) | \( p \leftrightarrow q \) |
|---------|---------|-----------------------------|
| T       | T       | T                           |
| T       | F       | F                           |
| F       | T       | F                           |
| F       | F       | T                           |

### Logical Operator Precedence
- **Order**: Negation \( \neg \), Conjunction \( \land \), Disjunction \( \lor \), Conditional \( \rightarrow \), Biconditional \( \leftrightarrow \).
- **Parentheses**: Use parentheses to clarify expressions.

## Implementation/Examples
```plaintext
Let p be "it is hot" and q be "it is sunny."
- Negation: ¬p = "It is not hot."
- Conjunction: p ∧ q = "It is hot and sunny."
- Disjunction: p ∨ q = "It is hot or sunny."
- Conditional: p → q = "If it is hot, then it is sunny."
- Biconditional: p ↔ q = "It is hot if and only if it is sunny."
```

> [!note] **Important**: Understanding the truth tables for each logical operation is crucial for mastering propositional logic.
> 
> [!warning] **Caution**: Be careful with the order of operations; incorrect precedence can lead to false conclusions.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter 2]]
- [[Tutorial+1+Solution]]
- [[CS1231_TUTORIAL+4]]