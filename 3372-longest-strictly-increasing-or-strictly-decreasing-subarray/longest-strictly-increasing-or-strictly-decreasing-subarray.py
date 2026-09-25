class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        lengthI = 1
        lengthD = 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                lengthI += 1
                if lengthI > res:
                    res = lengthI
            else:
                lengthI = 1

            if nums[i-1] > nums[i]:
                lengthD += 1
                if lengthD > res:
                    res = lengthD
            else:
                lengthD = 1

        return res