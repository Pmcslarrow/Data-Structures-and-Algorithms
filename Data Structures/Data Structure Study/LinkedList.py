#LinkedList.py

# HEAD [data | pointer] --> [data | pointer] --> [data | pointer] --> NULL

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

    def insert_at_beginning(self, new_val):

        current = self.head
        new_node = Node(new_val)

        if current is None:
            self.head = new_node
            self.head.next = None
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def insert_after_node(self, pointer_node, new_val):
        new_node = Node(new_val)

        if pointer_node is None:
            return
        else:
            new_node.next = pointer_node.next
            pointer_node.next = new_node
            self.size += 1

    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        if self.isEmpty():
            self.head = new_node
            self.head.next = None
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node.next = None
            current.next = new_node
            self.size += 1


    def __str__(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next
        


if __name__ == '__main__':
    p = LinkedList()
    p.insert_at_beginning(3)
    p.insert_at_beginning(2)
    p.insert_at_beginning(1)
    p.insert_at_end(4)

    p.__str__()



    
