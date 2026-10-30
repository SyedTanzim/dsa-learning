class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        start = 0
        end = 0
        currentMax = nums[0]
        currentMin = nums[-1]

        for i in range(1, len(nums)):
            if currentMax < nums[i]:
                currentMax = nums[i]
            elif currentMax > nums[i]:

                end = i

        for i in range(len(nums)-2, -1, -1):
            if currentMin > nums[i]:
                currentMin = nums[i]
            elif currentMin < nums[i]:
                start = i

        print(start,end)
        if start == 0 and end == 0:
            return 0
        return end - start + 1