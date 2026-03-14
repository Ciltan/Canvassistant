---
tags: [CS1231, lecture-notes, academic]
---

# CS1231: Discrete Structures - Tutorial 2

## Overview
This tutorial focuses on the concepts of quantifiers in logic, specifically their translations and negations. It covers nested quantifiers and provides examples to illustrate the application of these concepts in logical statements. The tutorial aims to enhance understanding of how to express logical propositions using quantifiers effectively.

## Key Concepts & Definitions
- **Quantifiers**: Symbols used in logic to express the quantity of specimens in a domain that satisfy a given property. The two primary quantifiers are:
  - **Universal Quantifier**: Denoted as `@`, meaning "for all".
  - **Existential Quantifier**: Denoted as `D`, meaning "there exists".
- **Negation of Quantifications**: The process of expressing the opposite of a quantified statement.
- **Nested Quantifiers**: Quantifiers that are placed within the scope of other quantifiers.

## Detailed Technical Breakdown

### 1. Translation of Quantified Statements
Given the predicates:
- \( R(x) \): "x is a rabbit"
- \( H(x) \): "x hops"

Translate the following statements into English:
- (a) \( @x (R(x) \Rightarrow H(x)) \): For every animal, if it is a rabbit, then it hops.
- (b) \( @x (R(x) \land H(x)) \): Every animal is a rabbit and hops.
- (c) \( D x (R(x) \Rightarrow H(x)) \): There is an animal such that if it is a rabbit, then it hops.
- (d) \( D x (R(x) \land H(x)) \): There is an animal that is a rabbit and hops.

### 2. Truth Table for Implication
| p     | q     | p → q |
|-------|-------|-------|
| T     | T     | T     |
| T     | F     | F     |
| F     | T     | T     |
| F     | F     | T     |

### 3. Example of Predicate Logic
Let \( Q(x,y) \) be the predicate "If \( x < y \) then \( x^2 < y^2 \)" with the domain for both \( x \) and \( y \) being \( \{1, -2\} \).
- (a) Why is \( Q(-2, 1) \) false and \( Q(1, 2) \) true?
- (b) Find all values of \( x \) and \( y \) for which \( Q(x,y) \) is true.

### 4. Logical Statements and Their Truth Values
Evaluate the following statements:
- (a) \( @x \in \mathbb{R}, x > 2 \Rightarrow x > 1 \): True
- (b) \( @x \in \mathbb{R}, x > 2 \Rightarrow x^2 > 4 \): True
- (c) \( @x \in \mathbb{R}, x^2 > 4 \Rightarrow x > 2 \): False
- (d) \( @x \in \mathbb{R}, x^2 > 4 \lor |x| > 2 \): True

## Implementation/Examples
```plaintext
1. Translate the following into English:
   - @x (R(x) → H(x)): For every animal, if it is a rabbit, then it hops.
   - D x (R(x) ∧ H(x)): There is an animal that is a rabbit and hops.
```

> [!note] **Important Note**: Understanding the structure of logical statements is crucial for mastering discrete mathematics and computer science concepts.

> [!warning] **Caution**: Be careful with the negation of quantified statements, as they can lead to common logical fallacies if misinterpreted.

## Related
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[Midterm+Briefing]]