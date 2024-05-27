import graphviz

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root, dot):
    if root:
        inorder_traversal(root.left, dot)
        dot.node(str(root.key), label=str(root.key))
        if root.left:
            dot.edge(str(root.left.key), str(root.key), style='dotted')
        if root.right:
            dot.edge(str(root.key), str(root.right.key), style='dotted')
        inorder_traversal(root.right, dot)

def preorder_traversal(root, dot):
    if root:
        dot.node(str(root.key), label=str(root.key))
        if root.left:
            dot.edge(str(root.key), str(root.left.key), style='dotted')
        if root.right:
            dot.edge(str(root.key), str(root.right.key), style='dotted')
        preorder_traversal(root.left, dot)
        preorder_traversal(root.right, dot)

def postorder_traversal(root, dot):
    if root:
        postorder_traversal(root.left, dot)
        postorder_traversal(root.right, dot)
        dot.node(str(root.key), label=str(root.key))
        if root.left:
            dot.edge(str(root.left.key), str(root.key), style='dotted')
        if root.right:
            dot.edge(str(root.right.key), str(root.key), style='dotted')

def visualize_binary_tree(root):
    dot_inorder = graphviz.Digraph(comment='Inorder Traversal')
    inorder_traversal(root, dot_inorder)
    dot_inorder.render('inorder_traversal', view=True, format='png')

    dot_preorder = graphviz.Digraph(comment='Preorder Traversal')
    preorder_traversal(root, dot_preorder)
    dot_preorder.render('preorder_traversal', view=True, format='png')

    dot_postorder = graphviz.Digraph(comment='Postorder Traversal')
    postorder_traversal(root, dot_postorder)
    dot_postorder.render('postorder_traversal', view=True, format='png')

# Example usage:
root = None
keys = [5, 3, 7, 2, 4, 6, 8]
for key in keys:
    root = insert(root, key)

visualize_binary_tree(root)