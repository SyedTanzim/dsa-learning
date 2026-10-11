class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            j = i+1

            if nums[i] != 0:
                continue
            
            while j < len(nums):
                if nums[j] == 0:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        
        return nums