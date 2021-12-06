class BST:
    def __init__(self, value=None):
        self.item = value
        self.left = None
        self.right = None

    def insert(self, value):

        if value == self.item:
            return

        if value < self.item:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        if value > self.item:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


    def printPreorder(self, root):
 
        if root:
    
            # First print the data of node
            print(root.item),
    
            # Then recur on left child
            self.printPreorder(root.left)
    
            # Finally recur on right child
            self.printPreorder(root.right)


    def printPostorder(self, root):
    
        if root:
    
            # First recur on left child
            self.printPostorder(root.left)
    
            # the recur on right child
            self.printPostorder(root.right)
    
            # now print the data of node
            print(root.item)


    def printInorder(self, root):
 
        if root:
    
            # First recur on left child
            self.printInorder(root.left)
    
            # then print the data of node
            print(root.item)
    
            # now recur on right child
            self.printInorder(root.right)


tree = BST(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
