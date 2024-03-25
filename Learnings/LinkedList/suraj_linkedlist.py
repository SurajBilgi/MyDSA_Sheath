class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_my_ll(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print("None")

    def get_length(self):
        if self.head is None:
            # print("Length is 0")
            return 0
        
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        # print("Length is",count)
        return count



    def insert_at_beginning(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)

        last = self.head
        while last.next:
            last = last.next
    
        last.next = Node(data)

    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            raise "Invalid Index"
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break

            itr = itr.next
            count += 1

    def delete_at_node(self,index):
        if index<0 or index>self.get_length():
            raise "Invalid Index"
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1


    def delete_value(self,value):
        itr = self.head
        while itr:
            if itr.data == value:
                print("Found it",itr.data)
                itr.next = itr.next.next
            itr = itr.next

        


linked_list = LinkedList()
linked_list.print_my_ll()
linked_list.get_length()
linked_list.insert_at_beginning(1)
linked_list.insert_at_end(4)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.insert_at_end(5)
linked_list.insert_at_index(5,7)
linked_list.print_my_ll()
linked_list.delete_at_node(3)
# linked_list.delete_value(2)
linked_list.print_my_ll()


