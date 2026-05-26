class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1):
            return False
        stack = []
        open = ["[", "{", "("]
        for ch in s:
            if ch in open:
                stack.append(ch)
            else:
                print(stack)
                if (len(stack) == 0):
                    return False
                if ch == ")" and stack[-1] == "(":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0