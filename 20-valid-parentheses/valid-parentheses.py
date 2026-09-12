class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        if len(s) < 2:
            return False

        if  s[0] == ")" or s[0] ==  "}" or s[0] == "]":
            return False
        
        for i in range(len(s)):
            if ( s[i] == "(" or s[i] == "[" or s[i] == "{" ):
                stack.append(s[i])

            elif ( len(stack) > 0 and s[i] == ")" and stack[-1] == "(" ):
                stack.pop()
            elif ( len(stack) > 0 and s[i] == "}" and stack[-1] == "{" ):
                stack.pop()
            elif ( len(stack) > 0 and s[i] == "]" and stack[-1] == "[" ):
                stack.pop()
            else:
                return False
        
        if len(stack) > 0:
            return False
        else:
            return True