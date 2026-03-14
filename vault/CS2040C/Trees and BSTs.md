---
tags: [CS2040C, trees, BST, binary-tree, AVL, traversal]
---

# Trees and Binary Search Trees

## Overview

A tree is a hierarchical, non-linear data structure consisting of nodes connected by edges. A **binary tree** has at most two children per node. A **Binary Search Tree (BST)** adds an ordering property that enables efficient search, insertion, and deletion. CS2040C also covers **AVL trees** as a self-balancing BST.

## Tree Terminology

| Term | Definition |
|------|-----------|
| Root | The topmost node (no parent) |
| Leaf | A node with no children |
| Internal node | A node with at least one child |
| Depth | Number of edges from root to the node |
| Height | Number of edges on the longest path from the node to a leaf |
| Height of tree | Height of the root node |
| Degree | Number of children of a node |
| Subtree | A node and all its descendants |

## Binary Tree

### Node Structure

```cpp
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val) : data(val), left(nullptr), right(nullptr) {}
};
```

### Tree Traversals

Four standard traversals, each with $O(n)$ time and $O(h)$ space (where $h$ is the height):

```cpp
// Pre-order: Root -> Left -> Right
void preorder(TreeNode* root) {
    if (!root) return;
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

// In-order: Left -> Root -> Right
void inorder(TreeNode* root) {
    if (!root) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

// Post-order: Left -> Right -> Root
void postorder(TreeNode* root) {
    if (!root) return;
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " ";
}

// Level-order (BFS): Level by level, left to right
void levelOrder(TreeNode* root) {
    if (!root) return;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* curr = q.front(); q.pop();
        cout << curr->data << " ";
        if (curr->left) q.push(curr->left);
        if (curr->right) q.push(curr->right);
    }
}
```

> [!important] In-order Traversal of a BST
> In-order traversal of a BST produces elements in **sorted ascending order**. This is a key property frequently tested.

## Binary Search Tree (BST)

### BST Property

For every node $x$:
- All nodes in the left subtree have keys $<$ $x.key$
- All nodes in the right subtree have keys $>$ $x.key$

### Core Operations

```cpp
class BST {
    TreeNode* root;

    // Search: O(h)
    TreeNode* search(TreeNode* node, int key) {
        if (!node || node->data == key) return node;
        if (key < node->data) return search(node->left, key);
        return search(node->right, key);
    }

    // Insert: O(h)
    TreeNode* insert(TreeNode* node, int key) {
        if (!node) return new TreeNode(key);
        if (key < node->data)
            node->left = insert(node->left, key);
        else if (key > node->data)
            node->right = insert(node->right, key);
        return node;
    }

    // Find minimum: O(h)
    TreeNode* findMin(TreeNode* node) {
        while (node->left) node = node->left;
        return node;
    }

    // Find maximum: O(h)
    TreeNode* findMax(TreeNode* node) {
        while (node->right) node = node->right;
        return node;
    }

    // Delete: O(h)
    TreeNode* remove(TreeNode* node, int key) {
        if (!node) return nullptr;
        if (key < node->data)
            node->left = remove(node->left, key);
        else if (key > node->data)
            node->right = remove(node->right, key);
        else {
            // Case 1: Leaf node
            if (!node->left && !node->right) {
                delete node;
                return nullptr;
            }
            // Case 2: One child
            if (!node->left) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            }
            if (!node->right) {
                TreeNode* temp = node->left;
                delete node;
                return temp;
            }
            // Case 3: Two children
            // Replace with in-order successor (min of right subtree)
            TreeNode* successor = findMin(node->right);
            node->data = successor->data;
            node->right = remove(node->right, successor->data);
        }
        return node;
    }
};
```

### BST Operations Complexity

| Operation | Average (balanced) | Worst (skewed) |
|-----------|-------------------|----------------|
| Search | $O(\log n)$ | $O(n)$ |
| Insert | $O(\log n)$ | $O(n)$ |
| Delete | $O(\log n)$ | $O(n)$ |
| Find Min/Max | $O(\log n)$ | $O(n)$ |
| In-order Successor | $O(\log n)$ | $O(n)$ |

