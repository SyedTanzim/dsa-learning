class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        realDiff = None
        closest = None

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:

                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum == target:
                    return currentSum
                    
                currentDiff = abs(currentSum - target)

                if realDiff == None:
                    realDiff = currentDiff
                    closest = currentSum
                elif currentDiff < realDiff:
                    realDiff = currentDiff
                    closest = currentSum

                if currentSum < target:
                    j += 1
                elif currentSum > target:
                    k -= 1
            
        return closest