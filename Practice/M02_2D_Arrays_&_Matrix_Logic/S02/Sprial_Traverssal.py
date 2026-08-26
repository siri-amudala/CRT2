#leetcode question 54
from typing import List
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    rows,cols=len(matrix),len(matrix[0])
    top,bottom=0,rows-1
    left,right=0,cols-1
    res=[]
    while top<=bottom and left<=right:
        for col in range(left,right+1):
            res.append(matrix[top][col])
        top+=1
        for row in range(top,bottom+1):
            res.append(matrix[row][right])
        right-=1
        if top<=bottom:
            for col in range(right,left-1,-1):
                res.append(matrix[bottom][col])
            bottom-=1
        if left<=right:
            for row in range(bottom,top-1,-1):
                res.append(matrix[row][left])
            left+=1
    return res

row=[[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(row))
