class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] # list comprehension

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h% self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h] 

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()
print(t.get_hash('6-Mar'))
t['6-Mar']=130
t['7-Mar']=110
t['8-Mar']=140
t['9-Mar']=100
t['10-Mar']=210

print(t.arr)
print(t['8-Mar'])

del t['10-Mar']
print(t['10-Mar'])