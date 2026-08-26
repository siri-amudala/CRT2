
# leetcode question 59
from typing import List
def generateMatrix(n: int) -> List[List[int]]:
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    res = [[0] * n for _ in range(n)]

    while top <= bottom and left <= right:
        # left -> right
        for col in range(left, right + 1):
            res[top][col] = num
            num += 1
        top += 1

        # top -> bottom
        for row in range(top, bottom + 1):
            res[row][right] = num
            num += 1
        right -= 1

        # right -> left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                res[bottom][col] = num
                num += 1
            bottom -= 1

        # bottom -> top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                res[row][left] = num
                num += 1
            left += 1

    return res
columns=3
print(generateMatrix(columns))