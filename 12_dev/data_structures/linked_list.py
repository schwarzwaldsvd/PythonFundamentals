class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0


    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            self.size += 1
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        self.tail = itr

        node = Node(data, self.head)
        self.head = node
        self.size += 1


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.tail = self.head
            self.size += 1
            return
        
        # itr = self.head
        # while itr.next:
        #     itr = itr.next
        itr = self.tail
        
        itr.next = Node(data, None)
        self.tail = itr.next
        self.size += 1


    def print(self):
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


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count, self.size


    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise Exception(f"Index '{index}' is not a valid index")
        
        if index == 0: # trying to remove the head
            self.head = self.head.next
            self.size -= 1
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                if itr.next.next is not None:
                    itr.next = itr.next.next
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
                    node = Node(data, itr.next)
                    itr.next = node
                    self.size += 1
                    break

                itr = itr.next
                count += 1


    def find_index_by_value(self, value):
        # finds the value and returns its respective index from the list
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
            self.head.next = Node(data_to_insert, self.head.next)
            self.size += 1
            return
        
        index = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                if index < self.size - 1:
                    itr.next = Node(data_to_insert, itr.next)
                else:  # when index == length - 1:
                    itr.next = Node(data_to_insert, None)
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
            self.size -= 1
            return

        index = 0      
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if index == self.size - 2:
                    self.tail = itr
                self.size -= 1
                break
            itr = itr.next
            index += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(1)
    ll.insert_at_beginning(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at(1, "cherry")
    ll.print()
    print(ll.size)
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.insert_values([10,20,30,40,50], False)
    ll.print()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.insert_values_reversed([22,33,44,55,77], False)
    ll.print()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    
    print(ll.find_index_by_value(79))
    ll.insert_after_value(79,99)
    ll.print()

    ll.insert_values_reversed(["pear","grapefruit","carrot","potato","jackfruit"], False)
    ll.insert_values(["banana","mango","grapes","orange","figs"], False)
    print("Index for 'figs' is ", ll.find_index_by_value("figs"))
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    ll.remove_by_value("orange") # remove orange from linked list
    print(ll.get_length())
    ll.remove_by_value("figs")
    ll.insert_at(8, "ice-cream")
    print(ll.find_index_by_value("figs"))
    ll.insert_after_value("jackfruit", "ice-cream")
    ll.remove_by_value("figs")
    ll.remove_by_value("orange")
    ll.print()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)
    print(ll.get_length())

    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
    print("head:", ll.head.data, ", tail:", ll.tail.data, ", size:", ll.size)