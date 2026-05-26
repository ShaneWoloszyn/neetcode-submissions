class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n1 = 0
        n2 = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                n1 = stack[-1]
                stack.pop()
                n2 = stack[-1]
                stack.pop()
                stack.append(n1 + n2)
            elif tokens[i] == "-":
                n1 = stack[-1]
                stack.pop()
                n2 = stack[-1]
                stack.pop()
                stack.append(n2 - n1)
            elif tokens[i] == "*":
                n1 = stack[-1]
                stack.pop()
                n2 = stack[-1]
                stack.pop()
                stack.append(n1 * n2)
            elif tokens[i] == "/":
                n1 = stack[-1]
                stack.pop()
                n2 = stack[-1]
                stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(tokens[i]))
        return stack[0]