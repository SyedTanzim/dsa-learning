class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        lengthI = 1
        lengthD = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                lengthI += 1
                if lengthI > increasing:
                    increasing = lengthI
            else:
                lengthI = 1

            if nums[i-1] > nums[i]:
                lengthD += 1
                if lengthD > decreasing:
                    decreasing = lengthD
            else:
                lengthD = 1

        return max(increasing, decreasing)