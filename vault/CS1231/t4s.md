---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 4

## Overview
This note summarizes the key points and solutions from CS1231 Tutorial 4, focusing on logical reasoning, set theory, and proof techniques. The tutorial covers various problems related to propositional logic, set operations, and their properties, providing a comprehensive understanding of the underlying concepts. The solutions demonstrate the application of logical principles and set theory in problem-solving.

## Key Concepts & Definitions
- **Propositional Logic**: A branch of logic dealing with propositions that can be true or false. See [[Logic - Propositional Logic]].
- **Set Operations**: Fundamental operations including union, intersection, and difference. Refer to [[ch2]] for more details.
- **Cardinality**: The number of elements in a set, denoted as |A|. 
- **Power Set**: The set of all subsets of a set A, denoted as P(A).
- **Disjoint Sets**: Two sets A and B are disjoint if their intersection is empty, i.e., A ∩ B = ∅.

## Detailed Technical Breakdown

### Problem Solutions
1. **Truth Values**: 
   - Given: T, T, F, T, T, T, F

2. **Set Membership**:
   - If \( n \in B \), then \( n = 3j + 2 \) for some \( j \in \mathbb{Z} \). Thus, \( n \in D \) as \( n = 3(j + 1) - 1 \). Conversely, if \( n \in D \), then \( n = 3j - 1 \) implies \( n \in B \). Therefore, \( B = D \).

3. **Cardinality**:
   - \( |A| = 5 \)

4. **Set Comparison**:
   - Sets {a} and {a, b, c} are not equal.

5. **Logical Implications**:
   - (a) Let \( x \in T \). Then \( P(x) \lor Q(x) \) is true, leading to \( x \in T \cup T \).
   - (b) \( P \to Q \equiv \neg P \lor Q \) and \( T = T \).

6. **Cartesian Products**:
   - \( (A \times B) \times C \) and \( A \times (B \times C) \) yield different results.

7. **Set Membership Implications**:
   - \( x \notin A \) or \( x \notin B \) does not imply \( x \notin A \cup B \). Counterexample: \( A = \{1\}, B = \{2\}, x = 1 \).

8. **Set Intersection**:
   - If \( \exists x \in (A - C) \cap (B - C) \cap (A - B) \), a contradiction arises, proving \( (A - C) \cap (B - C) \cap (A - B) = \emptyset \).

9. **Cartesian Product Intersection**:
   - If \( \exists (x, y) \in (A \times B) \cap (C \times D) \), a contradiction arises, proving \( (A \times B) \cap (C \times D) = \emptyset \).

10. **Set Properties**:
    - (a) False. Counterexample: \( A = \{1, 2, 3\}, B = \{3\}, C = \{2\} \).
    - (b) False. Same counterexample.
    - (c) True. \( A \cup B \subseteq U \) implies \( U \subseteq A \cup B \).
    - (d) True. \( P(A \cap B) \subseteq P(A) \cap P(B) \).

11. **Logical Equivalence**:
    - (a) Proves \( LHS = RHS \) through logical deductions.
    - (b) Truth table analysis confirms equivalence.

12. **Set Equality**:
    - (a) \( \{1, 2, 7, 8\} \).
    - (b) Proves \( A = B \) through direct and contrapositive proofs.

## Implementation/Examples
```plaintext
1. Truth Values: T, T, F, T, T, T, F
2. Set Membership: If n ∈ B, then n = 3j + 2.
3. Cardinality: |A| = 5
4. Set Comparison: {a} ≠ {a, b, c}
5. Logical Implications: P → Q ≡ ¬P ∨ Q
```

> [!note] **Important Note**: Understanding the properties of sets and logical implications is crucial for mastering the concepts in CS1231. Review the definitions and examples provided in this tutorial to reinforce your understanding.

> [!warning] **Caution**: Be careful with counterexamples, as they can often reveal the truth or falsity of a statement in set theory and logic.

## Related
- See [[AY2122+Sem1+Homework+3]] for additional practice problems.
- Refer to [[CS1231+TUTORIAL+3]] for previous tutorial content.
- Explore [[Midterm+Briefing]] for exam preparation resources.