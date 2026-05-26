class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = 1

        while l < len(numbers) - 1:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            else:
                r = r + 1
            if r > len(numbers) - 1:
                l = l + 1
                r = l + 1
        return -1