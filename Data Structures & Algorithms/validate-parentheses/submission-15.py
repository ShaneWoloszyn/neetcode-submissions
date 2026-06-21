class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"(":")", "{":"}", "[":']'}
        stack = []

        for p in s:
            print(p)
            if p in pairs:
                stack.append(p)
            else:
                if len(stack) == 0 or pairs[stack.pop()] != p:
                    return False
        
        return len(stack) == 0