class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        cur = {}

        l = 0
        res, resLen = [-1, -1], float('inf')
        have, need = 0, len(tMap)
        for r in range(0, len(s)):
            cur[s[r]] = 1 + cur.get(s[r], 0)

            if cur[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r + 1]
                    resLen = (r - l + 1)
                
                cur[s[l]] -= 1
                if s[l] in tMap and tMap[s[l]] > cur[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0]:res[1]] if res != [-1, -1] else ""
