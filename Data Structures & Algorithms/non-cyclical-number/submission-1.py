class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []

        while True:
            hold = 0
            for l in list(str(n)):
                hold += (int(l) * int(l))
            
            n = hold 

            if n == 1:
                return True
            if n in seen:
                return False

            seen.append(n)
        return False