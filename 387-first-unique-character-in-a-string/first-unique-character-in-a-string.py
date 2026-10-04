class Solution:
    def firstUniqChar(self, s: str) -> int:
        charFreq = {}

        for char in s:
            charFreq[char] = charFreq.get(char,0) + 1
        
        index = 0

        for char in s:
            if charFreq.get(char) == 1:
                return index
            index += 1
        return -1