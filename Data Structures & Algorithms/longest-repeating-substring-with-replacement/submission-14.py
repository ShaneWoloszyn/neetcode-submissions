class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for char in charSet:
            l = 0
            subs = 0

            for r in range(len(s)):
                if s[r] != char:
                    subs += 1
                
                while subs > k:
                    subs -= 1 if s[l] != char else 0
                    l += 1
                
                res = max(res, (r - l + 1))
        
        return res