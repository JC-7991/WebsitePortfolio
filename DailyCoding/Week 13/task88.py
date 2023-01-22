'''
Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''

def divide(dividend, divisor):
 
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)
 
    quotient = 0

    while(dividend >= divisor):
        dividend -= divisor
        quotient += 1
 
    if sign == -1:
        quotient = -quotient
 
    return quotient
 
if __name__ == "__main__":

    print(divide(25, 5))
    print(divide(43, -8))
    print(divide(100, 3))