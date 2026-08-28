class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sMap = Counter(s)

        res = []

        for char in order:
            if char in sMap:
                res.append(char * sMap[char])
                del sMap[char]
        
        for key, frq in sMap.items():
            res.append(key * frq)

        return "".join(res)
        