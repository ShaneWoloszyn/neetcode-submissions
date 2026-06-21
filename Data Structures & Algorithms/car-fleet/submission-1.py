class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [[p, s] for p, s in zip(position, speed)] 
        times = sorted(times)

        stack = [] # time to arrival

        for p, s in times[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)