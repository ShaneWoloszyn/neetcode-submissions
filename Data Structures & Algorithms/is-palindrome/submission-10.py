class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(alnum)
        l = 0
        r = len(alnum) - 1
        while l <= r:
            if (alnum[l] != alnum[r]):
                return False
            l += 1
            r -= 1
        return True
