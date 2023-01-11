'''
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

def mergeInv(ints):

    ints.sort()
    stack = []
    stack.append(ints[0])

    for i in ints[1:]:

        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    for i in range(len(stack)):
        print(stack[i], end = " ")

if __name__ == "__main__":

    arr = [[1, 3], [5, 8], [4, 10], [20, 25]]
    mergeInv(arr)