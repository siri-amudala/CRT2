#leetcode 867 
from typing import List
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])

    res = [[0] * m for _ in range(n)]

    for r in range(m):
        for c in range(n):
            res[c][r] = matrix[r][c]

    return res
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))
