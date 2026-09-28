class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        cur = {}
        have = 0
        need = len(tMap)

        res, resInd = float('inf'), [-1, -1]
        l = 0

        for r in range(len(s)):
            cur[s[r]] = 1 + cur.get(s[r], 0)
            if cur[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res:
                    res = (r - l + 1)
                    resInd = [l, r]
                cur[s[l]] -= 1
                if cur[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        
        return s[resInd[0]:resInd[1] + 1] if res != float('inf') else ""