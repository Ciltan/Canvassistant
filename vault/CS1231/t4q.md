---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 4

## Overview
This tutorial focuses on fundamental concepts in set theory, including membership, subsets, Cartesian products, and the properties of operations on sets. It presents a series of problems designed to test understanding of these concepts, along with proofs and counterexamples to reinforce learning. The tutorial emphasizes logical reasoning and the application of set operations in various contexts.

## Key Concepts & Definitions
- **Set**: A collection of distinct objects, considered as an object in its own right.
- **Membership**: The relation between an element and a set, denoted as \( x \in A \) if \( x \) is an element of set \( A \).
- **Subset**: A set \( A \) is a subset of set \( B \) if every element of \( A \) is also an element of \( B \), denoted \( A \subseteq B \).
- **Cartesian Product**: The Cartesian product of sets \( A \) and \( B \), denoted \( A \times B \), is the set of all ordered pairs \( (a, b) \) where \( a \in A \) and \( b \in B \).
- **Symmetric Difference**: The symmetric difference of sets \( A \) and \( B \), denoted \( A \oplus B \), is defined as \( (A - B) \cup (B - A) \).

## Detailed Technical Breakdown

### 1. True or False Statements
- (a) \( \emptyset \in \{ \emptyset \} \) 
- (b) \( \emptyset \in \{ \emptyset, \{ \emptyset \} \} \) 
- (c) \( \{ \emptyset \} \in \{ \emptyset \} \) 
- (d) \( \{ \emptyset \} \in \{ \{ \emptyset \} \} \) 
- (e) \( \{ \emptyset \} \subset \{ \emptyset, \{ \emptyset \} \} \) 
- (f) \( \{ \{ \emptyset \} \} \subset \{ \emptyset, \{ \emptyset \} \} \) 
- (g) \( \{ \{ \emptyset \} \} \subset \{ \{ \emptyset \}, \{ \emptyset \} \} \) 

### 2. Set Equality
Let \( B = \{ n \in \mathbb{Z} : n = 3j + 2, j \in \mathbb{Z} \} \) and \( D = \{ n \in \mathbb{Z} : n = 3j - 1, j \in \mathbb{Z} \} \). Determine if \( B = D \).

### 3. Cardinality
Find \( |A| \) if \( A = \{ 1, 2, \{ 2 \}, \{ 4, 5 \}, 5, 5 \} \).

### 4. Set Operations
Let \( A = \{ a, b, c \} \), \( B = \{ b, c, d \} \), \( C = \{ b, c, e \} \). Calculate:
- \( (A - B) - C \)
- \( A - (B - C) \)
Are they equal?

### 5. Truth Set of Predicate
Let \( T \) denote the truth set of the predicate \( P(x) \). Prove:
- (a) \( T = T \cup T \), \( T = T \cap T \)
- (b) \( T = T \cup T \)

### 6. Cartesian Products
Let \( A = \{ 1, 2, 3 \} \), \( B = \{ u, v \} \), \( C = \{ m, n \} \). List the elements of:
- \( (A \times B) \times C \)
- \( A \times B \times C \)
Are the two Cartesian products equal?

### 7. Proof Error
Identify the mistake in the proof of the theorem: For all sets \( A \) and \( B \), \( A \cup B \subseteq A \cup B \).

### 8. Set Intersection
Prove that \( (A - C) \cap (B - C) \cap (A - B) = \emptyset \).

### 9. Set Intersection and Cartesian Products
Prove that for all sets \( A, B, C, D \), if \( A \cap C = \emptyset \), then \( (A \times B) \cap (C \times D) = \emptyset \).

### 10. Prove or Counterexample
For each statement, either prove it true or find a counterexample:
- (a) If \( B \cap C \subseteq A \), then \( (A - B) \cap (A - C) = \emptyset \).
- (b) \( (A - B) \cap (C - B) = A - (B \cup C) \).
- (c) If \( A \subseteq B \), then \( A \cup B = U \).
- (d) \( P(A \cap B) = P(A) \cap P(B) \).

### 11. Set Equality Proof
Show that \( A \cap B \cap C = A \cup B \cup C \):
- (a) By showing that each side is a subset of the other side.
- (b) By using a membership table.

### 12. Symmetric Difference
Define the symmetric difference \( A \oplus B = (A - B) \cup (B - A) \):
- (a) Let \( A = \{ 1, 2, 3, 4 \} \), \( B = \{ 3, 4, 5, 6 \} \), \( C = \{ 5, 6, 7, 8 \} \). Find \( (A \oplus B) \oplus C \).
- (b) Prove that if \( A \oplus C = B \oplus C \), then \( A = B \).

> [!note] Remember to review the properties of sets and operations thoroughly, as they form the foundation for understanding more complex concepts in set theory.
> [!important] Pay special attention to proofs and counterexamples, as they are crucial for demonstrating your understanding of logical reasoning in mathematics.

## Related
- [[Logic - Propositional Logic]]
- [[CS1231 TUTORIAL 3]]
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem2+Homework+3(S)]]