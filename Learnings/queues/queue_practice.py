
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None


    def isempty(self):
        if self.head is None:
            return True
        
    def enqueue(self,data):
        if self.isempty():
            node = Node(data)
            self.head = node
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next

            
        node = Node(data)
        itr.next = node


    def dequeue(self):
        if self.head is None:
            print("Stack is Empty")
            return
        
        print("Item is Dequeued:",self.head.data)
        self.head = self.head.next
        return self.head.data

        
    def print_all(self):
        if self.head is None:
            print("Stack is Empty")
            return
        
        itr = self.head
        while itr:
            print(itr.data,end=" -> ")
            itr = itr.next
        print(None)

    def peek(self):
        if self.isempty():
            print("The Stack is Empty")
            return
        
        # print("The Top item is :", self.head.data)
        return self.head.data

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_all()


print("Queue Peek:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Queue Peek after dequeuing:", queue.peek())

queue.print_all()
