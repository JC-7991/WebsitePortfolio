# Given the head of a singly linked list, reverse it in-place.

class ListNode:

    def __init__(self, x):

        self.val = x
        self.next = None

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return

        curr = head
        prev = None

        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt