'''
Given a string and a set of characters, return the shortest substring containing all
the characters in the set.For example, given the string "figehaeci" and the set of 
characters {a, e, i}, you should return "aeci". If there is no substring containing 
all the characters in the set, return null.
'''

from typing import Set

def short(string: str, characters: Set[str]) -> str:
    char_queue, index_queue = [], []