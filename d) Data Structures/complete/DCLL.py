#DLL.PY 
#This program implements a doubly circular linked list (DCLL)

class Node:                                                                        
    def __init__(self, value):                                              #Each node has two pointers
        self.item = value                                                   #next and prev
        self.next = None
        self.prev = None
    
    def get_item(self):                                                     #Returns item in node
        return self.item

    def count(self):                                                        #The other count function that uses recursion
        if self.next is None:   
            return 1
        else:
            return 1 + self.next.count()

    def set_next(self, nextvalue):
        self.next = nextvalue

    def __str__(self):
        return str(self.item)

class DCLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.pop_total = 0

    def append(self, value):
        if self.is_empty():
            self.size += 1

            self.head = Node(value)
            self.head.next = self.head
            self.head.prev = self.head
            return                      #Think of the return as refreshing the page so that computer knows the switches

        if self.size == 1:
            self.size += 1

            head = self.head
            temp = Node(value)

            head.next = temp
            head.prev = temp

            temp.next = head
            temp.prev = head
            return
        
        if self.size >= 2:
            self.size += 1

            head = self.head               
            temp = Node(value)              

            head.prev.next = temp
            temp.next = head
            temp.prev = head.prev

            head.prev = temp
            self.tail = temp
            return 


    def remove(self, index):

        self.size -= 1
    
        if index == 0:
            current = self.head      
            previous = current.prev    
            infront = current.next      

            previous.next = infront
            infront.prev = previous
            self.head = infront
            return
            
        else:
            current = self.head
            for _ in range(index):
                current = current.next

            previous = current.prev     
            current = current 
            infront = current.next      
        
            previous.next = infront
            infront.prev = previous
            return


    def get_size(self):
        return self.size
        


    def index(self, item):                                                     #Searches for i in LL, returns index
        current = self.head
        counter = 0

        while current.item != item:
            counter += 1
            current = current.next
        
        return counter


    def pop(self, current):
        
        previous = current.prev
        current = current
        infront = current.next

        previous.next = infront
        infront.prev = previous
        self.size -= 1
        return


    def is_empty(self):
        return self.head == None

    def count(self):
        return self.size

    def __str__(self):
        current = self.head
        for i in range(self.size):
            print(str(current), end = " ")
            current = current.next
        print('\n')

    def __repr__(self):
        return self.__str__()

