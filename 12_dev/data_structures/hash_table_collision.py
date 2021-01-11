class HashTable():
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)] # list comprehension

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h% self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][idx] = (key,value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]

t = HashTable()
print(t.get_hash('6-Mar'))
t['6-Mar']=130
t['7-Mar']=110
t['8-Mar']=140
t['9-Mar']=100
t['10-Mar']=210
t['13-Mar']=342 # hash 33 
t['22-Mar']=444 # hash 33 

print(t.arr)
print(t['22-Mar'])

del t['10-Mar']
print(t['10-Mar'])