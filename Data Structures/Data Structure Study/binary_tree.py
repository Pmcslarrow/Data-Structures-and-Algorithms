class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def inorder(temp):
 
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.val,end = " ")
    inorder(temp.right)

def insert(root, new_value):
    new_node = Node(new_value)

    if (not root):
        root = Node(new_value)
    
    checklist = []
    checklist.append(root)

    while (len(checklist)):

        temp_node = checklist[0]
        checklist.pop(0)

        if (not root.left):
            root.left = new_node
            break
        else:
            checklist.append(root.left)

        
        if (not root.right):
            root.right = new_node
            break
        else:
            checklist.append(root.right)


def delete_deepest_node(root, d_node):
    q = []
    q.append(root)

    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        #checks if right exist, and if it is the deepest node
        #If it is, make it none
        #if it isn't, append it to the list to start it as next node
        if temp.right is not None:
            if temp.right is d_node:
                temp = None
                return
            else:
                q.append(temp.right)

        if temp.left is not None:
            if temp.left is d_node:
                temp = None
                return
            else:
                q.append(temp.left)


        
if __name__ == '__main__':
    root = Node(10)
    insert(root, 5)
    insert(root, 13)
    inorder(root)


        


            