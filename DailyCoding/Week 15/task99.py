'''
Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.
For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is
[1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.
'''

def findLongest(arr, n):

    ans = 0
    cnt = 0
    arr.sort()

    x = []
    x.append(arr[0])

    for i in range(1, n):
        if(arr[i] != arr[i - 1]):
            x.append(arr[i])
