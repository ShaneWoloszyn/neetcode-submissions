class Solution:
    def isPalindrome(self, s: str) -> bool:
        hold = ""
        for i in range(len(s)):
            if s[i].isalnum():
                hold += s[i].lower()

        l = 0
        r = len(hold) - 1
        while l < r:
            if hold[l] != hold[r]:
                return False
            l += 1
            r -= 1
        return True