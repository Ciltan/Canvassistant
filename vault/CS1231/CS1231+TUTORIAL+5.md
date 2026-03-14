---
tags: [CS1231, lecture-notes, academic]
---

# CS1231: Discrete Structures - Tutorial 5

## Overview
This tutorial focuses on the fundamental concepts of functions in discrete mathematics, including definitions of injective, surjective, and bijective functions. It also explores the determination of domains and ranges for various functions, alongside practical examples to illustrate these concepts. The tutorial aims to solidify understanding of function properties and their implications in mathematical contexts.

## Key Concepts & Definitions
- A function **f** from set **A** to set **B** is an assignment of exactly one element of **B** to each element of **A**.
- **Domain**: The set **A** from which elements are taken.
- **Codomain**: The set **B** to which elements are assigned.
- **Range**: The set of images of elements from the domain, denoted as **f(A)**.
- **Injective (One-to-One)**: A function **f: X → Y** is injective if for all **a, b ∈ X**, if **f(a) = f(b)** then **a = b**.
- **Surjective (Onto)**: A function **f: X → Y** is surjective if for every **y ∈ Y**, there exists at least one **x ∈ X** such that **f(x) = y**.
- **Bijection**: A function that is both injective and surjective.
- **Piecewise Functions**: Defined by different expressions based on the input value.

## Detailed Technical Breakdown

### Function Properties
- **Injective Function**: 
  - Example: **f(n) = n + 1** is injective because each input maps to a unique output.
  
- **Surjective Function**: 
  - Example: **f(n) = n^2** is not surjective when mapping from integers to reals, as negative outputs are not possible.

- **Bijection**: 
  - Example: **f(n) = n** is a bijection from integers to integers.

### Domain and Range Determination
| Function Definition | Domain | Range |
|---------------------|--------|-------|
| (a) f(n) = last digit of n | {n ∈ Z | n ≥ 0} | {0, 1, ..., 9} |
| (b) f(n) = n + 1 | {n ∈ Z | n > 0} | {2, 3, ...} |
| (c) f(bit string) = number of 1s | Set of all bit strings | {0, 1, ..., length of string} |
| (d) f(bit string) = total bits | Set of all bit strings | {0, 1, ..., length of string} |

### Function Evaluation Examples
- For the function **f: Z → R**:
  - (a) **f(n) = ±n**: Not a function (not unique).
  - (b) **f(n) = n^2 + 1**: Valid function (unique image).
  - (c) **f(n) = 1/(n^2 - 4)**: Not valid for n = ±2 (no image).
  - (d) **f(n) = sin(n)**: Valid function (unique image).

> [!note] **Important**: Always check the uniqueness of images when determining if a relation is a function.

## Implementation/Examples
```python
def is_injective(f):
    seen = set()
    for x in f:
        if f[x] in seen:
            return False
        seen.add(f[x])
    return True

def is_surjective(f, codomain):
    return all(y in f.values() for y in codomain)

def is_bijection(f, codomain):
    return is_injective(f) and is_surjective(f, codomain)
```

> [!warning] **Caution**: When defining functions, ensure that the domain and codomain are clearly specified to avoid ambiguity.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]