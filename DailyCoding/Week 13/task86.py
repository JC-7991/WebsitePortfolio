'''
Given a string of parentheses, write a function 
to compute the minimum number of parentheses to be 
removed to make the string valid (i.e. each open parenthesis is eventually closed).
For example, given the string "()())()", you should return 1. 
Given the string ")(", you should return 2, since we must remove all of them.
'''

class Solution:

    def validRemove(self, S):

        S, stack = list(S), []

        for i, c in enumerate(S):

            if c == ")":
                if stack: stack.pop()
                else: S[i] = ""

            elif c == "(": stack.append(i)
            
        for i in stack: S[i] = ""
        return "".join(S)