class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            self.tail = self.head
            self.size += 1
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        self.tail = itr

        node = Node(data, self.head, None)
        self.head.prev = node
        self.head = node
        self.size += 1


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            self.tail = self.head
            self.size += 1
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)
        # self.prev = itr
        self.tail = itr.next
        self.size += 1

    
      
    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        llstr += '<null>'
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.tail
        llstr = '<null>'
        while itr:
            llstr += ' <-- ' + str(itr.data)
            itr = itr.prev
        print(llstr)

    

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.print_forward()
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(90)
    ll.print_forward()
    # print(ll.tail.prev)
    # print(ll.tail.next)
    # # print(ll.head.prev)
    # print(ll.head.next)
    # ll.insert_at_beginning(85)
    # print(ll.get_length())
    # print(ll.head.prev)

    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_at_end(5624)
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.print_backward()
    
    # print(ll.tail.data)
    # print(ll.find_index_by_value(79))
    # ll.insert_after_value(79,99)
    # ll.print()

    # ll.insert_values(["banana","mango","grapes","orange","figs"])
    # ll.print_forward()

    