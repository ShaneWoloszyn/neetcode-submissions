class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0

        
        while l < len(numbers):
            r = l + 1
            while r < len(numbers):
                cur = numbers[l] + numbers[r]
                print(l, r, cur)
                if cur == target:
                    return [l + 1, r + 1]
                elif cur > target:
                    r = len(numbers)
                r += 1
            l += 1
        
        return []