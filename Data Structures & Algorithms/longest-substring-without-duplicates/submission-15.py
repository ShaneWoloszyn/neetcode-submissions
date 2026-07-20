class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        res = 1

        while r < len(s):
            res = max(res, (r - l))
            while s[r] in s[l:r]:
                l += 1
            r += 1
        res = max(res, (r - l))
        return res