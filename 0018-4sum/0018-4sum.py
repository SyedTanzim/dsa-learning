class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(len(nums)-1, i, -1):
                k = i+1
                l = j-1

                if j < len(nums) - 1 and nums[j] == nums[j+1]:
                    continue

                totalSum = 0

                while k < l:
                    totalSum = nums[i] + nums[j] + nums[k]+ nums[l]

                    if totalSum == target:
                        res.append( [ nums[i], nums[j], nums[k], nums[l] ] )
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1

                    elif totalSum < target:
                        k += 1
                        while k < l and nums[k] == nums[k-1]:
                            k += 1
                    else:
                        l -= 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                
        return res
