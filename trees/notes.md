# Trees Notes

## 1) Complete Binary Tree

A complete binary tree has every level fully filled except possibly the last
level, and the last level is filled from left to right.

### Why it matters

- Nodes are packed tightly.
- If nodes are indexed in level order, parent/child indexes have clean rules.
- This is why complete binary trees are often stored in arrays (no need for
  explicit linked nodes).
- Core examples: binary heap and segment tree implementations.

### Important structural property

The left and right subtrees of a complete binary tree are also complete binary
trees. More precisely, at least one of those two subtrees is a perfect binary
tree.

Useful observation: if the right subtree reaches the same height as the left
subtree, then the left subtree must already be completely full at every level;
otherwise, nodes could not have been placed that far right.

## 2) Perfect Binary Tree

A perfect binary tree is a special case of a complete binary tree where every
level is fully filled.

If depth is `h`, total node count is:

`2^h - 1`

This comes from a geometric series and is a very useful shortcut.

## 3) Binary Search Tree (BST)

A Binary Search Tree (BST) is defined by this rule:

- for every node, **all nodes** in its left subtree are smaller
- for every node, **all nodes** in its right subtree are larger

Quick memory aid: **left smaller, right larger**.

### Common beginner mistake

Do not only compare a node with its direct children. The rule is about the
entire subtree, not just one level.

### BST example (valid)

```
      7
    /   \
   4     9
  / \     \
 1   5     10
```

This is valid because:
- every value in the left subtree of `7` is `< 7`
- every value in the right subtree of `7` is `> 7`
- the same rule also holds recursively for nodes like `4` and `9`

### Non-BST example (invalid)

```
      7
    /   \
   4     9
  / \     \
 1   8     10
```

This is not a BST because node `8` is in the left subtree of `7` but `8 > 7`,
which breaks the global subtree rule.

### Why BST is useful

BST gives ordered structure, so search can skip half the tree at each step:

- If searching for value `x`:
  - `x < root.val`: go left
  - `x > root.val`: go right
  - equal: found

Compared to a normal binary tree (no ordering), this is much faster in
practice because you do not always need to traverse the entire tree.

## 4) Height-Balanced Binary Tree

A height-balanced binary tree satisfies this rule:

- for **every node**, the height difference between left subtree and right
  subtree is at most `1`

Important: this must hold at every node, not just at the root.

### Example (balanced)

```
        1
      /   \
     2     3
    /     / \
   4     5   7
          \
           6
```

This tree is height-balanced because each node keeps left/right heights close
enough (difference `<= 1`).

### Example (not balanced)

```
        1
      /   \
     2     3
    /     / \
   4     5   7
  /
 8
      \
       6
```

This is not height-balanced. For node `2`, left subtree height is much larger
than right subtree height (difference `> 1`).

### Why this matters

If a height-balanced binary tree has `N` nodes, its height is `O(log N)`.
That is a key reason many tree data structures try to stay balanced:

- insert: fast
- delete: fast
- search: fast
- update: fast

If a tree becomes very unbalanced, it can degrade toward a linked-list shape:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
```

In that case, operations become much slower.

## 5) Self-Balanced Binary Tree

From the height-balanced section: when tree height stays around `O(log N)`,
insert, delete, search, and update remain efficient.

A self-balanced binary tree keeps this property over time by adjusting its
structure during insertions and deletions.

In other words: the tree does not just start balanced; it actively re-balances
itself after updates.

### Classic example

One of the most classic self-balanced trees is the **Red-Black Tree**, which is
a self-balanced BST.

### Core operation: rotation

To maintain balance, the key structural operation is **rotation**:

- left rotation
- right rotation

Rotations change local parent/child relationships while preserving BST order,
which is why they are central to red-black tree balancing logic.
