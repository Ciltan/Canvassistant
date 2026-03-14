---
tags: [CS1231, logic, predicate_logic, quantifiers, inference]
---

# Predicate Logic

## Overview

Predicate logic extends propositional logic by allowing us to reason about **properties of objects** and **relationships between objects**. It introduces **predicates**, **quantifiers**, and **rules of inference** that form the backbone of mathematical proof.

## Predicates and Propositional Functions

> [!note] Definition: Predicate
> A **predicate** (or **propositional function**) is a statement involving one or more variables that becomes a proposition when specific values are substituted for the variables.

**Example:** Let $P(x)$ denote "$x > 3$."
- $P(4)$ is the proposition "$4 > 3$" which is **true**
- $P(2)$ is the proposition "$2 > 3$" which is **false**

A predicate $P(x)$ has:
- **Variable(s):** $x$ (the subject)
- **Domain** (or **universe of discourse**): the set of all possible values for $x$

**Multi-variable predicates:** $Q(x, y)$ could denote "$x + y = 5$". This becomes a proposition when both $x$ and $y$ are given values from a specified domain.

## Quantifiers

### Universal Quantifier ($\forall$)

> [!note] Definition: Universal Quantifier
> The **universal quantification** of $P(x)$ is the statement "$P(x)$ for all values of $x$ in the domain," written $\forall x \, P(x)$. It is true when $P(x)$ is true for **every** $x$ in the domain, and false if there exists **at least one** $x$ for which $P(x)$ is false (such an $x$ is a **counterexample**).

**Example:** Let the domain be all integers. "$\forall x \, (x^2 \geq 0)$" is **true**.

> [!warning] Important
> When the domain is empty, $\forall x \, P(x)$ is **vacuously true** for any predicate $P$.

If the domain is finite, say $\{a_1, a_2, \ldots, a_n\}$, then:
$$\forall x \, P(x) \equiv P(a_1) \land P(a_2) \land \cdots \land P(a_n)$$

### Existential Quantifier ($\exists$)

> [!note] Definition: Existential Quantifier
> The **existential quantification** of $P(x)$ is the statement "there exists an $x$ in the domain such that $P(x)$," written $\exists x \, P(x)$. It is true when $P(x)$ is true for **at least one** $x$ in the domain.

**Example:** Let the domain be all real numbers. "$\exists x \, (x^2 = 2)$" is **true** (take $x = \sqrt{2}$).

If the domain is finite:
$$\exists x \, P(x) \equiv P(a_1) \lor P(a_2) \lor \cdots \lor P(a_n)$$

### Uniqueness Quantifier ($\exists!$)

> [!note] Definition: Uniqueness Quantifier
> $\exists! x \, P(x)$ means "there exists a **unique** $x$ such that $P(x)$." Formally:
> $$\exists! x \, P(x) \equiv \exists x \, (P(x) \land \forall y \, (P(y) \rightarrow y = x))$$

## Negating Quantifiers (De Morgan's Laws for Quantifiers)

$$\lnot \forall x \, P(x) \equiv \exists x \, \lnot P(x)$$

$$\lnot \exists x \, P(x) \equiv \forall x \, \lnot P(x)$$

> [!important] Intuition
> - "Not everything is $P$" is the same as "something is not $P$"
> - "Nothing is $P$" is the same as "everything is not $P$"

**Example:** Negate "$\forall x \, (x^2 > x)$":
$$\lnot \forall x \, (x^2 > x) \equiv \exists x \, \lnot(x^2 > x) \equiv \exists x \, (x^2 \leq x)$$

## Nested Quantifiers

Many mathematical statements require **multiple quantifiers**.

**Reading nested quantifiers:** Read left to right.

| Statement | Meaning |
|---|---|
| $\forall x \, \forall y \, P(x,y)$ | For every $x$ and every $y$, $P(x,y)$ |
| $\forall x \, \exists y \, P(x,y)$ | For every $x$, there exists a $y$ such that $P(x,y)$ |
| $\exists x \, \forall y \, P(x,y)$ | There exists an $x$ such that for every $y$, $P(x,y)$ |
| $\exists x \, \exists y \, P(x,y)$ | There exist an $x$ and a $y$ such that $P(x,y)$ |

> [!warning] Order Matters!
> $\forall x \, \exists y \, P(x,y)$ and $\exists y \, \forall x \, P(x,y)$ are generally **NOT** equivalent.
>
> - $\forall x \, \exists y \, (x + y = 0)$: For every $x$ there is a $y$ such that $x + y = 0$. **True** (take $y = -x$).
> - $\exists y \, \forall x \, (x + y = 0)$: There is a single $y$ that works for ALL $x$. **False**.
>
> However: $\exists x \, \forall y \, P(x,y) \rightarrow \forall y \, \exists x \, P(x,y)$ is always true (but not the converse).

### Negating Nested Quantifiers

