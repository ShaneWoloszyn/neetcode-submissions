class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []

        def search(openedP, closedP):
            if openedP == closedP == n:
                res.append("".join(stack))
                return
            
            if openedP < n:
                stack.append("(")
                search(openedP + 1, closedP)
                stack.pop()

            if openedP > closedP:
                stack.append(")")
                search(openedP, closedP + 1)
                stack.pop()
        
        search(0, 0)
        return res
    