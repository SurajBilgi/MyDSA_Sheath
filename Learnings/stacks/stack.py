class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top.data

    def print(self):
        if self.top is None:
            print("Linked List is Empty!")
            return
        temp = self.top
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.print()

print("Stack Peek:", stack.peek())
print("Popped:", stack.pop())
print("Stack Peek after popping:", stack.peek())

stack.print()