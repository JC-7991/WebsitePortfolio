'''
Given a mapping of digits to letters (as in a phone number), 
and a digit string, return all possible letters the number could 
represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” 
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

from typing import Dict, List

def mappings(convert: Dict[str, str], string: str, result: List[str] = []) -> List[str]:

    if not string:
        return result

    if not result:
        for elem in convert[string[0]]:
            result.append(elem)
        return mappings(convert, string[1:], result)

    temp = []

    for part in result:
        for elem in convert[string[0]]:
            temp.append(part + elem)
    
    result[:] = temp

    return mappings(convert, string[1:], result)

if __name__ == "__main__":

    print(mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23", []))
    print(mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "32", []))
    print(mappings({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "222", []))