class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)
        
        have, need = 0, len(tMap)
        window = {}
        l = 0
        res, resLen = [-1, -1], float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tMap and window[c] == tMap[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1]
