---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 4: Induction

## Overview
This chapter delves into the concept of [[Mathematical Induction]], a fundamental proof technique used to establish the truth of propositions for all natural numbers. The principle consists of two main steps: the basis step, where the proposition is verified for the initial case, and the inductive step, where the truth for a general case is shown based on the assumption that it holds for all preceding cases.

## Key Concepts & Definitions
- **Mathematical Induction**: A method of proof used to establish the validity of a statement for all natural numbers.
- **Basis Step**: The initial verification that the proposition holds for the first natural number.
- **Inductive Step**: The process of proving that if the proposition holds for an arbitrary natural number \( k \), it also holds for \( k + 1 \).
- **Induction Hypothesis**: The assumption that the proposition is true for all natural numbers up to \( k \).

## Detailed Technical Breakdown

### Principle of Mathematical Induction
To prove that \( \forall n \in \mathbb{Z}^+, P(n) \) is true, follow these steps:
1. **Basis Step**: Verify that \( P(1) \) is true.
2. **Inductive Step**: Show that \( \forall k \in \mathbb{Z}^+, (P(1) \land P(2) \land \ldots \land P(k)) \implies P(k + 1) \).

### Example 1: Sum of the First \( n \) Natural Numbers
- **Proposition**: \( \sum_{i=1}^{n} i = \frac{n(n + 1)}{2} \)
- **Proof**:
  - **Basis Step**: For \( n = 1 \), \( \sum_{i=1}^{1} i = 1 = \frac{1(1 + 1)}{2} \).
  - **Inductive Step**: Assume true for \( k \):
    \[
    \sum_{i=1}^{k} i = \frac{k(k + 1)}{2}
    \]
    Show for \( k + 1 \):
    \[
    \sum_{i=1}^{k + 1} i = \sum_{i=1}^{k} i + (k + 1) = \frac{k(k + 1)}{2} + (k + 1) = \frac{(k + 1)(k + 2)}{2}
    \]

### Example 2: Proving \( n < 2^n \) for all \( n \in \mathbb{Z}^+ \)
- **Proof**:
  - **Basis Step**: For \( n = 1 \), \( 1 < 2^1 \).
  - **Inductive Step**: Assume true for \( k \):
    \[
    k < 2^k
    \]
    Show for \( k + 1 \):
    \[
    k + 1 < 2^k + 1 < 2^k + 2^k = 2^{k + 1}
    \]

### Example 3: Harmonic Numbers
- **Definition**: \( H_n = \sum_{i=1}^{n} \frac{1}{i} \)
- **Proposition**: \( H_n \geq 1 + \frac{n}{2} \)
- **Proof**:
  - **Basis Step**: For \( n = 1 \), \( H_1 = 1 \geq 1 + 0 \).
  - **Inductive Step**: Assume true for \( k \):
    \[
    H_k \geq 1 + \frac{k}{2}
    \]
    Show for \( k + 1 \):
    \[
    H_{k + 1} = H_k + \frac{1}{k + 1} \geq 1 + \frac{k}{2} + \frac{1}{k + 1}
    \]

## Implementation/Examples
```markdown
# Example of Mathematical Induction in Code
def sum_n(n):
    return n * (n + 1) // 2

# Testing the function
for i in range(1, 6):
    print(f"Sum of first {i} natural numbers: {sum_n(i)}")
```

> [!note] **Important**: The principle of mathematical induction is not just a technique but a powerful tool in proving theorems across various fields of mathematics and computer science.
> 
> [!warning] **Caution**: Ensure that both the basis and inductive steps are correctly established; failure in either can invalidate the proof.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]