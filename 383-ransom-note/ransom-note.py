from collections import Counter

class Solution:
    def canConstruct(self, string1: str, string2: str) -> bool:
        countStr1 = Counter(string1)
        countStr2 = Counter(string2)

        print(countStr1)
        print(countStr2)

        for key in countStr1:
            target = countStr1[key]
            value = countStr2[key]
            
            if target > value:
                return False
        
        return True