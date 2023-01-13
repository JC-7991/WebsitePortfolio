'''
Given an array of integers, write a function to determine 
whether the array could become non-decreasing by modifying at most 1 element.
For example, given the array [10, 5, 7], you should return true, 
since we can modify the 10 into a 1 to make the array non-decreasing.
Given the array [10, 5, 1], you should return false, since we can't 
modify any one element to get a non-decreasing array.
'''

def modify(arr, n):
 
    modify = 0

    if(arr[n - 1] >= arr[n - 2]):
        arr[n - 1] = arr[n - 2] - 1
        modify += 1

    if(arr[0] <= arr[1]):
        arr[0] = arr[1] + 1
        modify += 1

    for i in range(n - 2, 0, -1):
 
        if(arr[i - 1] <= arr[i] and arr[i + 1] <= arr[i]) or \
            (arr[i - 1] >= arr[i] and arr[i + 1] >= arr[i]):
 
            arr[i] = (arr[i - 1] + arr[i + 1]) // 2

            modify += 1

            if(arr[i] == arr[i - 1] or arr[i] == arr[i + 1]):
                return False

    if(modify > 1):
        return False
 
    return True
 
if __name__ == "__main__":

    arr = [10, 5, 7]
    n = len(arr)

    if(modify(arr, n)):
        print("Yes.")
    else:
        print("No.")