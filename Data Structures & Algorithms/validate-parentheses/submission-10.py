class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for p in s:
            if p in pairs.values():
                if len(stack) < 1:
                    return False
                if pairs[stack[-1]] != p:
                    return False
                stack.pop(-1)
            else:
                stack.append(p)
        return len(stack) == 0