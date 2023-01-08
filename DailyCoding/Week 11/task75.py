'''
Given an array of numbers, find the length of the 
longest increasing subsequence in the array. The 
subsequence does not necessarily have to be contiguous.
For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''

global maximum
 
def lengthX(arr, n):

    global maximum
 
    if n == 1:
        return 1

    end = 1
 
    for i in range(1, n):
        res = lengthX(arr, i)
        if arr[i - 1] < arr[n - 1] and res+1 > end:
            end = res + 1
 
    maximum = max(maximum, end)
 
    return end
 
 
def lengthY(arr):
 
    global maximum
    n = len(arr)
    maximum = 1
    
    lengthX(arr, n)
 
    return maximum
 
if __name__ == "__main__":
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    n = len(arr)
    print ("Length:", lengthY(arr))