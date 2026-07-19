class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                t, start = stack.pop()
                res[start] = i - start
            stack.append([temp, i])
        
        return res