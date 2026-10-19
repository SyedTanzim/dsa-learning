class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k== 0:
            return 0
        sa = 0
        j = 0
        cp = 1
        for i in range(len(nums)):
            cp *= nums[i]
            while cp >= k and j <= i:
                cp /= nums[j]
                j += 1
            sa += i - j + 1
        return sa