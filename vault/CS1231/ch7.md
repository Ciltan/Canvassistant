---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 7: Trees

## Overview
This chapter introduces the concept of trees in graph theory, defining them as connected, undirected graphs without cycles. It explores the properties of trees, including rooted trees and their terminology, and presents key theorems related to tree structures. The chapter also discusses the significance of trees in various applications, such as organizational structures and molecular models.

## Key Concepts & Definitions
- **Tree**: A connected (undirected) graph with no cycles. 
- **Forest**: A graph where all connected components are trees.
- **Rooted Tree**: A tree with one designated vertex as the root, with edges directed away from it.
- **Parent**: In a rooted tree, the vertex connected to a child vertex.
- **Child**: A vertex connected to a parent vertex.
- **Sibling**: Vertices that share the same parent.
- **Ancestor**: A vertex that is on the path from the root to a given vertex.
- **Descendant**: A vertex that can be reached from a given vertex by following edges downward.
- **Leaf**: A vertex with no children.
- **Internal Vertex**: A vertex that has at least one child.
- **m-ary Tree**: A tree where each internal vertex has at most m children.
- **Full m-ary Tree**: An m-ary tree where every internal vertex has exactly m children.
- **Binary Tree**: A tree where each internal vertex has at most two children.

## Detailed Technical Breakdown

### Definitions and Properties
- A **tree** cannot contain loops or multiple edges, as these would create cycles.
- A **forest** is defined as a collection of trees.
- The unique path property of trees states that there is a unique simple path between any two vertices.

### Theorems
1. **Unique Path Theorem**: A graph is a tree if and only if there is a unique simple path between any two vertices.
2. **Degree Theorem**: A tree with \( n \geq 2 \) vertices has at least two vertices of degree 1.
3. **Vertex Removal Theorem**: If \( v \) is a vertex of degree 1 in a tree \( T \) with \( n \geq 2 \) vertices, then \( T - v \) is also a tree.
4. **Edge Count Theorem**: A tree with \( n \) vertices has \( n - 1 \) edges.
5. **Full m-ary Tree Theorem**: A full m-ary tree with \( i \) internal vertices contains \( n = mi + 1 \) vertices.

### Terminology
- **Subtree**: The subgraph consisting of a vertex and all its descendants.
- **Ordered Rooted Tree**: A rooted tree where the children of each vertex are ordered from left to right.

## Implementation/Examples
```plaintext
Example of a Rooted Tree:
        a
       / \
      b   c
     / \   \
    d   e   f
```

> [!note] **Applications of Trees**: Trees are utilized in various fields, including computer science for file systems, biology for phylogenetic trees, and organizational structures in businesses.

> [!important] **Key Properties**: Remember that every tree with \( n \) vertices has \( n - 1 \) edges, and a tree must be connected and acyclic.

## Related
- [[Logic - Propositional Logic]]
- [[Stacks and Queues]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]