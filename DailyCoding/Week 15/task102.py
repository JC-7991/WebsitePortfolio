'''
Given a list of integers and a number K, return which contiguous elements of the list
sum to K.
For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].
'''

def contigElements(nums, k):
    
    arr = []
    sum = 0
    i = 0

    while i < len(nums) and not sum == k:

        if nums[i] + sum <= k:
            sum += nums[i]
            arr.append(nums[i])
            i += 1

        else:
            if arr:
                num = arr.pop(0)
                sum -= num
            else:
                i += 1
    
    return arr