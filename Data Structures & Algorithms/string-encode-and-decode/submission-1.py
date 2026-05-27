class Solution:

    def encode(self, strs: List[str]) -> str:
        end = ""
        for s in strs:
            end += str(len(s)) + ","
        end += "#"
        for s in strs:
            end += s
        print(end)
        return end

    def decode(self, s: str) -> List[str]:
        lengths = []
        i = 0
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            lengths.append(int(cur))
            i += 1
        i += 1
        end = []
        for n in range(len(lengths)):
            end.append(s[i: (i + lengths[n])])
            i += lengths[n]
        
        return end
            