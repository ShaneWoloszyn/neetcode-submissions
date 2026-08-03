class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "/", "*"}
        for ops in tokens:
            if ops not in operations:
                stack.append(int(ops))
                continue
            print(stack)
            n2 = stack.pop()
            n1 = stack.pop()
            if ops == "+":
                stack.append(n1 + n2)
            elif ops == "-":
                stack.append(n1 - n2)
            elif ops == "*":
                stack.append(n1 * n2)
            else:
                stack.append(int(n1 / n2))

        return stack[-1]