class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def search(opened, closed, cur):
            if opened == closed == n:
                res.append(cur)
                return
            
            if opened < n:
                cur += "("
                search(opened + 1, closed, cur)
                cur = cur[0:len(cur) - 1]
            
            if closed < opened:
                cur += ")"
                search(opened, closed + 1, cur)

        search(0, 0, "")
        return res