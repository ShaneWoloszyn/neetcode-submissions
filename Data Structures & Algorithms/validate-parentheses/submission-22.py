class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char in pMap:
                stack.append(char)
            else:
                if not stack or pMap[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0