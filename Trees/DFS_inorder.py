class node :
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None 
    
root = node(1)
root.left = node(2)
root.right = node(3)

root.left.left = node(4)
root.left.right = node(5)

root.right.right = node(6)

def inorder(currNode):
    if currNode == None:
        return

    inorder(currNode.left)
    print(currNode.data , end = " ")
    inorder(currNode.right)

inorder(root)
