class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "/"
        
        res += "#"

        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        r = s.index("#") + 1

        cur = ""
        l = 0
        while s[l] != "#":
            while s[l] != "/":
                cur += s[l]
                l += 1
            res.append(s[r:(r + int(cur))])
            r += int(cur)
            cur = ""
            l += 1
        
        return res