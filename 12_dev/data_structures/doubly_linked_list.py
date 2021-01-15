class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev
        self.data = data
        self.next = next
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)
       
        self.head.prev = node
        self.head = node
        self.tail = node
        
        # self.tail.next = node
            
        if self.tail is not None:
            self.tail = self.head.prev
    
      
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

    # def print_backward(self):
    #     if self.head is None:
    #         print("Linked List is empty")
    #         return

               
    #     itr = self.head
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception(f"Index '{index}' is not a valid index")
        
        if index == 0: # trying to remove the head
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
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

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        self.insert_at(self.find_index_by_value(data_after) + 1, data_to_insert)
    
    
    def remove_by_value(self, data):
    # Remove first node that contains data
        self.remove_at(self.find_index_by_value(data))

if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_at_beginning(5)
    ll.print_forward()
    print(ll.head.prev.data)
    ll.insert_at_beginning(89)
    ll.print_forward()
    print(ll.head.next.data)
    # ll.insert_at_beginning(85)
    # print(ll.get_length())
    # print(ll.head.prev)

    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
    # ll.insert_at_end(5624)
    ll.print_forward()
    
    # print(ll.tail.data)
    # print(ll.find_index_by_value(79))
    # ll.insert_after_value(79,99)
    # ll.print()

    # ll.insert_values(["banana","mango","grapes","orange","figs"])
    # ll.print_forward()

    