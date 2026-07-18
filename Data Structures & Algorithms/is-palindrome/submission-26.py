class Solution:
    def isPalindrome(self, s: str) -> bool:
        toCheck = ""
        for char in s:
            if char.isalnum():
                toCheck += char.lower()
        
        l, r = 0, len(toCheck) - 1

        while l <= r:
            if toCheck[l] != toCheck[r]:
                return False
            l, r = l + 1, r - 1


        return True