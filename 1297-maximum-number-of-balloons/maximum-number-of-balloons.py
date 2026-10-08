class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        charFreq = {}

        for char in text:
            if char in "balloon":
                charFreq[char] = charFreq.get(char, 0) + 1
        
        return min(
            charFreq.get('b', 0),
            charFreq.get('a', 0),
            charFreq.get('l', 0) // 2,
            charFreq.get('o', 0) // 2,
            charFreq.get('n', 0),
        )