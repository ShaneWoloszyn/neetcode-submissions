class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for dig in digits:
            num += str(dig)
        num = int(num)
        num += 1

        return list(str(num))