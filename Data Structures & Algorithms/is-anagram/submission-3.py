class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] = hashMap[s[i]] + 1

        for i in range(len(t)):
            if t[i] not in hashMap or hashMap[t[i]] == 0:
                return False
            else:
                hashMap[t[i]] = hashMap[t[i]] - 1
        return True
