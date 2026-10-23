class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:
            if len(stack1) < 1:
                if i == "#":
                    continue
                else:
                    stack1.append(i)
            elif i == "#":
                stack1.pop()
            else:
                stack1.append(i)
        
        for i in t:
            if len(stack2) < 1:
                if i == "#":
                    continue
                else:
                    stack2.append(i)
            elif i == "#":
                stack2.pop()
            else:
                stack2.append(i)
        
        if stack1 == stack2:
            return True
        return False