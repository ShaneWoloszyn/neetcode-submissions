class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "/"
        
        res += "#"

        for s in strs:
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        lens = []
        i = 0
        while s[i] != "#":
            cur = ""
            while s[i] != "/":
                cur += s[i]
                i += 1
            lens.append(int(cur))
            i += 1
        
        i += 1
        
        res = []

        for l in lens:
            res.append(s[i: i + l])
            i += l

        return res