---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 2 Notes

## Overview
This note summarizes key concepts and exercises from CS1231 Tutorial 2, focusing on logical statements and their implications. The tutorial covers various forms of logical expressions, including universal and existential quantifiers, and explores the relationships between hypotheses and conclusions. It also provides examples of logical negations and their interpretations in mathematical contexts.

## Key Concepts & Definitions
- **Logical Implication**: A statement of the form "If P, then Q" denoted as \( P \rightarrow Q \).
- **Universal Quantifier**: Denoted as \( \forall \), it asserts that a property holds for all elements in a given set.
- **Existential Quantifier**: Denoted as \( \exists \), it asserts that there is at least one element in a set for which a property holds.
- **Counterexample**: An example that disproves a statement or proposition.
- **Negation**: The logical operation that takes a statement and produces its opposite.

## Detailed Technical Breakdown

### 1. Logical Statements
- **(a)** If an animal is a rabbit, then it hops. (Alt: Every rabbit hops.)
- **(b)** Every animal is a rabbit and hops.
- **(c)** There is an animal such that if it is a rabbit, then it hops.
- **(d)** There is an animal that is a rabbit and hops. (Alt: Some rabbits hop.)

### 2. Hypotheses and Conclusions
- **Example**: Hypothesis true, conclusion false.
- **Set of pairs**: \{(1,1),(1,2),(1,−2),(2,1),(2,2),(2,−2),(−2,−2)\}

### 3. Universal Statements
- **(a)** \( \forall n \in \mathbb{Z}, \text{ if } n^2 \text{ is even then } n \text{ is even.} \)
- **(b)** \( \forall n \in \mathbb{Z}, \text{ if } n \text{ is even then } n^2 \text{ is even.} \)

### 4. Truth Values
- **Truth Values**: T, T, F (counterexample \( x = -3 \)), T

### 5. Logical Expressions
- **(a)** \( \forall x(D(x) \rightarrow \neg W(x)) \)
- **(b)** \( \forall x(O(x) \rightarrow W(x)) \)
- **(c)** \( \forall x(P(x) \rightarrow D(x)) \)
- **(d)** \( \forall x(P(x) \rightarrow \neg O(x)) \)
- **(e)** Yes, since \( P(x) \rightarrow D(x) \rightarrow \neg W(x) \rightarrow \neg O(x) \).

> [!important] Note: Many students provided \( \forall x(D(x) \land \neg W(x)) \) for (a), which is true only if the domain consists solely of ducks that do not waltz.

### 6. Existential Statements
- **(a)** \( \exists d \in \mathbb{Z} \text{ such that } 6 \in \mathbb{Z} \text{ and } d \neq 3. \)
- **(b)** There is an even integer whose square is odd.

### 7. Logical Negations
- **(a)** Some animal is able to fly but not a bird.
- **(b)** There is a function which is a polynomial but has no real roots.

### 8. Negation of Statements
- **Example**: \( \forall x \in D, \exists y \in E \text{ such that } x+y \neq -y. \)

### 9. Logical Equivalence
- **(a)** \( \exists r \in \mathbb{Q} \text{ such that } \forall a \in \mathbb{Z}, \forall b \in \mathbb{Z}, r \neq a/b. \)
- **(b)** \( \forall x \in \mathbb{R}, \exists y \in \mathbb{R} \text{ such that } x + y \neq 0. \)

### 10. Solutions to Logical Problems
- **Example**: \( S = (p \land \neg q) \lor (\neg p \land q) \)

## Implementation/Examples
```plaintext
1. Logical Implication: If P, then Q
2. Universal Quantifier: For all x, P(x)
3. Existential Quantifier: There exists an x such that P(x)
```

> [!note] The tutorial emphasizes the importance of understanding the structure of logical statements and their implications in mathematical reasoning.

## Related
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[Midterm+Briefing]]