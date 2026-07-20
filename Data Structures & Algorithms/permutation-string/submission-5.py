class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sMap = Counter(s1)
        l, r = 0, len(s1) - 1
        tMap = Counter(s2[l:r + 1])

        while r < len(s2) - 1:
            print(sMap, tMap)
            if sMap == tMap:
                return True
            r += 1
            tMap[s2[r]] += 1
            tMap[s2[l]] -= 1
            l += 1
            if tMap[s2[l]] == 0:
                del tMap[s2[l]]
        
        if sMap == tMap:
                return True
        
        return False