'''
Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''

def divide(dividend: int, divisor: int) -> int:

    quotient = 0

    while dividend > 0:

        dividend -= divisor
        if dividend >= 0:
            quotient += 1

    return quotient

if __name__ == "__main__":
    print(divide(5, 25))
    print(divide(3, 24))
    print(divide(2, 5))

