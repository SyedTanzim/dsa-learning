class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        maxSum = 0
        val = 0

        for index, num in enumerate(nums):
            val += num

            if num <= nums[index-1]:
                val = num

            if maxSum < val:
                maxSum = val  
        
        return maxSum