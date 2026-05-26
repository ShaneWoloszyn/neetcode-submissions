class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "{", "["]
        stack = []
        for p in s:
            if p in open:
                stack.append(p)
            elif len(stack) == 0:
                return False
            elif p == ")":
                if stack[-1] != "(":
                    return False
                stack.pop()
            elif p == "}":
                if stack[-1] != "{":
                    return False
                stack.pop()
            elif p == "]":
                if stack[-1] != "[":
                    return False
                stack.pop()
        print(stack)
        if len(stack) != 0:
            return False
        return True