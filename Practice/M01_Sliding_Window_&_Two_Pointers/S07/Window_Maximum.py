#leetcode 1763 Longest Nice Substring
from typing import List
def longestNiceSubstring(s: str) -> str:
    if len(s) < 2:
        return ""
    
    char_set = set(s)
    
    for i, c in enumerate(s):
        if c.swapcase() not in char_set:
            left = longestNiceSubstring(s[:i])
            right = longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
    return s
s="YazaAay"
print(longestNiceSubstring(s))

#leetcode 1652 defuse the bomb
from typing import List
def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    res = [0] * n
    if k == 0:
        return res
    if k > 0:
        left = 1
        right = k
    else:
        left = n + k  
        right = n - 1
    current_sum = sum(code[i % n] for i in range(left, right + 1))
    for i in range(n):
        res[i] = current_sum
        current_sum -= code[left % n]
        left += 1
        right += 1
        current_sum += code[right % n]
      
    return res
    
