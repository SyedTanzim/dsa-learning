class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        value = 0
        for i in range(len(nums)):
            value += nums[i]
            nums[i] = value
        return nums 

        