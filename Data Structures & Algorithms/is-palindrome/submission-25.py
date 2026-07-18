class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for char in s:
            if char.isalnum():
                check += char.lower()
        
        l, r = 0, len(check) - 1
        while l < r:
            if check[l] != check[r]:
                return False
            l += 1
            r -= 1

        return True