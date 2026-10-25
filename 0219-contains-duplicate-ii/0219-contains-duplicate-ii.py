class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        countMap = {}
        
        for i in range(len(nums)):
            if nums[i] in countMap:
                if abs(countMap[nums[i]] - i) <= k:
                    return True
            countMap[nums[i]] = i
        
        return False
        