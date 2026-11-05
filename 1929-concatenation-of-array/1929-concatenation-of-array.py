class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = 2 * len(nums)
        ansArray = [0] * n

        for i in range(len(nums)):
            ansArray[i] = nums[i]
            ansArray[i + len(nums)] = nums[i]
        return ansArray