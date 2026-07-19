class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pMap = {"(":")", "{":"}", "[":"]"}

        for char in s:
            if char in pMap:
                stack.append(char)
            else:
                if not stack or pMap[stack.pop()] != char:
                    return False
        
        return len(stack) == 0