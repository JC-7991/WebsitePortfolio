'''
Given a tree, find the largest tree/subtree that is a BST.
Given a tree, return the size of the largest tree/subtree that is a BST.
'''

IMIN = -2147483648
IMAX = 2147483647

def largestBST(root):

    if root == None:
        return IMAX,IMIN,0

    if(root.left == None and root.right == None):
        return root.data,root.data,1
         
    left = largestBST(root.left)
    right = largestBST(root.right)
    ans = [0,0,0]
         
    if left[1] < root.data and right[0] > root.data:

        ans[0] = min(left[0], right[0], root.data)
        ans[1] = max(right[1], left[1], root.data)
        ans[2] = 1 + left[2] + right[2]
        return ans
 
    ans[0] = IMIN
    ans[1] = IMAX
    ans[2] = max(left[2], right[2])

    return ans
 
def largestBSTUtil(root):
    return largestBST(root)[2]

import sys
sys.setrecursionlimit(1000000)
from collections import deque

class newNode:
    
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
 
if __name__ == "__main__":

    root = newNode(50)
    root.left = newNode(75)
    root.right = newNode(45)
    root.left.left = newNode(40)

    print("The size of the largest BST is",largestBSTUtil(root))