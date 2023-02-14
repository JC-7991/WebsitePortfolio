'''
Determine whether a doubly linked list is a palindrome. What if it's singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.ptr = None
 
 
def isPD(head):
 
    slow = head
    stack = []
    ispalin = True

    while slow != None:
        stack.append(slow.data)
        slow = slow.ptr

    while head != None:
 
        i = stack.pop()

        if head.data == i:
            ispalin = True
        else:
            ispalin = False
            break

        head = head.ptr
 
    return ispalin

if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(3)
    six = Node(2)
    seven = Node(1)

    one.ptr = two
    two.ptr = three
    three.ptr = four
    four.ptr = five
    five.ptr = six
    six.ptr = seven
    seven.ptr = None

    result = isPD(one)
    
    print("isPalindrome:", result)