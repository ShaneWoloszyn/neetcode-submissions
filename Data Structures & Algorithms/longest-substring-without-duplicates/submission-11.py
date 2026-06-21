class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1

        maxLen = 1
        cur = [s[l]]
        while r < len(s):
            while s[r] in cur:
                cur.pop(0)
                l += 1
            cur.append(s[r])
            r += 1
            maxLen = max(maxLen, len(cur))
        
        return maxLen