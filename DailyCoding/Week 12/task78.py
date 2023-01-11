'''
Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def printList(node):
	while(node != None) :
		print(node.data, end =" ")
		node = node.next

def mergeLists(first, second):

	if(first.next == None):
		first.next = second
		return first
	
	curr1 = first
	next1 = first.next
	curr2 = second
	next2 = second.next

	while(next1 != None and curr2 != None):
	
		if((curr2.data) >= (curr1.data) and (curr2.data) <= (next1.data)):

			next2 = curr2.next
			curr1.next = curr2
			curr2.next = next1
			curr1 = curr2
			curr2 = next2
		
		else:

			if(next1.next):
				next1 = next1.next
				curr1 = curr1.next
			else:
				next1.next = curr2
				return first

	return first

def merge(first, second):

	if(first == None):
		return second
	if(second == None):
		return first
	if(first.data < second.data):
		return mergeLists(first, second)
	else:
		return mergeLists(second, first)

def mergeKlists(lst, n):

        if n == 1:
            return lst[0]
        if n == 0:
            return None

        mergedlist = merge(lst[0], lst[1])

        for i in range(2, n):
            mergedlist = merge(mergedlist, lst[i])

        return mergedlist

if __name__ == "__main__":
    
    k = 4
    mlist = [i for i in range(k)]

    mlist[0] = Node(0)
    mlist[0].next = Node(2)
    mlist[0].next.next = Node(4)

    mlist[1] = Node(1)
    mlist[1].next = Node(3)
    mlist[1].next.next = Node(5)

    mlist[2] = Node(6)
    mlist[2].next = Node(7)
    mlist[2].next.next = Node(9)

    mlist[3] = Node(8)
    mlist[3].next = Node(10)

    mergedlists = mergeKlists(mlist, k)
    printList(mergedlists)