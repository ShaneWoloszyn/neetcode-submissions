class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str((len(s))) + "/"
        res += "#"
        
        for s in strs:
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        lengths = []

        while s[i] != "#":
            cur = ""
            while s[i] != "/":
                cur += s[i]
                i += 1
            lengths.append(int(cur))
            i += 1
        i += 1

        res = []
        for length in lengths:
            res.append(s[i:i + length])
            i += length

        return res