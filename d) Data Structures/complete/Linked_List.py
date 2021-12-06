class Node:                                                                 #Node Class (value and pointers)
    def __init__(self, value):
        self.item = value
        self.next = None
    
    def get_item(self):                                                     #returns the value in the node
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

#-------------------------------------------------------------------------------------------------------------
class LinkedList:                                                           #LinkedList Data Structure
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):                                                #Adds a new node to linked list
        if self.is_empty():
            self.size += 1
            self.head = Node(value)
        else:
            self.size += 1
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)


    def is_empty(self):                                                     #Returns boolean of whether list is empty or not
        return self.head == None


    def chop(self):                                                         #orphans self.head for self.head.next 
        if self.is_empty(): 
            pass
        else:
            self.head = self.head.next
            self.size -= 1


    def get_size(self):                                                     #Method returns the size of the linked list
        return self.size

    def count(self):                                                        #counts number of nodes 
        if self.head is None:
            return 0
        else:
            return self.head.count()

    def index(self, i):                                                     #Returns the node at index 'i'
        if i > self.size - 1:
            pass
        else:
            counter = 0
            current = self.head
            while current.next is not None and counter != i:
                counter += 1
                current = current.next
            return current.item
    
    def indexassign(self, i, x):
        if i > self.size - 1:
            print("Out of bounds")
        elif i < 0:
            print("Out of bounds")
        else:
            counter = 0
            current = self.head                                                         #First value
            while current.next is not None and counter != i:                            #iterates through linked list
                counter += 1
                current = current.next                                                  #Iterate all the way to this current value
            inserted_item = current.item = x                                            #This changes the node its on at i to the value of x


    def pop(self):
        prev = self.head                        #prev is the head node
        current = prev.next                     #current is the node right above 
        twoInfront = current.next               #twoInfront watches the node two infront of prev   
        while twoInfront is not None:           #if the value of twoInfront is None, that means prev holds 43 and current has the last item stored in it
            prev = prev.next                    #Now holds third to last item inside of it '43'
            current = current.next              #Now holds the last item inside of it that will be popped! '60'
            twoInfront = twoInfront.next        #Stops the loop as it holds 'None' inside of it
        print(current.item)                     #current.item stores the last item to pop and prints it here
        prev.next = twoInfront                  #I orphan the current node by putting the pointer from prev past current and pointed towards twoInfront
            


    def pop_index(self, i):                     #essentially the same function as pop
        counter = 0                             
        prev = self.head #19
        current = prev.next #24
        twoInfront = current.next #43
        while counter != i - 1:                 #only difference is I use a counter and use that to depict when to stop the loop
            prev = prev.next
            current = current.next
            twoInfront = twoInfront.next
            counter += 1
        print(current.item)
        prev.next = twoInfront

    def insert(self, item):         #I need help understanding insert. I read it and rewatched that part of class
                                    #Still dont get it though
        if self.is_empty():
            temp = Node(item)
            self.head = temp
        
    


    def __str__(self):                          #Prints out my entire linked list with nodes and pointers
        if self.is_empty():
            return "[]"
        else:
            current = self.head
            while current.next is not None:
                print(str(current.item) + ' -->', end=" ")
                current = current.next


    def __iter__(self):
        return LinkedListIterator(self.head)

class LinkedListIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current is not None:
            temp = self.current.item
            self.current = self.current.next
            return temp
        else:
            raise StopIteration



"""
class linked_list_iterator:
    def __init__(self, value):
        self.index = 0
        self.current = value

    def __next__(self):
        if self.index < self.current.count():
            current = self.current[self.index]
            self.index += 1
            return current
        else:
            raise StopIteration
"""

#I define all the constants inside main:
def main():
    #Create my linked list
    lst = LinkedList()
    lst.append(19)    #index 0
    lst.append(24)    #index 1
    lst.append(43)    #index 2
    lst.append(60)    #index 3   
    lst.append(65)    #index 4
    lst.append(84)    #index 5
    lst.append(92)    #index 6

    for i in lst:
        print(i)

    
if __name__ == "__main__":
    main()
