class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
                break
            else:
                hashSet.add(i)
        return False
        