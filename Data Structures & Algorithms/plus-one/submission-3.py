class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] = digits[-1] + 1


        carry = digits[-1] // 10

        digits[-1] %= 10

        i = len(digits) - 2

        while i >= 0 and carry != 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
            i -= 1
        

        return [carry] + digits if carry != 0 else digits
            