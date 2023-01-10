'''
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

def mergeIntervals(intervals):

    intervals.sort()
    stack = []
    stack.append(intervals[0])

    for i in intervals[1:]:
        
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    print("Merged intervals:", end = " ")

    for i in range(len(stack)):
        print(stack[i], end=" ")

if __name__ == "__main__":
    arr = [[1, 3], [5, 8], [4, 10], [20, 25]]
    mergeIntervals(arr)