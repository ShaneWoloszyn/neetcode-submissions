class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "/", "*"}

        for tok in tokens:
            if tok not in operations:
                stack.append(int(tok))
                continue
            
            x = stack.pop()
            y = stack.pop()
        
            if tok == "+":
                stack.append(x + y)
            elif tok == "-":
                stack.append(y - x)
            elif tok == "/":
                stack.append(int(y / x))
            else:
                stack.append(x * y)
        return stack[0]