#tree.py
class Node:
    def __init__(self, value):
        self.item = value
        self.left = None
        self.right = None
    
    def get_node(self):
        return self.item