class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create hashmap
        # add characters until repeat
        # move a char forward and claer hashmap 
        # repeat
        max = 0
        l = 0
        r = 0
        hashMap = {}
        while l < len(s):
            if r >= len(s) or s[r] in hashMap:
                if max < r - l:
                    max = r - l
                l += 1
                r = l
                hashMap = {}
            else:
                hashMap[s[r]] = 1
                r += 1
        return max