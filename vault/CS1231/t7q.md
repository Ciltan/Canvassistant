---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 7: Number Representations and Cryptography

## Overview
This tutorial focuses on various number representations, including binary, decimal, and hexadecimal systems, as well as concepts related to the [[Cantor expansion]]. Additionally, it explores properties of prime numbers and their implications in number theory, alongside practical applications in the [[RSA cryptosystem]]. The exercises aim to enhance understanding of modular arithmetic and the greatest common divisor (gcd).

## Key Concepts & Definitions
- **Binary Expansion**: The representation of a number in base 2.
- **Decimal Representation**: The standard base 10 representation of numbers.
- **Hexadecimal Representation**: A base 16 number system using digits 0-9 and letters A-F.
- **Cantor Expansion**: A unique representation of integers as a sum of factorials.
- **Modular Arithmetic**: A system of arithmetic for integers, where numbers wrap around after reaching a certain value (the modulus).
- **Greatest Common Divisor (gcd)**: The largest positive integer that divides two or more integers without leaving a remainder.
- **RSA Cryptosystem**: A public-key cryptographic system that uses the mathematical properties of prime numbers.

## Detailed Technical Breakdown

### 1. Number Representations
- **Binary Expansion of 321**: 
  - Convert 321 to binary.
  
- **Decimal Representation of (101011111)**:
  - Convert binary to decimal.

- **Hexadecimal Representation of 175627**:
  - Convert decimal to hexadecimal.

- **Hexadecimal to Binary Conversions**:
  - (a) Convert (80E)₁₆ to binary.
  - (b) Convert (135AB)₁₆ to binary.

### 2. Cantor Expansion
- **Definition**: A sum of the form \( a_n n! + a_{n-1} (n-1)! + \ldots + a_2 2! + a_1 1! \) where \( 0 \leq a_i \leq i \).
- **Find Cantor Expansions**:
  - (a) For the integer 2.
  - (b) For the integer 7.

### 3. Prime Number Properties
- **Theorem**: If \( 2^n - 1 \) is prime, then \( n \) is prime.
  - **Hint**: Use the identity \( 2^{ab} - 1 = (2^a - 1) \cdot 2^{a(b-1)} + 2^{a(b-2)} + \ldots + 2^a + 1 \).

### 4. Divisibility
- **Prove**: The product of any three consecutive integers is divisible by 6.

### 5. Modular Exponentiation
- **Find**: \( 11644 \mod 645 \).

### 6. GCD Calculation
- **Find**: \( \text{gcd}(14039, 1529) = d \) and integers \( s, t \) such that \( d = 14039s + 1529t \).

### 7. Inverses in Modular Arithmetic
- **Find the inverse of \( a \mod m \)** for the following pairs:
  - (i) (2, 6)
  - (ii) (3, 7)
  - (iii) (13, 33)

### 8. RSA Cryptosystem
- **Parameters**: Let \( p = 29 \), \( q = 53 \), \( n = pq = 1537 \), and \( e = 47 \).
  - (i) Encrypt the message "HELP" using \( 01 \) for A, \( 02 \) for B, etc.
  - (ii) Decrypt the message obtained in (i).

### 9. GCD Representation
- **Prove**: For positive integers \( a \) and \( b \), the smallest positive integer \( d \) that can be expressed as \( as + bt \) (where \( s, t \in \mathbb{Z} \)) is \( d = \text{gcd}(a, b) \).

> [!important] Remember to practice conversions between different number systems as they are foundational in computer science and cryptography.
> 
> [!note] Understanding the properties of prime numbers is crucial for grasping concepts in number theory and cryptography.

## Related
- [[Logic - Propositional Logic]]
- [[RSA Cryptosystem]]
- [[Modular Arithmetic]]
- [[Greatest Common Divisor]]
- [[Cantor Expansion]]