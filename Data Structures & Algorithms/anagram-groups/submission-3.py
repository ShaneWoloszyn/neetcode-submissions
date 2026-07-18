class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sMap = {}

        for s in strs:
            cur = "".join(sorted(s))
            if cur in sMap:
                sMap[cur].append(s)
            else:
                sMap[cur] = [s]
        
        res = []
        for vals in sMap.values():
            res.append(vals)
        
        return res
        
        