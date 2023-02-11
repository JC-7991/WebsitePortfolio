'''
Given a string and a set of characters, return the shortest substring containing all
the characters in the set.For example, given the string "figehaeci" and the set of 
characters {a, e, i}, you should return "aeci". If there is no substring containing 
all the characters in the set, return null.
'''

def short(string, chars):

    if chars.issubset(set(string)):

        left = short(string[1:], chars)
        right = short(string[:-1], chars)

        if left and right:
            return left if len(left) < len(right) else right
        
        elif left:
            return left
        elif right:
            return right
        else:
            return string

    return None