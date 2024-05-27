class Node:
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left == None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        if self.root == None:
            return False
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

my_tree = BinarySearchTree()

print(my_tree.insert(20))
print(my_tree.insert(10))
print(my_tree.insert(50))

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

print(my_tree.contains(10))
print(my_tree.contains(70))


