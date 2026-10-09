from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charFreq = Counter(s)
        res = 0
        odd = False

        for key in charFreq:
            if charFreq[key] % 2 != 0:
                odd = True
            res += charFreq[key] // 2 * 2 

        if odd:
            return res+1
        return res