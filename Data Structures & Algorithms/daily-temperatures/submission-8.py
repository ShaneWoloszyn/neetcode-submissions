class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in range(len(temperatures))]
        stack = []
        
        for i, temps in enumerate(temperatures):
            while stack and stack[-1][0] < temps:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temps, i])
        
        return res