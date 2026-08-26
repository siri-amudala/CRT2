#leetcode question 74
from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, (m * n) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // n][mid % n]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False 
m,n=3,4
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
print(searchMatrix(matrix, target))

#leetcode 240
from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1
    
    while row < rows and col >= 0:
        current = matrix[row][col]
        
        if current == target:
            return True
        elif current > target:
            col -= 1  
        else:
            row += 1  
            
    return False
rows, cols = 3, 4
matrix = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]]
target = 5
print(searchMatrix(matrix, target))