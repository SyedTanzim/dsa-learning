class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        charFreq = {}

        for char in text:
            if char == 'b' or char == 'a' or char == 'l' or char == 'o' or char == 'n':
                charFreq[char] = charFreq.get(char, 0) + 1
        
        for char in 'balon':
            if char not in charFreq:
                return 0

        maxBaloon = []

        for key in charFreq:
            if key == 'l' or key == 'o': 
                maxBaloon.append(charFreq[key] // 2)
            else:
                maxBaloon.append(charFreq[key] // 1)
        
        print(charFreq)
        print(maxBaloon)
        return min(maxBaloon)