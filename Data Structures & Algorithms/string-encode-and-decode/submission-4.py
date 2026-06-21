class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += (str(len(s)) + "#")
            
        ans += ("/")
    
        for s in strs:
            ans += (s)

        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        lengths = []

        while s[i] != "/":
            cur = ""
            while s[i] != "#":
                cur += s[i]
                i += 1
            lengths.append(int(cur))
            i += 1
        i += 1

        for l in lengths:
            res.append(s[i:i+l])
            i += l

        return res