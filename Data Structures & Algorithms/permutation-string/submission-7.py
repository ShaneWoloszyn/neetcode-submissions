class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sMap = Counter(s1)

        l = 0
        cur = Counter(s2[l:len(s1)])
        while l < len(s2) - len(s1):
            if cur == sMap:
                return True
            cur[s2[l]] -= 1
            if cur[s2[l]] == 0:
                del cur[s2[l]]
            cur[s2[l + len(s1)]] = 1 + cur.get(s2[l + len(s1)], 0)
            l += 1
        
        return cur == sMap