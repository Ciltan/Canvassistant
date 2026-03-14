---
tags: [MA1508E, linear_systems, gaussian_elimination, row_reduction]
---

# Systems of Linear Equations

## Overview

A system of linear equations is a collection of one or more linear equations involving the same variables. This chapter introduces the fundamental techniques for solving such systems, including Gaussian elimination and the concept of row echelon form, which underpin much of linear algebra.

## Linear Equations and Systems

> [!note] Definition: Linear Equation
> A **linear equation** in variables $x_1, x_2, \ldots, x_n$ is an equation of the form
> $$a_1 x_1 + a_2 x_2 + \cdots + a_n x_n = b$$
> where $a_1, a_2, \ldots, a_n$ and $b$ are real constants.

A **system of linear equations** (or **linear system**) is a collection of one or more linear equations involving the same variables:

$$\begin{cases} a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\ a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\ \vdots \\ a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m \end{cases}$$

A **solution** is an ordered $n$-tuple $(s_1, s_2, \ldots, s_n)$ that satisfies every equation simultaneously.

> [!important] Fundamental Theorem
> A system of linear equations has either:
> 1. **No solution** (inconsistent),
> 2. **Exactly one solution** (unique), or
> 3. **Infinitely many solutions**.
> There is no other possibility.

## Augmented Matrix and Elementary Row Operations

The system above can be represented compactly as an **augmented matrix**:

$$\left[\begin{array}{cccc|c} a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\ a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} & b_m \end{array}\right]$$

> [!note] Definition: Elementary Row Operations
> The three **elementary row operations** are:
> 1. **Row interchange**: Swap two rows ($R_i \leftrightarrow R_j$)
> 2. **Row scaling**: Multiply a row by a nonzero scalar ($kR_i \to R_i$, $k \neq 0$)
> 3. **Row replacement**: Add a multiple of one row to another ($R_i + kR_j \to R_i$)

Two matrices are **row equivalent** if one can be obtained from the other by a sequence of elementary row operations. Row equivalent augmented matrices represent systems with the same solution set.

## Row Echelon Form and Reduced Row Echelon Form

> [!note] Definition: Row Echelon Form (REF)
> A matrix is in **row echelon form** if:
> 1. All rows consisting entirely of zeros are at the bottom.
> 2. The first nonzero entry (called the **leading entry** or **pivot**) of each nonzero row is to the right of the leading entry of the row above it.
> 3. All entries in the column below a pivot are zero.

> [!note] Definition: Reduced Row Echelon Form (RREF)
> A matrix is in **reduced row echelon form** if it is in REF and additionally:
> 4. Each pivot is equal to 1.
> 5. Each pivot is the only nonzero entry in its column.

> [!important] Uniqueness of RREF
> Every matrix is row equivalent to one and only one matrix in reduced row echelon form.

## Gaussian Elimination

**Gaussian elimination** is the process of using elementary row operations to transform an augmented matrix into row echelon form. **Gauss-Jordan elimination** continues to reduced row echelon form.

### Algorithm

1. Start with the leftmost nonzero column (pivot column).
2. Select a nonzero entry in the pivot column as the pivot. If necessary, swap rows to move it to the top.
3. Use row replacement to create zeros below the pivot.
4. Cover the row containing the pivot and repeat steps 1-3 on the remaining submatrix.
5. (For RREF) Working from right to left, use row replacement to create zeros above each pivot, then scale each pivot to 1.

### Worked Example

Solve the system:
$$\begin{cases} x_1 + 2x_2 + x_3 = 3 \\ 2x_1 + 5x_2 + 2x_3 = 7 \\ x_1 + 3x_2 + 3x_3 = 5 \end{cases}$$

**Step 1**: Write the augmented matrix:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 2 & 5 & 2 & 7 \\ 1 & 3 & 3 & 5 \end{array}\right]$$

**Step 2**: $R_2 - 2R_1 \to R_2$ and $R_3 - R_1 \to R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 0 & 1 \\ 0 & 1 & 2 & 2 \end{array}\right]$$

**Step 3**: $R_3 - R_2 \to R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 2 & 1 \end{array}\right]$$

**Step 4**: $\frac{1}{2}R_3 \to R_3$:
$$\left[\begin{array}{ccc|c} 1 & 2 & 1 & 3 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & \frac{1}{2} \end{array}\right]$$

**Step 5** (back substitution to RREF): $R_1 - R_3 \to R_1$, then $R_1 - 2R_2 \to R_1$:
$$\left[\begin{array}{ccc|c} 1 & 0 & 0 & \frac{1}{2} \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & \frac{1}{2} \end{array}\right]$$

**Solution**: $x_1 = \frac{1}{2}$, $x_2 = 1$, $x_3 = \frac{1}{2}$.

## Pivot Positions and Free Variables

> [!note] Definition: Pivot Position and Pivot Column
> A **pivot position** is a location in the matrix that corresponds to a leading 1 in the RREF. A **pivot column** is a column that contains a pivot position.

Variables corresponding to pivot columns are called **basic variables** (or **leading variables**). Variables corresponding to non-pivot columns are called **free variables**.

> [!important] Existence and Uniqueness of Solutions
> For a linear system with augmented matrix $[A \mid \mathbf{b}]$:
> - The system is **consistent** if and only if the rightmost column of $[A \mid \mathbf{b}]$ is **not** a pivot column (i.e., no row of the form $[0 \ 0 \ \cdots \ 0 \mid c]$ with $c \neq 0$).
> - If consistent, the solution is **unique** if and only if there are **no free variables**.
> - If consistent with free variables, there are **infinitely many solutions** parameterised by the free variables.

### Example with Infinitely Many Solutions

$$\left[\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 0 & 1 & 2 \end{array}\right]$$

Here $x_2$ is a free variable. Setting $x_2 = t$ (parameter):
$$x_1 = 3 - 2t + 1 = 5 - 2t, \quad x_2 = t, \quad x_3 = 2$$

The general solution in parametric vector form:
$$\mathbf{x} = \begin{pmatrix} 5 \\ 0 \\ 2 \end{pmatrix} + t\begin{pmatrix} -2 \\ 1 \\ 0 \end{pmatrix}, \quad t \in \mathbb{R}$$

## Homogeneous Systems

A system is **homogeneous** if all the constants $b_i = 0$:
$$A\mathbf{x} = \mathbf{0}$$

> [!important] Key Property
> A homogeneous system is always consistent (the **trivial solution** $\mathbf{x} = \mathbf{0}$ always satisfies it). It has a nontrivial solution if and only if the system has at least one free variable, which occurs whenever the number of variables exceeds the number of pivot positions.

> [!warning] Common Exam Mistake
> A homogeneous system with more unknowns than equations ($n > m$) always has infinitely many (nontrivial) solutions. This follows because there must be at least $n - m > 0$ free variables.

## Applications

- **Network flow analysis**: Balancing flows through nodes.
- **Chemical equation balancing**: Each element gives a linear equation.
- **Circuit analysis**: Kirchhoff's laws produce linear systems.
- **Curve fitting**: Determining polynomial coefficients from data points.

## Related Notes

- [[Matrices]] - Matrix algebra and the equation $A\mathbf{x} = \mathbf{b}$
- [[Determinants]] - Using determinants to test invertibility and solve systems via Cramer's rule
- [[Vector Spaces]] - Solution sets as subspaces
