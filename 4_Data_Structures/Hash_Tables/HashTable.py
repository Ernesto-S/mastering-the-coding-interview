
class HashTable:
    def __init__ (self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):

        if isinstance(key, str):
            return sum(ord(char) for char in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            raise TypeError("Key must be an integer or string")
        
    
    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
            self.table[index].append((key, value))
    
    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return True
        return False
    
    def keys(self):
        keys = []
        for bucket in self.table:
            if bucket is not None:
                for k, v in bucket:
                    keys.append(k)
        return keys
    
myHashTable = HashTable(1)
myHashTable.insert('grapes', 10000)
myHashTable.insert('apples', 23)
myHashTable.insert('oranges', 2)
print(myHashTable.table) 
print(myHashTable.search('apples'))  # Output: one

print(myHashTable.keys())  # Output: ['grapes', 'apples
myHashTable.delete('apples')
print(myHashTable.keys())  # Output: ['grapes', 'oranges']