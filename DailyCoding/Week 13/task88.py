'''
Implement division of two positive integers without using the division, multiplication,
or modulus operators. Return the quotient as an integer, ignoring the remainder.
'''

def divide(dividend: int, divisor: int) -> int:

    quo = 0

    while dividend > 0:
        dividend -= divisor
        if dividend >= 0:
            quo += 1

    return quo

if __name__ == "__main__":
    print(divide(1, 0))

