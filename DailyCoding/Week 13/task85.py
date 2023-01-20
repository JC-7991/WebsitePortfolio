'''
Given three 32-bit integers x, y, and b, 
return x if b is 1 and y if b is 0, using only 
mathematical or bit operations. You can assume b 
can only be 1 or 0.
'''

def swicth(x, y, b):
    return (x * b) + (y * abs(b - 1))

if __name__ == "__main__":
    print(swicth(6, 8, 1))
    print(swicth(6, 8, 0))