class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "-", "/"]

        for token in tokens:
            ans = 0
            if token in operators:
                first = stack[-2]
                second = stack[-1]
                stack.pop()
                stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
            else:
                stack.append(int(token))
            print(stack)
        return int(stack[0])