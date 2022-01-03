#Stack_w_LL.py

class Node:
    def __init__(self, key):
        self.val = key
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    def isEmpty(self):
        return self.size == 0


    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        if self.isEmpty():
            self.head = new_node
            self.head.next = None
            self.size += 1
        else:
            self.size += 1
            current = self.head
            while current.next is not None:
                current = current.next
            new_node.next = None
            current.next = new_node

    def delete_end_node(self):
        pass


    def __str__(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next


class Stack(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def push(self, val):
        self.insert_at_end(val)

    def pop(self):
        self.delete_end_node()


if __name__ == '__main__':
    p = Stack()
    p.push(1)
    p.push(2)
    p.push(3)
    p.delete_end_node()
    p.__str__()


    
