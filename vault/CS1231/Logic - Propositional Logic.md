---
tags: [CS1231, logic, propositional_logic, truth_tables, connectives]
---

# Propositional Logic

## Overview

Propositional logic is the foundation of mathematical reasoning. It deals with **propositions** -- declarative statements that are either true or false, but not both. We study how to combine propositions using **logical connectives** and determine the truth values of compound propositions.

## Propositions

> [!note] Definition: Proposition
> A **proposition** is a declarative sentence that is either **true (T)** or **false (F)**, but not both.

**Examples of propositions:**
- "1 + 1 = 2" (True)
- "Toronto is the capital of Canada" (False)
- "$2^{10} = 1024$" (True)

**Non-propositions (not declarative or truth value undefined):**
- "What time is it?" (question)
- "x + 1 = 2" (truth value depends on $x$, so this is a **predicate**, not a proposition)
- "Do your homework!" (command)

We typically denote propositions by lowercase letters: $p, q, r, s, \ldots$

## Logical Connectives

### Negation ($\lnot$)

> [!note] Definition: Negation
> The **negation** of $p$, denoted $\lnot p$ (read "not $p$"), is the proposition that is true when $p$ is false, and false when $p$ is true.

| $p$ | $\lnot p$ |
|:---:|:---:|
| T | F |
| F | T |

### Conjunction ($\land$)

> [!note] Definition: Conjunction
> The **conjunction** of $p$ and $q$, denoted $p \land q$ (read "$p$ and $q$"), is true when both $p$ and $q$ are true, and false otherwise.

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

### Disjunction ($\lor$)

> [!note] Definition: Disjunction
> The **disjunction** of $p$ and $q$, denoted $p \lor q$ (read "$p$ or $q$"), is true when at least one of $p$ or $q$ is true, and false only when both are false. This is the **inclusive or**.

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### Exclusive Or ($\oplus$)

> [!note] Definition: Exclusive Or
> The **exclusive or** of $p$ and $q$, denoted $p \oplus q$, is true when exactly one of $p$ or $q$ is true, and false otherwise.

| $p$ | $q$ | $p \oplus q$ |
|:---:|:---:|:---:|
| T | T | F |
| T | F | T |
| F | T | T |
| F | F | F |

### Conditional / Implication ($\rightarrow$)

> [!note] Definition: Conditional Statement
> The **conditional statement** $p \rightarrow q$ (read "if $p$ then $q$") is false only when $p$ is true and $q$ is false. Here $p$ is the **hypothesis** (antecedent) and $q$ is the **conclusion** (consequent).

| $p$ | $q$ | $p \rightarrow q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

> [!warning] Vacuous Truth
> When $p$ is false, $p \rightarrow q$ is **vacuously true** regardless of $q$. This is a common source of confusion. The implication only "promises" something when the hypothesis is true.

**Ways to express $p \rightarrow q$:**
- "if $p$, then $q$"
- "$p$ implies $q$"
- "$p$ only if $q$"
- "$q$ if $p$"
- "$p$ is sufficient for $q$"
- "$q$ is necessary for $p$"
- "$q$ whenever $p$"
- "$q$ unless $\lnot p$"

**Related conditionals:**

| Name | Statement | Form |
|---|---|---|
| **Conditional** | $p \rightarrow q$ | "if $p$ then $q$" |
| **Converse** | $q \rightarrow p$ | "if $q$ then $p$" |
| **Inverse** | $\lnot p \rightarrow \lnot q$ | "if not $p$ then not $q$" |
| **Contrapositive** | $\lnot q \rightarrow \lnot p$ | "if not $q$ then not $p$" |

> [!important] Key Fact
> A conditional and its **contrapositive** are logically equivalent: $p \rightarrow q \equiv \lnot q \rightarrow \lnot p$.
> A conditional and its **converse** are **NOT** logically equivalent.
> A conditional and its **inverse** are **NOT** logically equivalent.
> The converse and inverse are logically equivalent to each other.

### Biconditional ($\leftrightarrow$)

> [!note] Definition: Biconditional
> The **biconditional** $p \leftrightarrow q$ (read "$p$ if and only if $q$", abbreviated "$p$ iff $q$") is true when $p$ and $q$ have the **same** truth value.

| $p$ | $q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

$$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$$

## Operator Precedence

| Precedence (highest first) | Operator |
|---|---|
| 1 | $\lnot$ |
| 2 | $\land$ |
| 3 | $\lor$ |
| 4 | $\rightarrow$ |
| 5 | $\leftrightarrow$ |

So $\lnot p \land q \rightarrow r$ means $((\lnot p) \land q) \rightarrow r$.

## Truth Tables

A truth table lists all possible combinations of truth values for the propositional variables and the resulting truth value of the compound proposition.

