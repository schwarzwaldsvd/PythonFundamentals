from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    # get the last element without removing it from the stack
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


s = Stack()
s.push(5)
s.push(34)
s.push(335)

if __name__ == '__main__':
    print(s.size())