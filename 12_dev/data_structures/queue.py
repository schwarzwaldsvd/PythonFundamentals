from collections import deque

class Queue:
    def __init__(self):
        self._buffer = deque()

    def enqueue(self, value):
        self._buffer.appendleft(value)

    def dequeue(self):
        return self._buffer.pop()

    def is_empty(self):
        return len(self._buffer)==0
    
    def size(self):
        return len(self._buffer)

pq = Queue()
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 Apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 Apr, 11.02 AM',
    'price': 132.00
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 Apr, 11.03 AM',
    'price': 135.00
})

if __name__ == '__main__':
    print(pq._buffer)
    print(pq.dequeue())
    print(pq.size())