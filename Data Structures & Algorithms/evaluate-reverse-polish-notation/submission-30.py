class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+", "-", "/", "*"]

        for token in tokens:
            if not token in ops:
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == "+":
                    stack.append(n1 + n2)
                elif token == "-":
                    stack.append(n1 - n2)
                elif token == "*":
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))
        
        return stack[0]