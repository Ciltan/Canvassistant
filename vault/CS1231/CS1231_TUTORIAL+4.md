---
tags: [CS1231, lecture-notes, academic]
---

# CS1231: Discrete Structures - Tutorial 4

## Overview
This tutorial focuses on fundamental concepts in discrete mathematics, particularly set theory and logic. Key topics include definitions of set operations, truth sets, and properties of subsets. The tutorial also emphasizes the importance of understanding the relationships between sets and their elements, as well as the implications of logical statements.

## Key Concepts & Definitions
- **Set Operations**: 
  - **Union**: \( A \cup B \) - the set of elements in either \( A \) or \( B \).
  - **Intersection**: \( A \cap B \) - the set of elements common to both \( A \) and \( B \).
  - **Difference**: \( A - B \) - the set of elements in \( A \) but not in \( B \).
  - **Cartesian Product**: \( A \times B = \{(a, b) | a \in A, b \in B\} \).
  - **Power Set**: \( P(A) = \{X | X \subseteq A\} \).
  
- **Truth Set**: \( T = \{x \in D | P(x) \text{ is true}\} \).

- **Subset Notation**: 
  - \( A \subseteq B \): \( A \) is a subset of \( B \).
  - \( A \subset B \): \( A \) is a proper subset of \( B \).

- **Cardinality**: \( |A| \) - the number of distinct elements in set \( A \).

## Detailed Technical Breakdown

### Set Operations
- **Union**: 
  - \( A \cup B = \{x | x \in A \text{ or } x \in B\} \)
  
- **Intersection**: 
  - \( A \cap B = \{x | x \in A \text{ and } x \in B\} \)

- **Difference**: 
  - \( A - B = \{x | x \in A \text{ and } x \notin B\} \)

- **Cartesian Product**: 
  - \( A \times B = \{(a, b) | a \in A, b \in B\} \)

- **Power Set**: 
  - \( P(A) = \{X | X \subseteq A\} \)

### Logical Statements
- **Truth Set**: 
  - Defined as \( T = \{x | P(x) \text{ is true}\} \).
  
- **Logical Implications**:
  - \( P \Rightarrow Q \): If \( P \) is true, then \( Q \) must also be true.

### Example Problems
1. **Determine Truth Values**:
   - Given \( H \in \{H\} \), evaluate the truth of various statements.
   - Example: \( H \in \{H, H\} \) is true.

2. **Set Equality**:
   - Let \( B = \{n \in \mathbb{Z} : n = 3j + 2, j \in \mathbb{Z}\} \) and \( D = \{n \in \mathbb{Z} : n = 3j - 1, j \in \mathbb{Z}\} \). Prove \( B = D \).

3. **Cardinality**:
   - Find \( |A| \) if \( A = \{1, 2, 2, 4, 5, 5, 5\} \). 
   - Answer: \( |A| = 5 \).

4. **Associative Laws**:
   - Investigate whether \( (A - B) - C = A - (B - C) \) holds true.

> [!important] **Note**: The associative law does not hold for set difference.

## Implementation/Examples
```markdown
Let A = {a, b, c}, B = {b, c, d}, C = {b, c, e}.
Calculate:
- (A - B) - C
- A - (B - C)
```

## Related
- [[Logic - Propositional Logic]]
- [[Sets and Functions]]
- [[CS1231_TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]