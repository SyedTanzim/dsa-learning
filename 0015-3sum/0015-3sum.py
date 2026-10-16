class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        i = 0

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums [i-1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j < k:
                sumOfIntegers = nums[i] + nums[j] + nums[k]

                if sumOfIntegers < 0:
                    j+=1
                elif sumOfIntegers > 0:
                    k -= 1

                elif sumOfIntegers == 0:
                    resList = [nums[i], nums[j], nums[k]]
                    res.append(resList)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return res