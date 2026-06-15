class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        sMap = {}
        tMap = {}

        for n in s:
            if n in sMap:
                sMap[n] += 1
            else:
                sMap[n] = 1
        
        for n in t:
            if n in tMap:
                tMap[n] += 1
            else:
                tMap[n] = 1
        s += t
        for n in s:
            if n in sMap and n not in tMap:
                return False
            if n in tMap and n not in sMap:
                return False
            if sMap[n] != tMap[n]:
                return False
        return True