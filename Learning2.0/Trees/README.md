# Trees Data Structures

This folder contains implementations of various tree data structures, with a focus on Binary Search Trees.

## Binary Search Tree (BST)

### Overview

A Binary Search Tree is a node-based binary tree data structure that maintains the BST property: for each node, all elements in the left subtree are less than the node's value, and all elements in the right subtree are greater than the node's value.

```
        50
       /  \
     30    70
    / \    / \
  20  40  60  80
```

### Key Properties

- Ordered: Left child < Parent < Right child
- No duplicates: Each value appears at most once
- Binary: Each node has at most two children
- Search-optimized: Allows efficient lookup, addition, and removal of items

### Operations

The `BinarySearchTree.py` file implements the following operations:

1. **Insert**: Adds a new value to the tree while maintaining the BST property.
2. **Contains/Search**: Checks if a value exists in the tree.
3. **Delete**: Removes a value from the tree while maintaining the BST property.
4. **Find Min/Max**: Finds the minimum or maximum value in the tree.
5. **Traversals**:
   - In-order (Left-Root-Right): Visits nodes in ascending order
   - Pre-order (Root-Left-Right): Useful for copying the tree
   - Post-order (Left-Right-Root): Useful for deleting the tree
   - Level-order: Breadth-first traversal of the tree
6. **Height**: Calculates the maximum depth of the tree

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insert    | O(log n)     | O(n)       |
| Delete    | O(log n)     | O(n)       |
| Traversal | O(n)         | O(n)       |

The worst-case time complexity occurs when the tree becomes skewed (resembling a linked list).

### Usage Example

```python
# Create a BST instance
bst = BinarySearchTree()

# Insert values
values = [50, 30, 70, 20, 40, 60, 80]
for value in values:
    bst.insert(value)

# Check if a value exists
print(bst.contains(40))  # True
print(bst.contains(90))  # False

# Find min and max values
print(bst.find_min())  # 20
print(bst.find_max())  # 80

# Get in-order traversal (sorted output)
print(bst.inorder_traversal())  # [20, 30, 40, 50, 60, 70, 80]

# Delete a value
bst.delete(30)
```

## Other Tree Data Structures

### Binary Tree vs. Binary Search Tree

A Binary Tree is a more general structure where each node has at most two children, without any ordering property. A Binary Search Tree adds the constraint that values must be ordered.

### Balanced BSTs

When a BST becomes skewed, its performance degrades. Balanced BSTs maintain a balanced structure to ensure O(log n) operations:

- AVL Tree: Self-balancing BST where the heights of the two child subtrees differ by at most one
- Red-Black Tree: Self-balancing BST with additional properties that ensure the tree remains balanced
- B-Tree: Generalization of a BST that allows nodes to have more than two children

### Heaps

A Heap is a specialized tree-based data structure:

- Min Heap: The parent node is always smaller than or equal to its children
- Max Heap: The parent node is always greater than or equal to its children

### Tries

A Trie (prefix tree) is a tree-like data structure used to store a dynamic set of strings, typically used for fast prefix searches.

## Applications of Trees

- File systems (directory structures)
- Database indexing
- Syntax parsing in compilers
- Network routing algorithms
- Decision trees in machine learning
- Expression evaluation
- Game AI (minimax algorithm) 