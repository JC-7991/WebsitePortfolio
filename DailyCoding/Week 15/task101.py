'''
Given an even number (greater than 2), return two prime numbers whose sum will be equal
to the given number.
A solution will always exist. See Goldbach's conjecture.
Example:
Input: 4
Output: 2 + 2 = 4 
If there are more than one solution possible, return the
lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
if a < c or a==c and b < d.
'''

def generate(n, isPrime):
    
    isPrime[0] = isPrime[1] = False
    for i in range(2, n + 1):
        isPrime[i] = True