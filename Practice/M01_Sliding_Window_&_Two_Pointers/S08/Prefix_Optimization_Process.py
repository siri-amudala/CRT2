#leetcode 1480 Running Sum of 1d Array
from typing import List
def runningSum(nums: List[int]) -> List[int]:
    res=[0]*(len(nums))
    for i in range(len(nums)):
        curr_sum=0
        for j in range(0,i+1):
            curr_sum+=nums[j]
        res[i]=curr_sum
    return res
nums=[1,2,3,4]
print(runningSum(nums))

#optimal solution
nums=[1,2,3,4]
for i in range(1,len(nums)):
    nums[i]+=nums[i-1]+nums[i]
print(nums)

#leetcode 1732 
from typing import List
def largestAltitude(gain: List[int]) -> int:
    curr_alt=0
    max_alt=0
    for g in gain:
        curr_alt += g
        max_alt = max(curr_alt,max_alt)
    return max_alt
gain=[-5,1,5,0,-7]
print(largestAltitude(gain))