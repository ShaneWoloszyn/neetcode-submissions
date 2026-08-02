class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        res = 1

        l = 0
        cur = {s[l]: 1}
        for r in range(1, len(s)):

            while s[r] in cur and cur[s[r]] > 0:
                cur[s[l]] = 0
                l += 1
            
            cur[s[r]] = 1
            res = max(res, (r - l + 1))
        
        return res