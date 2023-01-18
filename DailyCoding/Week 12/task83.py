'''
Invert a binary tree.
For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
'''

class Node:

   def __init__(self, data):

      self.left = None
      self.right = None
      self.data = data

   def printTree(self):

        if self.left:
            self.left.printTree()

        print( self.data, end = ' ')

        if self.right:
            self.right.printTree()

class Solution:

    def invertTree(self, root):

        if root == None:
            return
        root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
        return root

if __name__ == "__main__":

    Tree = Node(10)
    Tree.left = Node(20)
    Tree.right = Node(30)
    Tree.left.left = Node(40)
    Tree.right.right = Node(50)

    print('Initial Tree:', end = ' ' )
    Tree.printTree()
    Solution().invertTree(root = Tree)
    print('\nInverted Tree:', end = ' ')
    Tree.printTree()