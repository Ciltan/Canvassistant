---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 2 Notes

## Overview
This tutorial focuses on the application of [[Logic - Propositional Logic]] and quantifiers in mathematical reasoning. It covers the translation of logical statements involving predicates and quantifiers, the evaluation of truth values for specific cases, and the formulation of negations. The exercises aim to deepen understanding of logical expressions and their implications in various contexts.

## Key Concepts & Definitions
- **Predicate**: A statement that contains a variable and becomes a proposition when the variable is replaced with a specific value.
- **Quantifiers**: Symbols used in logic to express the quantity of specimens in the domain that satisfy a given predicate. The two main types are:
  - **Universal Quantifier (∀)**: Indicates that a statement is true for all elements in a domain.
  - **Existential Quantifier (∃)**: Indicates that there exists at least one element in the domain for which the statement is true.
- **Negation**: The logical operation that inverts the truth value of a proposition.

## Detailed Technical Breakdown

### 1. Translation of Logical Statements
- **(a)** ∀x(R(x) → H(x)): For all animals, if x is a rabbit, then x hops.
- **(b)** ∀x(R(x) ∧ H(x)): For all animals, x is a rabbit and x hops.
- **(c)** ∃x(R(x) → H(x)): There exists an animal x such that if x is a rabbit, then x hops.
- **(d)** ∃x(R(x) ∧ H(x)): There exists an animal x such that x is a rabbit and x hops.

### 2. Evaluation of Predicate Q(x,y)
- **(a)** Q(x,y) is false for (x,y) = (−2,1) because (-2 < 1) is true, but (-2)^2 < 1^2 (4 < 1) is false.
- **(b)** Q(x,y) is true for (x,y) = (1,2) because (1 < 2) is true and (1)^2 < (2)^2 (1 < 4) is true.
- **True values of Q(x,y)**: (1, 2), (1, -2), (-2, 2).

### 3. Rewriting Statements in Universal Form
- **(a)** ∀x (If x has an even square, then x is even).
- **(b)** ∀x (If x is an integer and x^2 is even, then x is even).
- **(c)** ∀x (If x is an even integer, then x^2 is even).
- **(d)** ∀x (If x is an even integer, then x has an even square).

### 4. Truth Evaluation of Statements
- **(a)** True: ∀x ∈ R, x > 2 → x > 1.
- **(b)** True: ∀x ∈ R, x > 2 → x^2 > 4.
- **(c)** False: ∀x ∈ R, x^2 > 4 → x > 2 (Counterexample: x = -3).
- **(d)** True: ∀x ∈ R, x^2 > 4 ↔ |x| > 2.

### 5. Expressing Statements with Quantifiers
- **(a)** ∀x (D(x) → ¬W(x)): No ducks are willing to waltz.
- **(b)** ∀x (O(x) → W(x)): No officers ever decline to waltz.
- **(c)** ∀x (P(x) → D(x)): All my poultry are ducks.
- **(d)** ∀x (P(x) → ¬O(x)): My poultry are not officers.
- **(e)** If (a), (b), (c) are true, (d) does not necessarily follow.

### 6. Negation of Statements
- **(a)** ¬∀d ∈ Z, (6 ∈ Z → d = 3): There exists a d in Z such that 6 ∈ Z and d ≠ 3.
- **(b)** ¬(If the square of an integer is odd, then the integer is odd): There exists an integer whose square is odd and the integer is even.

### 7. Rewriting Without "Necessary" or "Sufficient"
- **(a)** Being a bird is not a condition for an animal being able to fly.
- **(b)** Being a polynomial does not guarantee that a function has a real root.

### 8. Negation of Existential Statements
- Negation: ¬∃x ∈ D such that ∀y ∈ E, x + y = -y.
- Truth evaluation: The original statement is true if there exists an x in D that satisfies the condition.

### 9. Negation of Logical Statements
- **(a)** ¬∀r ∈ Q, ∃a ∈ Z, ∃b ∈ Z such that r = a/b: There exists an r in Q such that for all a in Z, for all b in Z, r ≠ a/b.
- **(b)** ¬∃x ∈ R such that ∀y ∈ R, x + y = 0: For all x in R, there exists a y in R such that x + y ≠ 0.
- **(c)** ¬(p ↔ q): (p ∧ ¬q) ∨ (¬p ∧ q).

### 10. Logical Expression for Exclusive OR
- S = (p ∧ ¬q) ∨ (¬p ∧ q)

### 11. Unique Existence Quantification
- ∃!x P(x) can be expressed as ∃x (P(x) ∧ ∀y (P(y) → y = x)).
- Negation: ¬(∃x (P(x) ∧ ∀y (P(y) → y = x))) translates to "There is no unique x such that P(x) is true."

### 12. Quantified Statements about Readers and Genres
- **(a)** ∃t ∈ T, ∀r ∈ R (Female(r) → Reads(r, t)): Some title is read by all female readers.
- **(b)** ∀r ∈ R, ∀g ∈ G, ∃t ∈ T (Reads(r, t) ∧ BelongsTo(t, g)): Every reader reads some title in every genre.
- **(c)** ∃r ∈ R, ∀t ∈ T (Reads(r, t)): Some reader reads all titles of some genre.
- **(d)** ∃g ∈ G, ∃r ∈ R (¬Reads(r, t) ∧ BelongsTo(t, g)): There is some genre for which some reader does not read any of its titles.
- **(e)** ∃g ∈ G, ∀t ∈ T (Reads(f, t) → Reads(m, t)): There is a genre in which every title read by a female reader is also read by a male reader.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]