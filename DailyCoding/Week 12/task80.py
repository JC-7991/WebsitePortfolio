'''
Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
'''

class newNode:
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None
        self.visited = False

def find(root, level, maxLevel, res):
 
    if(root != None):

        level += 1
        find(root.left, level, maxLevel, res)
        if (level > maxLevel[0]):
            res[0] = root.data
            maxLevel[0] = level
         
        find(root.right, level, maxLevel, res)

def deepestNode(root) :
 
    res = [-1]
    maxLevel = [-1]
    find(root, 0, maxLevel, res)
    return res[0]
                         
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.right.left = newNode(5)
    root.right.right = newNode(6)
    root.right.left.right = newNode(7)
    root.right.right.right = newNode(8)
    root.right.left.right.left = newNode(9)
    print(deepestNode(root))