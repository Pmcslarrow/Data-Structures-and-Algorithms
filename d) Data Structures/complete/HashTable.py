#HashTable.py
#Here I implement my first ever Hash Table using linear probing
#I got a little help from https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html
#But majority of this I struggled thorugh and overall added my own take as I thought theirs was not well made in parts
#Made on 8/21/21
#Paul McSlarrow

class HashTable:
    def __init__(self, arr_size):
        self.size = arr_size
        self.slots = [None for i in range(self.size)]
        self.data = [None for i in range(self.size)]

    def hash(self, key):
        ans = 0
        for i in key:
            ans += ord(i)
        return ans % self.size

    def rehash(self, key):
        hash = self.hash(key)
        return hash+1 % self.size

     
    def __setitem__(self, key, value):                  #These dunder methods let you juse indexing with []
        hash = self.hash(key)
        counter = 0

        if self.slots[hash] is None:
            self.slots[hash] = key
            self.data[hash] = value
        else:
            if self.slots[hash] == key:
                self.data[hash] = value
            else:
                new_hash = self.rehash(key)
                while self.slots[new_hash] is not None and self.slots[new_hash] != key:
                    counter += 1
                    new_hash = self.rehash(key) + counter
                    if new_hash >= self.size:
                        new_hash = new_hash % self.size
                
                self.slots[new_hash] = key
                self.data[new_hash] = value
        

        
    def __getitem__(self, key):
        found = False
        hash = self.hash(key) 
        counter = 0

        while not(found):
            if self.slots[hash] == key: 
                found = True
            else:
                hash = self.rehash(key)    
                if self.slots[hash] == key:
                    found = True
                else:
                    counter += 1
                    hash = self.rehash(key) + counter
                    if hash >= self.size:
                        hash = hash % self.size


        return self.data[hash]

            
    def __str__(self):
        return 'slots: ' + str(self.slots) + '\n' + 'data: ' + str(self.data)

paul = HashTable(10)

#THESE ALL HAVE HASHES OF 5... IT SHOWS THAT MY COLLISION HANDLING WORKS!!!!
paul['Kyle'] = 60
paul['Maxence'] = 19
paul['alis'] = 55
paul['abrt'] = 99
paul['ab'] = 22
paul['cvb'] = 1
print(paul)
print('alis == ', paul['alis'])
print('cvb == ', paul['cvb'])















