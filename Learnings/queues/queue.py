class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            dequeued = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.front.data

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue Peek:", queue.peek())
print("Dequeued:", queue.dequeue())
print("Queue Peek after dequeuing:", queue.peek())
