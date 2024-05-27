class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True


    def push(self,data):
        if self.isempty():
            node = Node(data)
            self.head = node
            return
        
        node = Node(data)
        node.next = self.head
        self.head = node


    def pop(self):
        if self.isempty():
            print("The Stack is Empty")
            return
        
        print("The Popped Item: ",self.head.data)
        self.head = self.head.next



    def peek(self):
        if self.isempty():
            print("The Stack is Empty")
            return
        
        print("The Top item is :", self.head.data)
        


    def print_all(self):
        if self.head is None:
            print("Stack is Empty")
            return
        
        itr = self.head
        while itr:
            print(itr.data,end=" -> ")
            itr = itr.next
        print(None)
        


    def size(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count




ms = Stack()
ms.peek()
ms.push(2)
ms.push(4)
ms.push(6)
ms.print_all()
ms.pop()
ms.peek()
ms.print_all()
print("lenght of the Stack", ms.size())