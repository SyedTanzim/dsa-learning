class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
    
        res = [0] * len(nums)
        i = 0
        j = len(nums) - 1
        index = len(nums) - 1

        while i <= j:
            if i == j:
                res[index] = nums[i] * nums[i]
                break
            if nums[i] * nums[i] < nums[j] * nums[j]:
                res[index] = nums[j] * nums[j]
                j -= 1
                index -= 1
            elif nums[i] * nums[i] > nums[j] * nums[j]:
                res[index] = nums[i] * nums[i]
                i += 1
                index -= 1
            elif nums[i] * nums[i] == nums[j] * nums[j]:
                res[index] = nums[i] * nums[i]
                index -= 1
                res[index] = nums[j] * nums[j]
                index -= 1
                i += 1
                j -= 1
        return res
        