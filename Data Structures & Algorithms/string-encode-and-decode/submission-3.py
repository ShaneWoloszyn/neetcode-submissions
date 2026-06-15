class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s))
            code += "#"
        code += "/"
        for s in strs:
            code += s
        print(code)
        return code
    def decode(self, s: str) -> List[str]:
        i = 0
        lens = []
        while s[i] != "/":
            cur = ""
            while s[i] != "#":
                cur += s[i]
                i += 1
            lens.append(int(cur))
            i += 1
        spot = i + 1
        ans = []
        print(lens)
        print(ans)
        for l in lens:
            ans.append(s[spot:spot+l])
            spot += l

        return ans