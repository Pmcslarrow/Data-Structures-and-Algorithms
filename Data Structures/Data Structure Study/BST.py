#BST.py

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        
    
def insert(root, key):

    if root is None:
        root = Node(key)
    else:
        if root.val == key:
            return Node(key)
        elif key < root.val:
            root.left = insert(root.left, key)
        elif key > root.val:
            root.right = insert(root.right, key)

    return root     


def minimum_value(root):
    while root.left is not None:
        root = root.left
    return root


def delete(root, key):
    #Search for key with recursion
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    
    elif key > root.val:
        root.right = delete(root.right, key)
    
    #Once the key is found go through the 3 cases
    else:


#THIS SHIT DOESNT ACTUALLY WORK, they lied.



        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        temp = minimum_value(root.right)

        root.key = temp.val

        print("root.right", root.right.val)
        root.right = delete(root.right, temp.val)
 
    return root



def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)    


if __name__ == '__main__':
    r = Node(50)
    insert(r, 30)
    insert(r, 20)
    insert(r, 40)
    insert(r, 70)
    insert(r, 60)
    insert(r, 80)


    delete(r, 70)
    inorder(r)
    