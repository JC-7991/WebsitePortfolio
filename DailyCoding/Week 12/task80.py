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

def find(root, lvl, max, res):
 
    if(root != None):

        lvl += 1
        find(root.left, lvl, max, res)

        if (lvl > max[0]):
            res[0] = root.data
            max[0] = lvl
         
        find(root.right, lvl, max, res)

def deepest(root) :
 
    res = [-1]
    max = [-1]
    find(root, 0, max, res)
    return res[0]
                         
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print(deepest(root))