#leetcode question 1493
from typing import List
def longestSubarray(nums: List[int]) -> int:
    left=0
    count_of_zero=0
    max_length=0
    for right in range(len(nums)):
        if nums[right]==0:
            count_of_zero+=1
        while count_of_zero > 1:
            if nums[left] == 0:
                count_of_zero -= 1
            left += 1
        
        max_length = max(max_length, right - left)
        
    return max_length
nums=[1,1,0,1,1,1,0,1,1]
print(longestSubarray(nums))


#leetcode question 1004
from typing import List
def longestOnes(nums: List[int], k: int) -> int:
    left = 0
    zero_count = 0
    max_len = 0
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
        
    return max_len
nums = [1,1,0,0,1,1,1,0,1]
k = 2
print(longestOnes(nums, k))

