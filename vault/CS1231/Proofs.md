---
tags: [CS1231, proofs, induction, direct_proof, contradiction]
---

# Proofs

## Overview

A **proof** is a valid argument that establishes the truth of a mathematical statement. This chapter covers the main proof techniques used throughout discrete mathematics: direct proof, proof by contrapositive, proof by contradiction, proof by cases, existence and uniqueness proofs, and mathematical induction.

## Terminology

> [!note] Key Definitions
> - **Theorem**: A statement that can be shown to be true (sometimes called a **proposition** or **fact** for less important results).
> - **Axiom / Postulate**: A statement assumed to be true without proof.
> - **Lemma**: A "helper" theorem used to prove a larger theorem.
> - **Corollary**: A result that follows directly from a theorem.
> - **Conjecture**: A statement believed to be true but not yet proved.

## Even and Odd Integers

> [!note] Definition
> An integer $n$ is **even** if $n = 2k$ for some integer $k$.
> An integer $n$ is **odd** if $n = 2k + 1$ for some integer $k$.

## Divisibility

> [!note] Definition
> Let $a, b$ be integers with $a \neq 0$. We say $a$ **divides** $b$, written $a \mid b$, if there exists an integer $k$ such that $b = ak$. We say $a$ is a **factor** or **divisor** of $b$, and $b$ is a **multiple** of $a$.

## Direct Proof

To prove $\forall x \, (P(x) \rightarrow Q(x))$:
1. Assume $P(c)$ for an arbitrary $c$ from the domain.
2. Use definitions, axioms, and previously proven results to show $Q(c)$.
3. Conclude $\forall x \, (P(x) \rightarrow Q(x))$ by universal generalization.

**Example:** Prove "If $n$ is odd, then $n^2$ is odd."

*Proof.* Let $n$ be an arbitrary odd integer. Then $n = 2k + 1$ for some integer $k$. Thus:
$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
Since $2k^2 + 2k$ is an integer, $n^2$ is odd. $\blacksquare$

**Example:** Prove "If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$."

*Proof.* Assume $a \mid b$ and $a \mid c$. Then $b = as$ and $c = at$ for some integers $s, t$. Thus $b + c = as + at = a(s+t)$. Since $s + t$ is an integer, $a \mid (b+c)$. $\blacksquare$

## Proof by Contrapositive

To prove $P \rightarrow Q$, we can equivalently prove $\lnot Q \rightarrow \lnot P$ (the contrapositive).

1. Assume $\lnot Q$.
2. Show $\lnot P$.

> [!important] When to Use
> Use proof by contrapositive when it is easier to work with $\lnot Q$ than to work forward from $P$, or when the direct approach seems difficult.

**Example:** Prove "If $n^2$ is even, then $n$ is even."

*Proof.* We prove the contrapositive: "If $n$ is odd, then $n^2$ is odd."
Assume $n$ is odd, so $n = 2k+1$ for some integer $k$. Then $n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2+2k) + 1$, which is odd. $\blacksquare$

## Proof by Contradiction

To prove a statement $P$:
1. Assume $\lnot P$.
2. Derive a contradiction (a statement of the form $R \land \lnot R$).
3. Conclude $P$ must be true.

**Example:** Prove "$\sqrt{2}$ is irrational."

*Proof.* Suppose for contradiction that $\sqrt{2}$ is rational. Then $\sqrt{2} = \frac{a}{b}$ where $a, b$ are integers with $b \neq 0$ and $\gcd(a, b) = 1$ (lowest terms).

Squaring: $2 = \frac{a^2}{b^2}$, so $a^2 = 2b^2$.

Thus $a^2$ is even, so $a$ is even (by contrapositive proved above). Write $a = 2c$.

Then $(2c)^2 = 2b^2 \Rightarrow 4c^2 = 2b^2 \Rightarrow b^2 = 2c^2$.

Thus $b^2$ is even, so $b$ is even.

But $a$ and $b$ are both even, contradicting $\gcd(a,b) = 1$. $\blacksquare$

**Example:** Prove "There are infinitely many primes."

*Proof.* Suppose for contradiction there are finitely many primes: $p_1, p_2, \ldots, p_n$. Consider $Q = p_1 p_2 \cdots p_n + 1$. Then $Q > 1$, so $Q$ has a prime divisor $p$. But $p$ must be some $p_i$, and $p_i \mid (p_1 p_2 \cdots p_n)$, so $p_i \mid (Q - p_1 p_2 \cdots p_n) = 1$. But no prime divides 1. Contradiction. $\blacksquare$

## Proof by Cases (Exhaustive Proof)

To prove $(P_1 \lor P_2 \lor \cdots \lor P_n) \rightarrow Q$, prove each case $P_i \rightarrow Q$ separately.

**Example:** Prove "For every integer $n$, $n^2 + n$ is even."

*Proof.* Case 1: $n$ is even. Then $n = 2k$, so $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$, which is even.

Case 2: $n$ is odd. Then $n = 2k+1$, so $n^2 + n = (2k+1)^2 + (2k+1) = 4k^2 + 4k + 1 + 2k + 1 = 4k^2 + 6k + 2 = 2(2k^2 + 3k + 1)$, which is even.

In both cases, $n^2 + n$ is even. $\blacksquare$

> [!note] Without Loss of Generality (WLOG)
> When cases are symmetric, we can say "without loss of generality" and prove only one case.

## Existence Proofs

To prove $\exists x \, P(x)$:

**Constructive proof:** Explicitly find a witness $c$ and verify $P(c)$.

