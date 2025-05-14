"""
Binary Search Tree (BST) Implementation

A Binary Search Tree is a node-based binary tree data structure that has the following properties:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
- There are no duplicate keys in the tree.

Time Complexity:
- Search: O(log n) average case, O(n) worst case (when tree is skewed)
- Insert: O(log n) average case, O(n) worst case
- Delete: O(log n) average case, O(n) worst case
- Min/Max: O(log n) average case, O(n) worst case
- Traversal: O(n) - must visit every node

Space Complexity:
- O(n) for storing n nodes
- O(h) for recursive call stack during traversals, where h is the height of the tree

Applications:
- Implement other data structures like maps, sets, and priority queues
- Database indexing
- Sorting algorithms
- Decision trees in machine learning
- Expression evaluation and syntax parsing
"""


class Node:
    """
    Node class represents a single node in the Binary Search Tree.
    Each node contains a value and pointers to left and right children.
    """

    def __init__(self, value):
        """
        Initialize a new Node with the given value.

        Args:
            value: The data to be stored in this node
        """
        self.value = value
        self.left = None  # Pointer to left child (smaller values)
        self.right = None  # Pointer to right child (larger values)


class BinarySearchTree:
    """
    Binary Search Tree implementation that follows these rules:
    - Left child contains a value less than its parent node
    - Right child contains a value greater than its parent node
    - No duplicate values are allowed
    - Each subtree is also a valid Binary Search Tree
    """

    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        Root is set to None for an empty tree.
        """
        self.root = None

    def insert(self, value):
        """
        Insert a new value into the Binary Search Tree.

        The method will:
        1. Create a new Node with the given value
        2. If the tree is empty, set the new node as root
        3. Otherwise, find the correct position to insert by traversing
           the tree according to BST properties

        Args:
            value: The value to insert into the tree

        Returns:
            True if insertion was successful, False if the value already exists
        """
        # Create a new node with the given value
        new_node = Node(value)

        # If the tree is empty, set the new node as root and return
        if self.root is None:
            self.root = new_node
            return True

        # Start traversing from the root
        current = self.root

        # Traverse until we find the correct position
        while True:
            # If the value already exists, don't insert it (no duplicates)
            if value == current.value:
                return False

            # If value is less than current node, go left
            if value < current.value:
                # If there's no left child, insert the new node here
                if current.left is None:
                    current.left = new_node
                    return True
                # Otherwise, move to the left child and continue
                current = current.left
            # If value is greater than current node, go right
            else:
                # If there's no right child, insert the new node here
                if current.right is None:
                    current.right = new_node
                    return True
                # Otherwise, move to the right child and continue
                current = current.right

    def contains(self, value):
        """
        Check if a value exists in the Binary Search Tree.

        Args:
            value: The value to search for

        Returns:
            True if value is found, False otherwise
        """
        # Start from the root
        current = self.root

        # Traverse until we find the value or reach a leaf node
        while current is not None:
            # Found the value
            if value == current.value:
                return True
            # If value is less than current node, go left
            elif value < current.value:
                current = current.left
            # If value is greater than current node, go right
            else:
                current = current.right

        # Value was not found
        return False

    def find_min(self):
        """
        Find the minimum value in the Binary Search Tree.

        Returns:
            The minimum value in the tree, or None if the tree is empty
        """
        # If tree is empty, return None
        if self.root is None:
            return None

        # The minimum value is always the leftmost node
        current = self.root
        while current.left is not None:
            current = current.left

        return current.value

    def find_max(self):
        """
        Find the maximum value in the Binary Search Tree.

        Returns:
            The maximum value in the tree, or None if the tree is empty
        """
        # If tree is empty, return None
        if self.root is None:
            return None

        # The maximum value is always the rightmost node
        current = self.root
        while current.right is not None:
            current = current.right

        return current.value

    def delete(self, value):
        """
        Remove a value from the Binary Search Tree.

        Args:
            value: The value to remove

        Returns:
            True if removal was successful, False if the value doesn't exist
        """
        # Initialize parent and current pointers
        parent = None
        current = self.root

        # Find the node to delete and its parent
        while current is not None and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # If the value was not found, return False
        if current is None:
            return False

        # Case 1: Node to delete has no children (leaf node)
        if current.left is None and current.right is None:
            # If it's not the root
            if current != self.root:
                # Remove reference from parent
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                # Tree becomes empty
                self.root = None

        # Case 3: Node to delete has two children
        elif current.left is not None and current.right is not None:
            # Find the successor (minimum value in right subtree)
            successor_parent = current
            successor = current.right

            # Find leftmost node in the right subtree
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Copy successor value to current node
            current.value = successor.value

            # Delete the successor (which has at most one child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        # Case 2: Node to delete has one child
        else:
            # Determine which child exists
            child = current.left if current.left is not None else current.right

            # If it's not the root
            if current != self.root:
                if parent.left == current:
                    parent.left = child
                else:
                    parent.right = child
            else:
                # Root is being replaced
                self.root = child

        return True

    def find(self, value):
        """
        Find a node in the Binary Search Tree.

        Args:
            value: The value to find

        Returns:
            The Node object if found, None otherwise
        """
        current = self.root

        while current is not None:
            if value == current.value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    # Traversal methods
    def inorder_traversal(self):
        """
        Perform in-order traversal (Left-Root-Right).

        Returns:
            A list containing the values in sorted order
        """
        result = []

        def inorder(node):
            if node:
                # Visit left subtree
                inorder(node.left)
                # Visit root
                result.append(node.value)
                # Visit right subtree
                inorder(node.right)

        inorder(self.root)
        return result

    def preorder_traversal(self):
        """
        Perform pre-order traversal (Root-Left-Right).

        Returns:
            A list containing the values in pre-order
        """
        result = []

        def preorder(node):
            if node:
                # Visit root
                result.append(node.value)
                # Visit left subtree
                preorder(node.left)
                # Visit right subtree
                preorder(node.right)

        preorder(self.root)
        return result

    def postorder_traversal(self):
        """
        Perform post-order traversal (Left-Right-Root).

        Returns:
            A list containing the values in post-order
        """
        result = []

        def postorder(node):
            if node:
                # Visit left subtree
                postorder(node.left)
                # Visit right subtree
                postorder(node.right)
                # Visit root
                result.append(node.value)

        postorder(self.root)
        return result

    def level_order_traversal(self):
        """
        Perform level-order (breadth-first) traversal.

        Returns:
            A list containing the values in level-order
        """
        if not self.root:
            return []

        result = []
        queue = [self.root]

        while queue:
            # Dequeue a node
            node = queue.pop(0)
            result.append(node.value)

            # Enqueue children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def height(self):
        """
        Calculate the height of the tree.

        Returns:
            The height of the tree, -1 for an empty tree
        """

        def calculate_height(node):
            if node is None:
                return -1
            left_height = calculate_height(node.left)
            right_height = calculate_height(node.right)
            return 1 + max(left_height, right_height)

        return calculate_height(self.root)


def visualize_tree(tree):
    """
    Function to display a simple visualization of the binary search tree.

    Args:
        tree: The BinarySearchTree instance to visualize
    """

    def print_tree(node, prefix="", is_left=True):
        if not node:
            return

        # Print right branch first (top of the visualization)
        print_tree(node.right, prefix + ("    " if is_left else "    "), False)

        # Print current node
        node_prefix = prefix + ("└── " if is_left else "┌── ")
        print(node_prefix + str(node.value))

        # Print left branch
        left_prefix = prefix + ("    " if not is_left else "    ")
        print_tree(node.left, left_prefix, True)

    # Start printing from the root
    if tree.root:
        print("\nTree Visualization:")
        print_tree(tree.root, "", True)
    else:
        print("Tree is empty")


if __name__ == "__main__":
    # Create a BST instance
    bst = BinarySearchTree()

    # Insert the values 50, 30, 70, 20, 40, 60, 80
    values = [50, 30, 70, 20, 40, 60, 80]

    print("Creating BST with values:", values)
    for value in values:
        bst.insert(value)
        print(f"Inserted {value}")

    # Visualize the tree
    visualize_tree(bst)

    # Demonstrate other BST operations
    print("\nTree Operations:")
    print(f"Contains 40: {bst.contains(40)}")
    print(f"Contains 90: {bst.contains(90)}")
    print(f"Minimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    print(f"Tree height: {bst.height()}")

    print("\nTraversals:")
    print(f"In-order: {bst.inorder_traversal()}")
    print(f"Pre-order: {bst.preorder_traversal()}")
    print(f"Post-order: {bst.postorder_traversal()}")
    print(f"Level-order: {bst.level_order_traversal()}")

    # Demonstrate deletion
    print("\nDeleting node with value 30:")
    bst.delete(30)
    visualize_tree(bst)
    print(f"In-order after deletion: {bst.inorder_traversal()}")

    """
    The resulting tree structure should look like:
    
            50
           /  \
         30    70
        / \    / \
      20  40  60  80
    
    This is a balanced binary search tree where:
    - Each node's left subtree contains values less than the node's value
    - Each node's right subtree contains values greater than the node's value
    - No duplicate values are allowed
    """
