from collections import deque

class Stack:
    def __init__(self):
        self._container = deque()
    
    def push(self, value):
        self._container.append(value)
    
    def pop(self):
        return self._container.pop()
    
    # get the last element without removing it from the stack
    def peek(self):
        return self._container[-1]
    
    def is_empty(self):
        return len(self._container) == 0
    
    def size(self):
        return len(self._container)


s = Stack()
s.push(5)
s.push(34)
s.push(335)

if __name__ == '__main__':
    print(s.size())