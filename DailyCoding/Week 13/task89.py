'''
Determine whether a tree is a valid binary search tree.
A binary search tree is a tree with two children, left and right,
and satisfies the constraint that the key in the left child must 
be less than or equal to the root and the key in the right child 
must be greater than or equal to the root.
'''

class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def maxValue(node):

    if node is None:
        return 0
     
    leftMax = maxValue(node.left)
    rightMax = maxValue(node.right)
     
    value = 0

    if leftMax > rightMax:
        value = leftMax
    else:
        value = rightMax
     
    if value < node.data:
        value = node.data
     
    return value
     
def minValue(node):

    if node is None:
        return 1000000000
     
    leftMax = minValue(node.left)
    rightMax = minValue(node.right)
     
    value = 0

    if leftMax < rightMax:
        value = leftMax
    else:
        value = rightMax
     
    if value > node.data:
        value = node.data
     
    return value

def isBST(node):

    if node is None:
        return True

    if(node.left is not None and maxValue(node.left) > node.data):
        return False

    if(node.right is not None and minValue(node.right) < node.data):
        return False

    if(isBST(node.left) is False or isBST(node.right) is False):
        return False
     
    return True
 
if __name__ == "__main__":

    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    if isBST(root) is True:
        print("Is a valid BST.")
    else:
        print("Is not a valid BST.")