---
tags: [CS1231, lecture-notes, academic]
---

# CS1231 Tutorial 3: Logical Reasoning and Argument Forms

## Overview
This tutorial focuses on the application of [[Logic - Propositional Logic]] to evaluate the validity of various argument forms. It includes exercises on truth tables, valid argument derivations, and logical proofs involving knights and knaves. The tutorial emphasizes critical thinking and the use of formal logic to derive conclusions from given premises.

## Key Concepts & Definitions
- **Truth Table**: A mathematical table used to determine the truth values of logical expressions based on their variables.
- **Valid Argument**: An argument where if the premises are true, the conclusion must also be true.
- **Converse Error**: A logical fallacy that occurs when the converse of a true statement is assumed to be true.
- **Inverse Error**: A logical fallacy that occurs when the inverse of a true statement is assumed to be true.
- **Knights and Knaves**: A classic logic puzzle involving two types of inhabitants: knights who always tell the truth and knaves who always lie.

## Detailed Technical Breakdown

### 1. Truth Table Validity
- **Arguments to Evaluate**:
  - (a) \( p \rightarrow r \)
  - (b) \( p \rightarrow q \lor r \)
  - (c) \( p \lor q \)
  - Premises: 
    - \( q \rightarrow r \)
    - \( \neg q \lor \neg r \)
  - Conclusions:
    - \( \therefore p \lor q \rightarrow r \)
    - \( \therefore \neg p \lor \neg r \)
    - \( q \rightarrow s \)
    - \( \therefore r \lor s \)

### 2. Deriving Conclusions
- **Premises**:
  - \( \neg p \lor q \rightarrow r \)
  - \( s \lor \neg q \)
  - \( \neg t \)
  - \( p \rightarrow t \)
  - \( \neg p \land r \rightarrow \neg s \)
- **Goal**: Derive \( \neg q \).

### 3. Logical Form and Inference
- **Arguments**:
  - (a) Sandra knows Java and C++.
    - Conclusion: Sandra knows C++.
    - **Inference**: Valid (Conjunction Introduction).
  - (b) If at least one number is divisible by 6, then their product is divisible by 6.
    - Conclusion: Product is not divisible by 6.
    - **Inference**: Converse Error.
  - (c) If rational numbers equal irrational numbers, then irrationals are infinite.
    - Conclusion: Rational numbers equal irrationals.
    - **Inference**: Valid (Affirming the Consequent).
  - (d) If I get a bonus, I buy a stereo.
    - Conclusion: If I get a bonus or sell my motorcycle, I buy a stereo.
    - **Inference**: Valid (Disjunction Introduction).

### 4. Chat Room Logic
- **Information**:
  - At least one of Kevin and Heather is chatting.
  - Exactly one of Randy and Vijay is chatting.
  - If Abby is chatting, then so is Randy.
  - Vijay and Kevin are either both chatting or both not chatting.
  - If Heather is chatting, then so are Abby and Kevin.
- **Analysis**: Use logical deductions to determine who is chatting.

### 5. Proving Superman's Non-Existence
- **Hypotheses**:
  1. If Superman is able and willing to prevent evil, he would do so.
  2. If Superman is unable to prevent evil, he is impotent.
  3. If Superman is unwilling to prevent evil, he is malevolent.
  4. Superman does not prevent evil.
  5. If Superman exists, he is neither impotent nor malevolent.
- **Proof Structure**: Use logical deductions to conclude that Superman does not exist.

### 6. Knights and Knaves
- **Part (a)**:
  - **Proof by Contradiction**:
    1. Assume A is a knight.
    2. A's statement implies B is a knight.
    3. B's statement implies A is a knave.
    4. Contradiction arises.
    5. Conclusion: A is a knave, B is a knight.
- **Part (b)**:
  - Analyze statements of C and D similarly to determine their identities.

### 7. Odd Integers
- **Proposition**: The product of any two odd integers is odd.
- **Proof**:
  - Let \( a = 2k + 1 \) and \( b = 2m + 1 \).
  - Then \( ab = (2k + 1)(2m + 1) = 4km + 2k + 2m + 1 = 2(2km + k + m) + 1 \).
  - Conclusion: \( ab \) is odd.

### 8. Smart's Proof Analysis
- **Comment**: Identify flaws in Smart's proof and provide a correct proof using contraposition.

## Implementation/Examples
```plaintext
# Example of a Truth Table for p → r
| p | q | r | p → r |
|---|---|---|-------|
| T | T | T |   T   |
| T | T | F |   F   |
| T | F | T |   T   |
| T | F | F |   F   |
| F | T | T |   T   |
| F | T | F |   T   |
| F | F | T |   T   |
| F | F | F |   T   |
```

> [!note] **Important**: Always check for logical fallacies when constructing arguments. Validity does not imply truth.
> [!warning] **Caution**: Misinterpretation of premises can lead to incorrect conclusions. Always clarify definitions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[CS1231+TUTORIAL+3]]
- [[Midterm+Briefing]]