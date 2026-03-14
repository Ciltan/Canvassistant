---
tags: [CS1231, lecture-notes, academic]
---

# Chapter 6: Graph Theory

## Overview
This chapter introduces the fundamental concepts of graph theory, defining key elements such as vertices, edges, loops, and multigraphs. It explores the visualization of graphs and the distinctions between simple graphs and multigraphs. Additionally, the chapter discusses directed graphs (digraphs) and their applications in modeling real-world scenarios, such as acquaintance relationships and web structures.

## Key Concepts & Definitions
- **Graph**: A graph \( G = (V, E) \) consists of:
  - \( V \): A nonempty finite set of [[vertices]].
  - \( E \): A set of [[edges]].
- **Edge**: An edge connects one or two vertices, referred to as its [[endpoints]].
  - **Loop**: An edge with one endpoint that connects a vertex to itself.
  - **Multiple Edges**: More than one edge connecting the same pair of vertices.
- **Simple Graph**: A graph with no loops or multiple edges.
- **Multigraph**: A graph that allows multiple edges but no loops.
- **Digraph**: A directed graph \( G = (V, E) \) where edges have a direction, represented as ordered pairs of vertices.

## Detailed Technical Breakdown

### Graph Representation
- **Vertices and Edges**:
  - Vertices are represented as points.
  - Edges are represented as line segments or curves connecting vertices.
  
| Type of Edge      | Description                                      |
|-------------------|--------------------------------------------------|
| Edge              | Connects two vertices \( a \) and \( b \)       |
| Loop              | Connects a vertex \( a \) to itself              |
| Multiple Edges    | More than one edge between the same vertices     |

### Directed Graphs
- **Directed Edge**: An edge that has a direction, denoted as \( uv \), indicating it starts from vertex \( u \) and ends at vertex \( v \).
- **Visualization**: Directed edges are depicted using arrows.

### Graph Models
- **Acquaintanceship Graphs**: Vertices represent people; an edge indicates mutual knowledge.
- **Influence Graphs**: Directed edges represent influence relationships.
- **Call Graphs**: Directed multigraphs model telephone calls between users.
- **Web Graphs**: Each web page is a vertex; directed edges represent hyperlinks.
- **Precedence Graphs**: Vertices represent statements in a program; directed edges indicate execution order.

## Implementation/Examples
```plaintext
# Example of a simple graph
Vertices: A, B, C
Edges: AB, AC, BC

# Example of a digraph
Vertices: 1, 2, 3
Edges: 12 (1 -> 2), 23 (2 -> 3), 31 (3 -> 1)
```

> [!note] **Important Note**: In a simple graph, the edge \( ab \) is the same as \( ba \). In a multigraph, if there are multiple edges between two vertices, they are counted as edges of multiplicity.

> [!warning] **Caution**: When modeling real-world scenarios with graphs, ensure that the properties of the graph (simple, multigraph, directed) accurately reflect the relationships being represented.

## Related
- [[Logic - Propositional Logic]]
- [[Chapter+2]]
- [[Chapter+4+How+Designers+Think]]
- [[CS1231+TUTORIAL+3]]
- [[Tutorial+1+Solution]]