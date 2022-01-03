#Implementation of a stack w/ python list
#LIFO

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def top(self):
        return self.stack[-1]

    def push(self, val):
        self.stack.append(val)
        self.size += 1

    def pop(self):
        print(self.stack[-1])
        del self.stack[-1]

    def flush(self):
        for i in range(self.size):
            self.pop()

p = Stack()
p.push("a")
p.push("b")
p.push("c")
p.flush()