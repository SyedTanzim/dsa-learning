from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        freqCount = Counter(nums)
        print(freqCount)
        res = []
        
        for _ in range(k):
            maxKey = max(freqCount, key=freqCount.get)
            res.append(maxKey)
            del freqCount[maxKey]
        return res