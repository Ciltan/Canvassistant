---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 3: The Integers

## Overview
This chapter delves into the fundamental concepts of integers, focusing on divisibility, prime numbers, and the properties of integers. It introduces key definitions and theorems that form the basis for understanding integer arithmetic and modular arithmetic. The chapter also discusses algorithms for identifying prime numbers and the significance of prime factorization.

## Key Concepts & Definitions
- **Divisibility**: An integer \( d \) divides another integer \( n \) if there exists an integer \( k \) such that \( n = dk \). This can also be expressed as \( d \mid n \) or \( d \nmid n \) if \( d \) does not divide \( n \).
- **Prime Number**: A positive integer greater than 1 that has exactly two positive divisors: 1 and itself.
- **Composite Number**: A positive integer greater than 1 that has more than two positive divisors.
- **Modular Arithmetic**: If \( a, b \in \mathbb{Z} \) and \( m \in \mathbb{Z}^+ \), then \( a \) is congruent to \( b \) modulo \( m \) if \( m \) divides \( (a - b) \), denoted as \( a \equiv b \mod m \).

## Detailed Technical Breakdown

### 3.1 Divisibility
- **Definitions**:
  - \( d \mid n \) if \( n = dk \) for some \( k \in \mathbb{Z} \).
  - Other expressions: \( n \) is divisible by \( d \), \( n \) is a multiple of \( d \), \( d \) is a factor of \( n \), or \( d \) is a divisor of \( n \).
  
- **Notation**:
  - \( d \mid n \) indicates \( d \) divides \( n \).
  - \( d \nmid n \) indicates \( d \) does not divide \( n \).

- **Examples**:
  - \( 2 \mid 4 \) (2 divides 4)
  - \( 3 \nmid 10 \) (3 does not divide 10)

### 3.2 Prime Numbers and GCD
- **Sieve of Eratosthenes**:
  - An algorithm to find all primes less than a given number \( n \).
  - Steps include marking multiples of each prime starting from 2.

- **Theorems**:
  - Every positive integer \( n > 1 \) has at least one prime divisor.
  - **Prime Factorization Theorem**: Every positive integer greater than 1 can be uniquely expressed as a product of primes.

### 3.3 Modular Arithmetic
- **Theorems**:
  - \( a \equiv b \mod m \) if and only if \( a \mod m = b \mod m \).
  - If \( a \equiv b \mod m \) and \( c \equiv d \mod m \), then \( a + c \equiv b + d \mod m \) and \( ac \equiv bd \mod m \).

## Implementation/Examples
```python
# Example of finding the quotient and remainder
def division_algorithm(n, d):
    q = n // d  # Quotient
    r = n % d   # Remainder
    return q, r

# Example usage
print(division_algorithm(11, 5))  # Output: (2, 1)
```

> [!note] **Important Note**: The remainder \( r \) in the division algorithm is always non-negative and less than \( d \).

> [!warning] **Caution**: Ensure that \( d \) is not zero when applying the division algorithm, as division by zero is undefined.

## Related
- See [[Logic - Propositional Logic]] for foundational logic concepts.
- Refer to [[Chapter+2]] for additional context on integers and their properties.
- Explore [[AY2122+Sem1+Homework+3]] for practical applications of these concepts.