For $n$ propositional variables, there are $2^n$ rows.

**Example:** Construct the truth table for $(p \rightarrow q) \land (\lnot p \rightarrow r)$

| $p$ | $q$ | $r$ | $p \rightarrow q$ | $\lnot p$ | $\lnot p \rightarrow r$ | $(p \rightarrow q) \land (\lnot p \rightarrow r)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| T | T | T | T | F | T | T |
| T | T | F | T | F | T | T |
| T | F | T | F | F | T | F |
| T | F | F | F | F | T | F |
| F | T | T | T | T | T | T |
| F | T | F | T | T | F | F |
| F | F | T | T | T | T | T |
| F | F | F | T | T | F | F |

## Logical Equivalences

> [!note] Definition: Logical Equivalence
> Two compound propositions $p$ and $q$ are **logically equivalent**, denoted $p \equiv q$, if they have the same truth value in every possible case (i.e., identical truth tables). A compound proposition that is always true is a **tautology**; always false is a **contradiction**; and sometimes true, sometimes false is a **contingency**.

### Important Logical Equivalences

**Identity Laws:**
$$p \land T \equiv p \qquad p \lor F \equiv p$$

**Domination Laws:**
$$p \lor T \equiv T \qquad p \land F \equiv F$$

**Idempotent Laws:**
$$p \lor p \equiv p \qquad p \land p \equiv p$$

**Double Negation:**
$$\lnot(\lnot p) \equiv p$$

**Commutative Laws:**
$$p \lor q \equiv q \lor p \qquad p \land q \equiv q \land p$$

**Associative Laws:**
$$p \lor (q \lor r) \equiv (p \lor q) \lor r \qquad p \land (q \land r) \equiv (p \land q) \land r$$

**Distributive Laws:**
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
$$p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$$

**De Morgan's Laws:**
$$\lnot(p \land q) \equiv \lnot p \lor \lnot q$$
$$\lnot(p \lor q) \equiv \lnot p \land \lnot q$$

**Absorption Laws:**
$$p \lor (p \land q) \equiv p \qquad p \land (p \lor q) \equiv p$$

**Negation Laws:**
$$p \lor \lnot p \equiv T \qquad p \land \lnot p \equiv F$$

### Equivalences Involving Conditionals

$$p \rightarrow q \equiv \lnot p \lor q$$

$$p \rightarrow q \equiv \lnot q \rightarrow \lnot p \quad \text{(contrapositive)}$$

$$p \lor q \equiv \lnot p \rightarrow q$$

$$p \land q \equiv \lnot(p \rightarrow \lnot q)$$

$$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$$

$$p \leftrightarrow q \equiv \lnot p \leftrightarrow \lnot q$$

$$p \leftrightarrow q \equiv (p \land q) \lor (\lnot p \land \lnot q)$$

$$\lnot(p \leftrightarrow q) \equiv p \oplus q$$

## Proving Logical Equivalence

Two methods:

1. **Truth table method:** Construct truth tables for both sides and verify all rows match.
2. **Using known equivalences:** Apply a chain of known equivalences to transform one side into the other.

**Example:** Show that $\lnot(p \rightarrow q) \equiv p \land \lnot q$

$$\lnot(p \rightarrow q) \equiv \lnot(\lnot p \lor q) \quad \text{(conditional equivalence)}$$
$$\equiv \lnot(\lnot p) \land \lnot q \quad \text{(De Morgan's)}$$
$$\equiv p \land \lnot q \quad \text{(double negation)}$$

**Example:** Show that $\lnot(p \lor (\lnot p \land q)) \equiv \lnot p \land \lnot q$

$$\lnot(p \lor (\lnot p \land q)) \equiv \lnot p \land \lnot(\lnot p \land q) \quad \text{(De Morgan's)}$$
$$\equiv \lnot p \land (\lnot(\lnot p) \lor \lnot q) \quad \text{(De Morgan's)}$$
$$\equiv \lnot p \land (p \lor \lnot q) \quad \text{(double negation)}$$
$$\equiv (\lnot p \land p) \lor (\lnot p \land \lnot q) \quad \text{(distributive)}$$
$$\equiv F \lor (\lnot p \land \lnot q) \quad \text{(negation law)}$$
$$\equiv \lnot p \land \lnot q \quad \text{(identity law)}$$

## Satisfiability

> [!note] Definition: Satisfiable
> A compound proposition is **satisfiable** if there exists an assignment of truth values to its variables that makes it true. It is **unsatisfiable** if it is a contradiction (false for every assignment).

## Related Notes

- [[Logic - Predicate Logic]] - Extension to predicates and quantifiers
- [[Proofs]] - Using logic to construct mathematical proofs
- [[Sets]] - Set operations parallel logical connectives (De Morgan's, distributive, etc.)
