
#leetcode 209. Minimum Size Subarray Sum
from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    left=0
    min_len=float("inf")
    cur_sum=0
    for right in range(len(nums)):
        cur_sum +=nums[right]
        while cur_sum>=target:
            min_len=min(min_len,right-left+1)
            cur_sum-=nums[left]
            left+=1
    return 0 if min_len==float("inf") else min_len
        
target=7
nums=[2,3,1,2,4,3]
print(minSubArrayLen(target,nums))




#leetcode question 713
from typing import List
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    left=0
    c=0
    p=1
    for right in range(len(nums)):
        p*=nums[right]
        while p>=k:
            p//=nums[left]
            left+=1
        c+=(right-left+1)
    return c
nums=[10,5,2,6]
k=100
print(numSubarrayProductLessThanK(nums,k))



#904 fruit into baskets
from typing import List
def totalFruit(fruits: List[int]) -> int:
    count={}
    left,ans=0,0
    for right in range(len(fruits)):
        count[fruits[right]]=count.get(fruits[right],0)+1
        while len(count) >2:
            count[fruits[left]]-=1
            if count[fruits[left]]==0:
                del count[fruits[left]]
            left+=1
        ans=max(ans,right-left+1)
    return ans
fruits=[1,2,1]
print(totalFruit(fruits))

