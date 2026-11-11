from collections import Counter 
class Solution:
    def countDigits(self, num: int) -> int:
        nums = str(num)
        res = 0
        
        for i in range(len(nums)):
            if int(nums[i]) != 0 and num % int(nums[i]) == 0:
                res += 1
        
        return res