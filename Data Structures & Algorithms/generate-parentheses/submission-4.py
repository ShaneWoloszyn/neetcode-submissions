class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def search(openedP, closedP, cur):
            if openedP == closedP == n:
                res.append(cur)
                return
            
            if closedP < openedP:
                cur += ")"
                search(openedP, closedP + 1, cur)
                cur = cur[0:len(cur) - 1]
            
            if openedP <= n:
                cur += "("
                search(openedP + 1, closedP, cur)

        search(0, 0, "")

        return res