Apply De Morgan's laws repeatedly, moving negation inward:

$$\lnot \forall x \, \exists y \, P(x,y) \equiv \exists x \, \lnot \exists y \, P(x,y) \equiv \exists x \, \forall y \, \lnot P(x,y)$$

**General rule:** Push $\lnot$ inward, flipping each quantifier ($\forall \leftrightarrow \exists$) until it reaches the predicate.

## Translating Between English and Logic

**Example 1:** "Every student in this class has taken a course in Java."
- Let $S(x)$: "$x$ is a student in this class," $J(x)$: "$x$ has taken a Java course."
- Domain: all people.
- Translation: $\forall x \, (S(x) \rightarrow J(x))$

> [!warning] Common Mistake
> Do NOT write $\forall x \, (S(x) \land J(x))$ -- this says everyone in the universe is both a student in this class AND has taken Java.

**Example 2:** "Some student in this class has taken a course in Java."
- Translation: $\exists x \, (S(x) \land J(x))$

> [!warning] Common Mistake
> Do NOT write $\exists x \, (S(x) \rightarrow J(x))$ -- this is true if there exists anyone who is NOT a student (since $F \rightarrow J(x)$ is vacuously true).

**Pattern:**
- $\forall$ typically pairs with $\rightarrow$
- $\exists$ typically pairs with $\land$

## Rules of Inference

Rules of inference are templates for constructing valid arguments. An **argument** is a sequence of propositions (premises) leading to a conclusion. An argument is **valid** if the conclusion follows necessarily from the premises.

### Rules of Inference for Propositional Logic

| Rule | Tautology | Name |
|---|---|---|
| $p, \; p \rightarrow q \;\therefore q$ | $(p \land (p \rightarrow q)) \rightarrow q$ | **Modus Ponens** |
| $\lnot q, \; p \rightarrow q \;\therefore \lnot p$ | $(\lnot q \land (p \rightarrow q)) \rightarrow \lnot p$ | **Modus Tollens** |
| $p \rightarrow q, \; q \rightarrow r \;\therefore p \rightarrow r$ | $((p \rightarrow q) \land (q \rightarrow r)) \rightarrow (p \rightarrow r)$ | **Hypothetical Syllogism** |
| $p \lor q, \; \lnot p \;\therefore q$ | $((p \lor q) \land \lnot p) \rightarrow q$ | **Disjunctive Syllogism** |
| $p \;\therefore p \lor q$ | $p \rightarrow (p \lor q)$ | **Addition** |
| $p \land q \;\therefore p$ | $(p \land q) \rightarrow p$ | **Simplification** |
| $p, \; q \;\therefore p \land q$ | $((p) \land (q)) \rightarrow (p \land q)$ | **Conjunction** |
| $p \lor q, \; \lnot p \lor r \;\therefore q \lor r$ | $((p \lor q) \land (\lnot p \lor r)) \rightarrow (q \lor r)$ | **Resolution** |

### Rules of Inference for Quantified Statements

| Rule | Name |
|---|---|
| $\forall x \, P(x) \;\therefore P(c)$ for any $c$ in domain | **Universal Instantiation (UI)** |
| $P(c)$ for arbitrary $c \;\therefore \forall x \, P(x)$ | **Universal Generalization (UG)** |
| $\exists x \, P(x) \;\therefore P(c)$ for some specific $c$ | **Existential Instantiation (EI)** |
| $P(c)$ for some specific $c \;\therefore \exists x \, P(x)$ | **Existential Generalization (EG)** |

> [!important] Restrictions
> - **UG**: $c$ must be **arbitrary** (no assumptions about $c$ beyond being in the domain).
> - **EI**: $c$ must be a **new** constant not previously used in the proof; it represents a specific (but unknown) element.

### Example: Constructing a Valid Argument

**Prove:** "Socrates is mortal" from "All men are mortal" and "Socrates is a man."

| Step | Statement | Justification |
|---|---|---|
| 1 | $\forall x \, (Man(x) \rightarrow Mortal(x))$ | Premise |
| 2 | $Man(Socrates)$ | Premise |
| 3 | $Man(Socrates) \rightarrow Mortal(Socrates)$ | Universal Instantiation on (1) |
| 4 | $Mortal(Socrates)$ | Modus Ponens on (2) and (3) |

## Common Fallacies

| Fallacy | Form | Why it fails |
|---|---|---|
| **Affirming the consequent** | $q, \; p \rightarrow q \;\therefore p$ | $q$ can be true for other reasons |
| **Denying the antecedent** | $\lnot p, \; p \rightarrow q \;\therefore \lnot q$ | $q$ may still hold via other conditions |

## Related Notes

- [[Logic - Propositional Logic]] - Foundations: connectives, truth tables, equivalences
- [[Proofs]] - Applying rules of inference to write mathematical proofs
- [[Sets]] - Quantifiers used extensively in set definitions and proofs
