class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        toCheck = set(s)
        res = 1

        for char in toCheck:
            l = 0
            cur = 0

            for r in range(len(s)):
                if s[r] != char:
                    cur += 1
                
                while cur > k:
                    if s[l] != char:
                        cur -= 1
                    l += 1
                res = max(res, (r - l + 1))
        
        return res