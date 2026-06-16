class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pMap = {")":"(", "}":"{","]":"["}

        for i in range(len(s)):
            if s[i] in pMap:
                if stack and stack[-1] == pMap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return len(stack) == 0
