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
    
    str1= None
    end1 = None
    str = 0
    end = 0
    temp_set = set()

    while end < len(string):

        temp_set.add(string[end])

        if chars.issubset(temp_set):
            while chars.issubset(temp_set):
                temp_set.discard(string[str])
                str += 1
            str -= 1
            if end1 is None:
                str1 = str
                end1 = end
            elif end1 - str1 > end-str:
                str1 = str
                end1 = end

            str = end
            end -= 1
            temp_set = set()

        end += 1

    return string[str1:end1+1] if str1 is not None else None