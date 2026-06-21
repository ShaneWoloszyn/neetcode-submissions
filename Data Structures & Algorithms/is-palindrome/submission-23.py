class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = ""
        for let in s:
            if let.isalnum():
                check += let.lower()
        print(check)

        l, r = 0, len(check) - 1

        while l < r:
            if check[l] != check[r]:
                return False
            l += 1
            r -= 1
        return True