> [!warning] Degenerate BST
> If elements are inserted in sorted order, the BST degenerates into a linked list with height $n$. All operations become $O(n)$. This motivates self-balancing BSTs.

## AVL Tree (Self-Balancing BST)

### Balance Factor

For each node: $\text{balance factor} = \text{height(left subtree)} - \text{height(right subtree)}$

An AVL tree maintains $|\text{balance factor}| \leq 1$ for every node.

### Rotations

When insertion or deletion violates the balance condition, we restore balance with rotations:

**Left-Left (LL) Case** -- Right Rotation:
```
    z                y
   / \             /   \
  y   T4   -->    x     z
 / \             / \   / \
x   T3          T1 T2 T3 T4
```

**Right-Right (RR) Case** -- Left Rotation:
```
  z                  y
 / \               /   \
T1   y    -->     z     x
    / \          / \   / \
   T2  x        T1 T2 T3 T4
      / \
     T3 T4
```

**Left-Right (LR) Case** -- Left Rotation on y, then Right Rotation on z:
```
    z               z              x
   / \             / \           /   \
  y   T4  -->     x   T4  -->  y     z
 / \             / \           / \   / \
T1  x           y   T3       T1 T2 T3 T4
   / \         / \
  T2  T3      T1  T2
```

**Right-Left (RL) Case** -- Right Rotation on y, then Left Rotation on z:
```
  z             z                 x
 / \           / \              /   \
T1   y  -->   T1  x    -->    z     y
    / \          / \          / \   / \
   x  T4       T2  y        T1 T2 T3 T4
  / \              / \
 T2  T3           T3  T4
```

### AVL Insertion

```cpp
struct AVLNode {
    int data, height;
    AVLNode *left, *right;
    AVLNode(int val) : data(val), height(0), left(nullptr), right(nullptr) {}
};

int height(AVLNode* n) { return n ? n->height : -1; }
int balanceFactor(AVLNode* n) { return n ? height(n->left) - height(n->right) : 0; }

void updateHeight(AVLNode* n) {
    n->height = 1 + max(height(n->left), height(n->right));
}

AVLNode* rotateRight(AVLNode* z) {
    AVLNode* y = z->left;
    z->left = y->right;
    y->right = z;
    updateHeight(z);
    updateHeight(y);
    return y;
}

AVLNode* rotateLeft(AVLNode* z) {
    AVLNode* y = z->right;
    z->right = y->left;
    y->left = z;
    updateHeight(z);
    updateHeight(y);
    return y;
}

AVLNode* balance(AVLNode* node) {
    updateHeight(node);
    int bf = balanceFactor(node);
    if (bf > 1) { // Left-heavy
        if (balanceFactor(node->left) < 0) // LR case
            node->left = rotateLeft(node->left);
        return rotateRight(node); // LL case
    }
    if (bf < -1) { // Right-heavy
        if (balanceFactor(node->right) > 0) // RL case
            node->right = rotateRight(node->right);
        return rotateLeft(node); // RR case
    }
    return node;
}

AVLNode* insert(AVLNode* node, int key) {
    if (!node) return new AVLNode(key);
    if (key < node->data)
        node->left = insert(node->left, key);
    else if (key > node->data)
        node->right = insert(node->right, key);
    return balance(node);
}
```

### AVL Tree Complexity

| Operation | Time | Space |
|-----------|------|-------|
| Search | $O(\log n)$ | $O(1)$ iterative |
| Insert | $O(\log n)$ | $O(\log n)$ recursive |
| Delete | $O(\log n)$ | $O(\log n)$ recursive |

> [!note] AVL Height Bound
> An AVL tree with $n$ nodes has height $h \leq 1.44 \log_2(n+2)$. This guarantees $O(\log n)$ operations in the worst case, unlike a plain BST.

## Related Notes

- [[Heaps and Priority Queues]] - another tree-based structure (but not a BST)
- [[Complexity Analysis]] - understanding O(log n) from balanced trees
- [[Graphs]] - trees are special cases of graphs
- [[Stacks and Queues]] - used in tree traversal algorithms
