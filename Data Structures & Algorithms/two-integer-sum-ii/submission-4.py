class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < len(numbers):
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                r += 1
            l += 1
            r = l + 1
        return []