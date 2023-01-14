'''
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
'''

class Node:
    def __init__(self, data):

        self.data= data
        self.left = None
        self.right = None
        self.visited = False

def find(root, level, max, res):
 
    if(root != None):

        level += 1
        find(root.left, level, max, res)
        if (level > max[0]):
            res[0] = root.data
            max[0] = level
         
        find(root.right, level, max, res)

def deepestNode(root) :
 
    res = [-1]
    max = [-1]
    find(root, 0, max, res)
    return res[0]
                         
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    print(deepestNode(root))