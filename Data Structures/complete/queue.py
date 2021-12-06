class FullQueue(Exception):
    __module__ = Exception.__module__               #Just makes it look better when printing the message
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'FullQueue error has been raised'      

class EmptyQueue(Exception):
    __module__ = Exception.__module__
    def __init__(self, *args):
        
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'EmptyQueue error has been raised'
        


class queue:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.items = [None] * self.size

        self.rear = 0                  #Remove it from the back    back[. . . . .]front
        self.front = 0                 #Add to the front pointer which starts at the back and moves towards the front


    def enqueue(self, item):
        if self.isFull():
            raise FullQueue('Can\'t add items in a full queue!')
        else:
            self.items[self.front] = item
            self.front = self.bump(self.front)
            self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueue('Can\'t remove items in empty queue!')
        else:
            del self.items[self.rear]
            self.rear = self.bump(self.rear)
            self.count -= 1

    def bump(self, index):
        return (index+1) % self.size

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __str__(self):
        for i in self.items:
            print(i, end=" ")

#-------------------------------------------------------------------------
Q = queue(5)
Q.dequeue()
Q.__str__()
