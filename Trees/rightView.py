from queue import Queue
class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

root = node(1)
root.left = node(2)
root.right = node(3)

root.left.left = node(4)
root.left.right = node(5)

root.right.right = node(6)

def rightView(root):
    nodes = Queue()
    nodes.put(None)
    nodes.put(root)

    while nodes.empty() == False:
        currnode = nodes.get()
        
        if currnode == None:
            if nodes.empty == True:
                break

            nodes.put(None)
            continue

        if nodes.queue[0] == None:
            print(currnode.data, end=" ")

        if currnode.left != None:
            nodes.put(currnode.left)

        if currnode.right != None:
            nodes.put(currnode.right)


rightView(root)