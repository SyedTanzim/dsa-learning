class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            for j in range(len(nums)-1, 0, -1):
                k = i + 1
                l = j - 1

                while k < l:
                    totalSum = nums[i] + nums[j] + nums[k] + nums[l]
                
                    if totalSum == target:
                        resList =  [ nums[i], nums[j], nums[k], nums[l] ] 
                        if resList not in res:
                            res.append(resList)
                        k += 1
                        l -= 1
                    elif totalSum > target:
                        l -= 1
                    else:
                        k += 1
        return res