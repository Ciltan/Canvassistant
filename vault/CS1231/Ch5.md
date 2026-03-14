---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 5: Counting

## Overview
This chapter delves into the fundamental principles of counting, including the Product Rule, Sum Rule, and Inclusion/Exclusion Principle. It provides a structured approach to calculating the number of ways to arrange or select items from sets, which is essential in combinatorial mathematics. Through various examples, the chapter illustrates how these rules can be applied to solve practical problems in counting.

## Key Concepts & Definitions
- **Product Rule**: If an operation can be broken down into a sequence of steps, the total number of ways to perform the operation is the product of the number of ways to perform each step.
- **Sum Rule**: If there are two properties with no overlap, the total number of objects is the sum of the objects with each property.
- **Difference Rule**: The number of objects with one property but not another can be found by subtracting the number of objects with both properties from the total with the first property.
- **Inclusion/Exclusion Principle**: A method for counting the number of elements in the union of multiple sets by accounting for overlaps.

## Detailed Technical Breakdown

### 5.1 Basics

#### Product Rule
- If the first step can be done in \( r \) ways and the second step in \( s \) ways, then the total number of ways to perform the operation is \( rs \).
  
**Example**: 
- Labeling auditorium chairs with letters (26 ways) and numbers (100 ways): 
  - Total = \( 26 \times 100 = 2600 \).

#### Sum Rule
- If there are \( m \) objects with property 1 and \( n \) objects with property 2, and no overlap, the total is \( m + n \).

**Example**: 
- Counting n-letter passwords:
  - For \( n = 1 \): 26 passwords
  - For \( n = 2 \): \( 26^2 = 676 \)
  - For \( n = 3 \): \( 26^3 = 17576 \)
  - Total = \( 26 + 676 + 17576 = 18278 \).

#### Difference Rule
- The number of objects with property 1 but not property 2 is \( m - n \).

**Example**: 
- Counting integers from 100 to 999 divisible by 5:
  - Total multiples in [1, 999]: \( \lfloor 999/5 \rfloor = 199 \)
  - Total multiples in [1, 99]: \( \lfloor 99/5 \rfloor = 19 \)
  - Result = \( 199 - 19 = 180 \).

### 5.2 Inclusion/Exclusion Principle
- For two sets \( A \) and \( B \):
  - \( |A \cup B| = |A| + |B| - |A \cap B| \).
  
**Example**: 
- Counting integers from 1 to 1000 that are multiples of 3 or 5:
  - \( |A_3| = 333 \), \( |A_5| = 200 \), \( |A_{15}| = 66 \)
  - Total = \( 333 + 200 - 66 = 467 \).

## Implementation/Examples

```markdown
### Example: Counting Bit Strings
- How many bit strings of length 8 either start with a 1 or end with two 0?
  - Let \( A \) be the set of strings starting with 1, \( B \) be those ending with 00.
  - \( |A| = 2^7 = 128 \), \( |B| = 2^6 = 64 \), \( |A \cap B| = 2^5 = 32 \).
  - Total = \( |A| + |B| - |A \cap B| = 128 + 64 - 32 = 160 \).
```

> [!note] The Product Rule is foundational in combinatorial counting and is widely applicable in various fields, including computer science and operations research.
> 
> [!important] Understanding the Inclusion/Exclusion Principle is crucial for accurately counting elements in overlapping sets, preventing over-counting.

## Related
- [[Logic - Propositional Logic]]
- [[Stacks and Queues]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]