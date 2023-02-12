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

def shortest(string, chars: set):
    
    final_start= None
    final_end = None

    start, end = 0, 0
    temp_set = set()
    while end < len(string):

        temp_set.add(string[end])

        if chars.issubset(temp_set):
            while chars.issubset(temp_set):
                temp_set.discard(string[start])
                start += 1
            start -= 1
            if final_end is None:
                final_start = start
                final_end = end
            elif final_end - final_start > end-start:
                final_start = start
                final_end = end

            start = end
            end -= 1
            temp_set = set()


        end += 1

    return string[final_start:final_end+1] if final_start is not None else None