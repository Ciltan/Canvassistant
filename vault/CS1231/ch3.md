---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 3: The Integers

## Overview
This chapter delves into the fundamental concepts of integers, focusing on divisibility, prime numbers, and the greatest common divisor (GCD). It introduces essential definitions and theorems, including the Division Algorithm and the Sieve of Eratosthenes, which are pivotal in number theory. The chapter also explores modular arithmetic and its applications, particularly in cryptology.

## Key Concepts & Definitions
- **Divisibility**: Let \( n, d \in \mathbb{Z} \) with \( d \neq 0 \). We say that \( d \) **divides** \( n \) (denoted \( d \mid n \)) if \( n = dk \) for some \( k \in \mathbb{Z} \). Other terms include:
  - \( n \) is **divisible** by \( d \)
  - \( n \) is a **multiple** of \( d \)
  - \( d \) is a **factor** of \( n \)
  - \( d \) is a **divisor** of \( n \)

- **Prime Number**: A positive integer greater than 1 that has exactly two positive divisors: 1 and itself.
- **Composite Number**: A positive integer that has more than two positive divisors.
- **Greatest Common Divisor (GCD)**: The largest integer \( d \) such that \( d \mid a \) and \( d \mid b \) for integers \( a \) and \( b \).

## Detailed Technical Breakdown

### Section 3.1: Divisibility
- **Definition**: \( d \mid n \) if \( n = dk \) for some \( k \in \mathbb{Z} \).
- **Properties**:
  - \( n \neq 0 \) implies \( n \mid 0 \).
  - If \( d \mid n \), then \( |d| \leq |n| \).
  
| Property | Description |
|----------|-------------|
| Transitive Property | If \( a \mid b \) and \( b \mid c \), then \( a \mid c \). |
| Division Algorithm | For \( n \in \mathbb{Z} \) and \( d \in \mathbb{Z}^+ \), there exist unique integers \( q \) and \( r \) such that \( n = dq + r \) with \( 0 \leq r < d \). |

### Section 3.2: Prime Numbers and GCD
- **Sieve of Eratosthenes**: An algorithm to find all primes less than a given number \( n \).
- **Theorem**: Every positive integer \( n > 1 \) has a prime divisor.
- **Prime Factorization Theorem**: Every positive integer greater than 1 can be uniquely expressed as a product of primes.

### Section 3.3: Algorithms
- **Base \( b \) Expansion**: Any integer \( n \) can be expressed uniquely in base \( b \).
- **Modular Exponentiation**: Efficiently computes \( b^n \mod m \) using the binary representation of \( n \).

### Section 3.4: Applications
- **Cryptology**: The GCD plays a crucial role in algorithms used for encryption and decryption.

## Implementation/Examples
```markdown
### Example: Division Algorithm
Let \( n = 7 \) and \( d = 3 \).
- Quotient \( q = 7 \text{ Div } 3 = 2 \)
- Remainder \( r = 7 \text{ Mod } 3 = 1 \)

### Example: Sieve of Eratosthenes
To find all primes less than 50:
1. Start with the list of numbers from 2 to 50.
2. Delete multiples of each prime starting from 2.
3. Remaining numbers are primes: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.
```

> [!note] **Important Note**: The GCD can be computed using the Euclidean Algorithm, which is efficient and straightforward.

> [!warning] **Caution**: The concept of prime factorization is crucial for understanding the structure of integers and their properties.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]