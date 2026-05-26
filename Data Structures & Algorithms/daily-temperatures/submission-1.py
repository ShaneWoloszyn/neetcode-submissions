class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = 0
        r = 1
        end = []
        while l < len(temperatures):
            if r > len(temperatures) - 1:
                end.append(0)
                l += 1
                r = l + 1
            elif temperatures[l] >= temperatures[r]:
                r += 1
            else:
                end.append(r - l)
                l += 1
                r = l + 1
        return end