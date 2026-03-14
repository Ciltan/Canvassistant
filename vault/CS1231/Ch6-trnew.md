---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 6: Graph Theory

## Overview
This chapter introduces the fundamental concepts of graph theory, focusing on the definitions and properties of graphs, including vertices, edges, loops, and multigraphs. It also explores directed graphs (digraphs) and their applications in modeling real-world scenarios such as acquaintance relationships and web structures. Understanding these concepts is essential for analyzing complex networks and their behaviors.

## Key Concepts & Definitions
- **Graph**: A graph G = (V, E) consists of:
  - **V**: A nonempty finite set of [[vertices]].
  - **E**: A set of [[edges]].
- **Edge**: An edge connects one or two vertices, referred to as its **endpoints**.
  - **Loop**: An edge with one endpoint, connecting a vertex to itself.
  - **Multiple Edges**: More than one edge connecting a pair of vertices.
- **Simple Graph**: A graph with no loops or multiple edges.
- **Multigraph**: A graph with no loops but allows multiple edges.
- **Digraph**: A directed graph where edges have a direction, represented as ordered pairs of vertices.

## Detailed Technical Breakdown

### Graph Structures
- **Vertices (V)**: Points in the graph representing entities.
- **Edges (E)**: Lines connecting vertices, which can be:
  - **Simple Edges**: Connect two distinct vertices.
  - **Loops**: Connect a vertex to itself.
  - **Multiple Edges**: Multiple connections between the same pair of vertices.

| Type of Edge      | Description                                   |
|-------------------|-----------------------------------------------|
| Simple Edge       | Connects two distinct vertices                |
| Loop              | Connects a vertex to itself                   |
| Multiple Edge     | More than one edge between two vertices       |

### Directed Graphs (Digraphs)
- **Definition**: A digraph G = (V, E) consists of:
  - **V**: A nonempty finite set of vertices.
  - **E**: A set of directed edges, represented as ordered pairs (u, v).

### Applications of Graphs
- **Acquaintanceship Graphs**: Vertices represent people; an edge indicates mutual acquaintance.
- **Influence Graphs**: Model influence dynamics where directed edges represent influence relationships.
- **Call Graphs**: Represent telephone calls in a network, with vertices as telephones and edges as calls.
- **Web Graphs**: Model the World Wide Web, where vertices are web pages and directed edges represent hyperlinks.
- **Precedence Graphs**: Used in computer programming to represent dependencies between statements.

## Implementation/Examples
```plaintext
# Example of a simple graph
Vertices: A, B, C
Edges: AB, AC, BC

# Example of a digraph
Vertices: 1, 2, 3
Edges: 12 (1 to 2), 23 (2 to 3), 31 (3 to 1)
```

> [!note] **Important Note**: In graph theory, the distinction between simple graphs and multigraphs is crucial for understanding the complexity of networks. Simple graphs are easier to analyze, while multigraphs can represent more intricate relationships.

> [!warning] **Caution**: When modeling real-world scenarios with graphs, ensure that the chosen graph type accurately reflects the relationships and dependencies present in the data.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[AY2122+Sem1+Homework+1(S)]]