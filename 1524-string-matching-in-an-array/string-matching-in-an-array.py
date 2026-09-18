class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        res = []
        
        for i in range(len(words)):
            word = words[i]
            for j in range(len(words)):
                if word in words[j] and word != words[j]:
                    if word not in res:
                        res.append(word)
        return res