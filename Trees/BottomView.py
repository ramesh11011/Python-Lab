#Top View of the tree
from queue import Queue
class node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.orientation = 0

root = node(1)
root.left = node(2)
root.right = node(3)


root.left.left = node(4)
root.left.right = node(5)

root.right.right = node(6)


def BottomView(root):
    nodes = Queue()
    visited = dict()
    nodes.put(root)

    while nodes.empty() == False:
        currnode = nodes.get()
        currOrientation = currnode.orientation
        visited[currOrientation] = currnode.data

        if currnode.left != None:
            currnode.left.orientation = currOrientation - 1
            nodes.put(currnode.left)

        if currnode.right != None:
            currnode.right.orientation = currOrientation + 1
            nodes.put(currnode.right)

    for i in sorted(visited):
        print(visited[i], end=" ")


BottomView(root)