---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 6

## Overview
This tutorial focuses on various mathematical proofs and problems related to integers, divisibility, and modular arithmetic. Key concepts include proving properties of odd integers, exploring quotient and remainder, and establishing relationships between divisors. The tutorial also addresses prime factorization and the characteristics of perfect squares.

## Key Concepts & Definitions
- **Odd Integer**: An integer of the form \( n = 2k + 1 \) for some integer \( k \).
- **Divisibility**: An integer \( a \) divides \( b \) (denoted \( a | b \)) if there exists an integer \( k \) such that \( b = ak \).
- **Modular Arithmetic**: A system of arithmetic for integers, where numbers "wrap around" upon reaching a certain value (the modulus).
- **Perfect Square**: An integer \( n \) is a perfect square if there exists an integer \( k \) such that \( n = k^2 \).
- **Prime Factorization**: Expressing a number as the product of its prime factors.

## Detailed Technical Breakdown

### 1. Proving Properties of Odd Integers
- Prove that for any odd integer \( n \):
  \[
  \frac{\lfloor n^2 \rfloor}{4} = \frac{n^2 - 1}{4} = \frac{\lceil n^2 \rceil}{4}
  \]

### 2. Quotient and Remainder
- Find the quotient and remainder for the following pairs:
  - (a) \( (44, 8) \)
  - (b) \( (777, 21) \)
  - (c) \( (-123, 19) \)
  - (d) \( (0, 17) \)
  - (e) \( (-100, 101) \)

### 3. Divisibility Implications
- Show that if \( a, b, c \) are integers with \( a \neq 0 \) and \( c \neq 0 \), and \( ac | bc \), then \( a | b \).

### 4. Equality of Divisors
- Prove that if \( a | b \) and \( b | a \), then \( a = b \) or \( a = -b \).

### 5. Odd and Even Divisibility
- Prove that if \( a \) divides \( b \), then \( a \) is odd or \( b \) is even.

### 6. Modular Equations
- Find the integer \( a \) for the following conditions:
  - (a) \( a \equiv -15 \mod 27 \) and \( -26 \leq a \leq 0 \).
  - (b) \( a \equiv 24 \mod 31 \) and \( -15 \leq a \leq 15 \).
  - (c) \( a \equiv 99 \mod 41 \) and \( 100 \leq a \leq 140 \).

### 7. Divisor Properties in Modular Arithmetic
- Prove that if \( d \) is a positive divisor of \( a, b \) and \( m \), and \( a \equiv b \mod m \), then \( \frac{a}{d} \equiv \frac{b}{d} \mod \frac{m}{d} \).

### 8. Counterexamples
- Find counterexamples for:
  - (a) If \( ac \equiv bc \mod m \), then \( a \equiv b \mod m \).
  - (b) If \( a \equiv b \mod m \) and \( c \equiv d \mod m \), then \( ac \equiv bd \mod m \).

### 9. Primality Check
- Determine whether \( 107 \) and \( 113 \) are primes.

### 10. Prime Factorization
- Find the prime factorization of \( 909,090 \).

### 11. Composite Numbers
- Show that \( a^m + 1 \) is composite if \( a \) and \( m \) are integers greater than 1 and \( m \) is odd. 
  > [!hint] Show that \( x + 1 \) is a factor of the polynomial \( x^m + 1 \) if \( m \) is odd.

### 12. Perfect Squares
- Prove that a positive integer is a perfect square if and only if it has an odd number of positive divisors.
  > [!important] Hint: Every divisor greater than \( n \) can be paired with a divisor less than \( n \).

## Implementation/Examples
```python
# Example of finding quotient and remainder
def quotient_remainder(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

# Example usage
print(quotient_remainder(44, 8))  # Output: (5, 4)
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Logic - Propositional Logic]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]