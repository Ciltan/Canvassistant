---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 4: Induction

## Overview
This chapter delves into the concept of [[Mathematical Induction]], a fundamental proof technique used to establish the truth of propositions for all natural numbers. The principle consists of two main steps: the basis step and the inductive step, which together form a robust framework for proving various mathematical statements. Through examples, we explore the application of induction in proving summations, inequalities, and properties of sequences.

## Key Concepts & Definitions
- **Mathematical Induction**: A method of proof used to establish that a statement holds for all natural numbers.
- **Basis Step**: The initial step in mathematical induction where the statement is verified for the first natural number.
- **Inductive Step**: The step where we assume the statement holds for an arbitrary natural number \( k \) and prove it for \( k + 1 \).
- **Induction Hypothesis**: The assumption that the statement is true for all integers up to \( k \).
- **Harmonic Numbers**: Defined as \( H_j = 1 + \frac{1}{2} + \frac{1}{3} + \ldots + \frac{1}{j} \).
- **Fibonacci Numbers**: A sequence defined by \( F_0 = 0, F_1 = 1 \), and \( F_n = F_{n-1} + F_{n-2} \) for \( n \geq 2 \).

## Detailed Technical Breakdown

### Principle of Mathematical Induction
1. **Basis Step**: Verify that \( P(1) \) is true.
2. **Inductive Step**: Show that if \( P(k) \) is true, then \( P(k + 1) \) is also true.

### Examples of Mathematical Induction
- **Sum of First \( n \) Natural Numbers**:
  - Proposition: \( \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \)
  - Proof involves verifying the basis step and using the inductive hypothesis.

- **Inequality**: Prove that \( n < 2^n \) for all \( n \in \mathbb{Z}^+ \).
  
- **Harmonic Numbers**: Prove that \( H_{2n} \geq 1 + \frac{n}{2} \).

### Theorem: Number of Subsets of a Finite Set
- Proposition: A set with \( n \) elements has \( 2^n \) subsets.
- Proof involves the basis step and inductive reasoning.

### Sum of Geometric Progression
- Proposition: For all integers \( n \geq 0 \) and \( r \neq 1 \):
  \[
  \sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}
  \]

### L-tromino Covering Problem
- Prove that for any integer \( n \geq 1 \), if one square is removed from a \( 2^n \times 2^n \) checkerboard, the remaining squares can be covered by L-trominoes.

### Fibonacci Numbers
- Prove that for \( n \geq 3 \), \( F_n > \phi^{n-2} \), where \( \phi = \frac{1 + \sqrt{5}}{2} \).

### Lame's Theorem
- States that the number of divisions used by the Euclidean algorithm to find \( \gcd(a, b) \) is at most \( 5 \) times the number of decimal digits in \( b \).

## Implementation/Examples
```markdown
### Example Proof of Sum of First n Natural Numbers
Let \( P(n) \) be the proposition that \( \sum_{i=1}^{n} i = \frac{n(n+1)}{2} \).

**Basis Step**: For \( n = 1 \):
\[
\sum_{i=1}^{1} i = 1 = \frac{1(1+1)}{2}
\]

**Inductive Step**: Assume true for \( n = k \):
\[
\sum_{i=1}^{k} i = \frac{k(k+1)}{2}
\]
Prove for \( n = k + 1 \):
\[
\sum_{i=1}^{k+1} i = \sum_{i=1}^{k} i + (k + 1) = \frac{k(k+1)}{2} + (k + 1) = \frac{(k + 1)(k + 2)}{2}
\]
Thus, \( P(k + 1) \) is true.
```

> [!note] **Induction Hypothesis**: Remember that the inductive step relies on the assumption that the statement holds for all integers up to \( k \).
> 
> [!important] **Key Takeaway**: Mathematical induction is a powerful tool in proving statements about integers, and understanding its structure is crucial for success in mathematical proofs.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]