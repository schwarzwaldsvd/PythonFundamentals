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
        
        itr = self.tail
        itr.next = Node(data, None, itr)
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

    
    def insert_values(self, data_list, overwrite):
        if overwrite:
            self.head = None
            self.size = 0
        for data in data_list:
            self.insert_at_end(data)

    
    def insert_values_reversed(self, data_list, overwrite):
        if overwrite:
            self.head = None
            self.size = 0
        for data in data_list:
            self.insert_at_beginning(data)


    def get_length_fwd(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count, self.size

    
    def get_length_bkw(self):
        count = 0
        itr = self.tail
        while itr:
            count += 1
            itr = itr.prev
        return count, self.size


    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise Exception(f"Index '{index}' is not a valid index")
        
        if index == 0: # trying to remove the head
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next.next is not None:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                else:
                    itr.next = None
                    self.tail = itr
                self.size -= 1
                break
            itr = itr.next
            count += 1
    
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.size:
            raise Exception(f"Index '{index}' is not a valid index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
                if count == index - 1:
                    node = Node(data, itr.next, itr)
                    itr.next = node
                    itr.next.next.prev = itr.next
                    self.size += 1
                    break

                itr = itr.next
                count += 1

        
    # finds the value and returns its respective index from the list
    def find_index_by_value(self, value):
        if self.head is None:
            return -1

        if self.head.data == value:
            return 0
        
        index = 0
        itr = self.head
        while itr:
            if itr.data == value:
                return index
            itr = itr.next
            index += 1

    
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after 'data_after' node
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next, self.head)
            self.head.next.next.prev = self.head.next
            self.size += 1
            return
        
        index = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                if index < self.size - 1:
                    itr.next = Node(data_to_insert, itr.next, itr)
                    itr.next.next.prev = itr.next
                else:  # at the end
                    itr.next = Node(data_to_insert, None, itr)
                    self.tail = itr.next
                self.size += 1
                break
            index += 1
            itr = itr.next

    
    # Remove first node that contains data
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return

        index = 0
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if index < self.size - 2:
                    itr.next.prev = itr
                else:
                    self.tail = itr
                self.size -= 1
                break
            itr = itr.next
            index += 1


    def contains(self, data):
        if self.head is None:
            return -1

        if self.head.data == data:
            return True
       
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.print_forward()
    ll.insert_at_beginning(89)
    ll.insert_at_beginning(90)
    ll.insert_values(["banana", "apple", "melon", "ice-cream"], True)
    ll.print_forward()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    print(ll.get_length_fwd())
    print(ll.get_length_bkw())
    ll.remove_by_value("ice-cream")
    ll.print_forward()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.insert_at_beginning(85)
    print(ll.get_length_fwd())

    ll.insert_at_end(79)
    ll.insert_at_end(1)
    ll.insert_at_end(5624)
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.print_backward()
    
    print(ll.find_index_by_value("ice-cream"))
    ll.insert_after_value(79,99)
    ll.print_forward()

    ll.insert_values(["banana","mango","grapes","orange","figs"], False)
    ll.print_forward()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    print(ll.get_length_fwd())
    print(ll.get_length_bkw())
    print(ll.contains("mango"))
