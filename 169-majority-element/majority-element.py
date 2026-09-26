class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        element = 0 

        for i in nums:
            if count == 0:
                count += 1
                element = i
            elif element == i:
                count += 1
            else:
                count -= 1

        return element
