class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class ll:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_all(self):
        if self.head is None:
            print("LL is empty")
            return
        
        itr = self.head
        while itr:
            print(itr.data,end=" -> ")
            itr = itr.next


        




myll = ll()
myll.print_all()

myll.insert_at_begining(1)
myll.insert_at_begining(2)
myll.insert_at_begining(3)

myll.print_all()