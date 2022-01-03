class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        return self.queue.pop(0)

if __name__ == '__main__':
    p = Queue()
    p.enqueue(5)
    p.enqueue(4)
    p.enqueue(3)
    p.enqueue(2)
    p.enqueue(1)
    print(p.dequeue())

