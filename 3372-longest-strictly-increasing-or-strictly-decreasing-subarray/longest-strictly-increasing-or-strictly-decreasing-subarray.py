class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestIncreasingSubarray = 1
        longestDecreasingSubarray = 1
        length = 1

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                length = 1
            else:
                length += 1
                if length > longestIncreasingSubarray:
                    longestIncreasingSubarray = length

        longestDecreasingSubarray = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                print(nums[i-1])
                length = 1
            else:
                length += 1
                if length > longestDecreasingSubarray:
                    longestDecreasingSubarray = length
        
        return max(longestIncreasingSubarray, longestDecreasingSubarray)