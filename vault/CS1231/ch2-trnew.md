---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 2: Sets and Functions

## Overview
This chapter introduces fundamental concepts in set theory, including definitions, operations, and properties of sets. It emphasizes the importance of understanding sets as collections of objects and explores various types of sets, such as finite, infinite, and power sets. Additionally, the chapter covers set operations like union, intersection, and difference, providing a foundation for further study in mathematical logic and functions.

## Key Concepts & Definitions
- **Set**: An unordered collection of objects, known as elements or members. 
- **Element Membership Notation**: 
  - \( x \in A \): object \( x \) is a member of set \( A \).
  - \( x \notin A \): object \( x \) is not a member of set \( A \).
- **Important Sets**:
  - \( \mathbb{R} \): set of real numbers.
  - \( \mathbb{Q} \): set of rational numbers.
  - \( \mathbb{Z} \): set of integers.
- **Subset**: Set \( A \) is a subset of set \( B \) if every element of \( A \) is also an element of \( B \) (denoted \( A \subseteq B \)).
- **Proper Subset**: Set \( A \) is a proper subset of set \( B \) if \( A \subseteq B \) and \( A \neq B \) (denoted \( A \subset B \)).
- **Universal Set**: The set that contains all objects under discussion, denoted by \( U \).
- **Empty Set**: The set with no members, denoted by \( \emptyset \).
- **Singleton Set**: A set with exactly one element.

## Detailed Technical Breakdown

### Set Definitions
- **Set Representation**:
  - A set can be described by listing its members: 
    - Example: \( D = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\} \)
  - A set can also be defined by its properties:
    - Example: The set of positive even numbers less than 100: 
      \[
      \{ x \in \mathbb{N} \mid x \in \mathbb{Z}, \frac{x}{2}, x < 100 \}
      \]

### Set Operations
- **Union**: The union of sets \( A \) and \( B \) is the set of elements that are in \( A \), \( B \), or both:
  \[
  A \cup B = \{ x \mid x \in A \lor x \in B \}
  \]
- **Intersection**: The intersection of sets \( A \) and \( B \) is the set of elements that are in both \( A \) and \( B \):
  \[
  A \cap B = \{ x \mid x \in A \land x \in B \}
  \]
- **Difference**: The difference of set \( B \) with respect to set \( A \) is the set of elements in \( B \) but not in \( A \):
  \[
  B - A = \{ x \mid x \in B \land x \notin A \}
  \]
- **Complement**: The complement of set \( A \) is the set of elements not in \( A \):
  \[
  A' = U - A
  \]

### Set Identities
- **Identity Laws**:
  - \( A \cup \emptyset = A \)
  - \( A \cap U = A \)
- **Domination Laws**:
  - \( A \cup U = U \)
  - \( A \cap \emptyset = \emptyset \)
- **Idempotent Laws**:
  - \( A \cup A = A \)
  - \( A \cap A = A \)

## Implementation/Examples
```markdown
### Example of Set Operations
Let \( A = \{1, 2, 3\} \) and \( B = \{2, 3, 4\} \).

- Union: 
  \[
  A \cup B = \{1, 2, 3, 4\}
  \]
- Intersection: 
  \[
  A \cap B = \{2, 3\}
  \]
- Difference: 
  \[
  A - B = \{1\}
  \]
```

> [!note] **Important Note**: The empty set is a subset of every set, including itself.
> [!warning] **Caution**: Be careful not to confuse the empty set \( \emptyset \) with a singleton set containing the empty set, \( \{\emptyset\} \).

## Related
- See also [[Logic - Propositional Logic]] for foundational concepts in logical reasoning.
- Refer to [[Chapter+2]] for additional context on sets and functions.
- Explore [[CS1231+TUTORIAL+3]] for practical applications of set theory in problem-solving.