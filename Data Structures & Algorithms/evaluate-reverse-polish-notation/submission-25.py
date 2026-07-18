class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for token in tokens:
            print(stack)
            if token not in "+/-*":
                stack.append(int(token))
                continue
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