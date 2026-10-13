class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        i = 0
        j = i+1
        k = 1

        while j < len(nums):
            if  nums[i] >= nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                k += 1
                i += 1
                j = i + 1
        return k
        