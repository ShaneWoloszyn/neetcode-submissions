class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        if len(s) == 0:
            return 0
        arr = [s[0]]
        maxDist = 1
        while r < len(s):
            if s[r] not in arr:
                arr.append(s[r])
                r += 1
            else:
                arr.pop(0)
                l += 1
            maxDist = max(maxDist, (r - l))
        return maxDist