**Example:** Prove "There exists a positive integer that can be written as the sum of cubes in two different ways."
*Proof.* $1729 = 10^3 + 9^3 = 12^3 + 1^3$. $\blacksquare$

**Non-constructive proof:** Show that a witness must exist without finding one explicitly (often via contradiction).

## Uniqueness Proofs

To prove $\exists! x \, P(x)$ (there exists a unique $x$ with property $P$):
1. **Existence:** Show $\exists x \, P(x)$.
2. **Uniqueness:** Show that if $P(a)$ and $P(b)$, then $a = b$.

## Mathematical Induction

> [!note] Principle of Mathematical Induction
> To prove $\forall n \geq n_0, \, P(n)$:
> 1. **Base case:** Prove $P(n_0)$.
> 2. **Inductive step:** Prove $\forall k \geq n_0, \, P(k) \rightarrow P(k+1)$.
>    - Assume $P(k)$ (**inductive hypothesis**).
>    - Show $P(k+1)$.

> [!warning] Common Mistakes in Induction
> - Forgetting the base case.
> - Not clearly stating the inductive hypothesis.
> - Assuming what you want to prove (circular reasoning).
> - Starting with $P(k+1)$ and manipulating it (should start from $P(k)$ or known facts and arrive at $P(k+1)$).

**Example:** Prove $\displaystyle\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ for all $n \geq 1$.

*Proof.*

**Base case:** $n = 1$. LHS $= 1$. RHS $= \frac{1 \cdot 2}{2} = 1$. LHS = RHS. $\checkmark$

**Inductive step:** Assume $\displaystyle\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$ for some $k \geq 1$. Show $\displaystyle\sum_{i=1}^{k+1} i = \frac{(k+1)(k+2)}{2}$.

$$\sum_{i=1}^{k+1} i = \left(\sum_{i=1}^{k} i\right) + (k+1) = \frac{k(k+1)}{2} + (k+1)$$
$$= \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

By induction, the formula holds for all $n \geq 1$. $\blacksquare$

**Example:** Prove $n! > 2^n$ for all $n \geq 4$.

*Proof.*

**Base case:** $n = 4$. $4! = 24 > 16 = 2^4$. $\checkmark$

**Inductive step:** Assume $k! > 2^k$ for some $k \geq 4$. Show $(k+1)! > 2^{k+1}$.

$$(k+1)! = (k+1) \cdot k! > (k+1) \cdot 2^k \geq 5 \cdot 2^k > 2 \cdot 2^k = 2^{k+1}$$

(using $k+1 \geq 5 > 2$ since $k \geq 4$). $\blacksquare$

## Strong Induction

> [!note] Principle of Strong Induction
> To prove $\forall n \geq n_0, \, P(n)$:
> 1. **Base case(s):** Prove $P(n_0)$ (and possibly $P(n_0 + 1), \ldots, P(n_0 + j)$).
> 2. **Inductive step:** Prove that if $P(n_0) \land P(n_0+1) \land \cdots \land P(k)$ is true, then $P(k+1)$ is true.
>
> The inductive hypothesis is stronger: you assume $P(i)$ for **all** $n_0 \leq i \leq k$.

**Example:** Prove every integer $n \geq 2$ can be written as a product of primes.

*Proof.*

**Base case:** $n = 2$. $2$ is prime, so it is a product of primes (a single prime). $\checkmark$

**Inductive step:** Assume every integer $i$ with $2 \leq i \leq k$ can be written as a product of primes. Show $k+1$ can too.

If $k+1$ is prime, done. If $k+1$ is composite, then $k+1 = ab$ where $2 \leq a, b \leq k$. By the strong inductive hypothesis, both $a$ and $b$ are products of primes, so $k+1 = ab$ is also a product of primes. $\blacksquare$

## Structural Induction

Used to prove properties of recursively defined structures (strings, trees, etc.):
1. **Base case:** Prove the property for the base elements.
2. **Inductive step:** Assume the property holds for the sub-structures, and prove it holds for the structure built from them.

## Summary of Proof Techniques

| Technique | To Prove | Strategy |
|---|---|---|
| **Direct proof** | $P \rightarrow Q$ | Assume $P$, derive $Q$ |
| **Contrapositive** | $P \rightarrow Q$ | Assume $\lnot Q$, derive $\lnot P$ |
| **Contradiction** | $P$ | Assume $\lnot P$, derive a contradiction |
| **Cases** | $P \rightarrow Q$ where $P = P_1 \lor \cdots \lor P_n$ | Prove each $P_i \rightarrow Q$ |
| **Induction** | $\forall n \geq n_0, P(n)$ | Base case + inductive step |
| **Strong induction** | $\forall n \geq n_0, P(n)$ | Base case(s) + strong inductive step |
| **Existence (constructive)** | $\exists x, P(x)$ | Exhibit a witness |
| **Existence (non-constructive)** | $\exists x, P(x)$ | Show non-existence leads to contradiction |
| **Uniqueness** | $\exists! x, P(x)$ | Existence + if $P(a) \land P(b)$ then $a = b$ |

## Related Notes

- [[Logic - Propositional Logic]] - Logical equivalences used in proofs
- [[Logic - Predicate Logic]] - Rules of inference that justify proof steps
- [[Sets]] - Proving set identities using element-wise proofs
- [[Functions]] - Proving injectivity, surjectivity via direct/contrapositive proofs
- [[Relations]] - Proving properties of relations (reflexivity, symmetry, transitivity)
