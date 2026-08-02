class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        toCheck = set(s)
        res = 0

        for char in toCheck:
            l = 0
            switch = 0

            for r in range(len(s)):
                if s[r] != char:
                    switch += 1
                    while switch > k:
                        if s[l] != char:
                            switch -= 1
                        l += 1
                res = max(res, (r - l + 1))
        
        return res