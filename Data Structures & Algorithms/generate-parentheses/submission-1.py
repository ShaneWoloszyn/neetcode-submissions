class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def search(openedP, closedP):
            if openedP == closedP == n:
                res.append("".join(subset))
                return
            
            if openedP < n:
                subset.append("(")
                search(openedP + 1, closedP)
                subset.pop()
            
            if openedP > closedP:
                subset.append(")")
                search(openedP, closedP + 1)
                subset.pop()
        
        search(0, 0)
        return res