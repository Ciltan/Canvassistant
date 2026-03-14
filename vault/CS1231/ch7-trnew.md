---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 7: Trees

## Overview
This chapter introduces the concept of trees in graph theory, defining them as connected, undirected graphs without cycles. It explores the properties of trees, including their unique paths between vertices and the structure of rooted trees. The chapter also discusses related concepts such as forests and m-ary trees, providing a foundation for understanding more complex data structures.

## Key Concepts & Definitions
- **Tree**: A connected (undirected) graph with no cycles. 
- **Forest**: A graph where all connected components are trees.
- **Rooted Tree**: A tree with one designated vertex as the root, with edges directed away from it.
- **Parent**: In a rooted tree, if an edge connects vertices u and v, then u is the parent of v.
- **Child**: A vertex that is connected to another vertex (its parent) by an edge.
- **Sibling**: Vertices that share the same parent.
- **Ancestor/Descendant**: If there is a simple path from vertex u to vertex v, then u is an ancestor of v, and v is a descendant of u.
- **Leaf**: A vertex with no children.
- **Internal Vertex**: A vertex that has at least one child.
- **Subtree**: The subgraph consisting of a vertex and all its descendants.
- **m-ary Tree**: A rooted tree where each internal vertex has at most m children.
- **Full m-ary Tree**: An m-ary tree where every internal vertex has exactly m children.
- **Binary Tree**: An m-ary tree where m = 2.

## Detailed Technical Breakdown

### Definitions and Properties
- **Tree Definition**: A tree is defined as a connected graph with no cycles. This means it cannot contain loops or multiple edges.
  
- **Forest Definition**: A forest is a collection of trees, meaning that each connected component of the graph is a tree.

### Theorems
- **Unique Path Theorem**: A graph is a tree if and only if there is a unique simple path between any two vertices. 
  - **Proof Outline**: 
    - If T is a tree, then every two vertices are connected by a path, which can be reduced to a simple path.
    - Conversely, if every two vertices are connected by a unique simple path, T must be connected and cannot contain cycles.

### Rooted Trees
- In a rooted tree, one vertex is designated as the root, and all edges are directed away from it. 
- Terminology related to rooted trees includes parent, child, siblings, ancestors, descendants, leaves, and internal vertices.

### Subtrees
- A subtree rooted at a vertex u consists of u and all its descendants.

### m-ary Trees
- An m-ary tree is defined by the number of children each internal vertex can have. 
- A full m-ary tree has all internal vertices with exactly m children, while a binary tree is a specific case where m = 2.

## Implementation/Examples
```plaintext
Example of a Tree:
    a
   / \
  b   c
 / \
d   e

Example of a Binary Tree:
    a
   / \
  b   c
 / \
d   e
```

> [!note] **Key Takeaway**: Trees are fundamental structures in computer science, used in various applications such as data organization, searching algorithms, and hierarchical data representation.

> [!important] **Important Concept**: Understanding the properties of trees, especially the unique path theorem, is crucial for grasping more complex data structures and algorithms.

## Related
- [[Logic - Propositional Logic]]
- [[Stacks and Queues]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]