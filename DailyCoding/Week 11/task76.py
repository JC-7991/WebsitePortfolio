'''
You are given an N by M 2D matrix of lowercase letters. 
Determine the minimum number of cols that can be removed to 
ensure that each row is ordered from top to bottom lexicographically. 
That is, the letter at each column is lexicographically later as you go
down each row. It does not matter whether each row itself is 
ordered lexicographically.
For example, given the following table:
cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:
ca
df
gi
So your function should return 1, since we only needed to remove 1 column.
As another example, given the following table:
abcdef
Your function should return 0, since the rows are already ordered (there's only one row).
As another example, given the following table:
zyx
wvu
tsr
Your function should return 3, since we would need to remove all the cols to order it.
'''

from typing import List

def colRemove(matrix: List[List[int]]) -> int:

    rows = len(matrix)
    cols = len(matrix[0])
    cnt = 0

    for column in range(cols):
        for row in range(rows - 1):

            if matrix[row][column] > matrix[row + 1][column]:
                cnt += 1
                break

    return cnt

if __name__ == "__main__":

    print(colRemove(["cba", "daf", "ghi"]))
    print(colRemove(["abcdef"]))
    print(colRemove(["zyx", "wvu", "tsr"]))