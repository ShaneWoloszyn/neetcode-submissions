class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we have a fleet if a car behind another will arrive slower
        # going from last position, we can find if its slower than the stack in front of it
        # if it is we pop and then append

        ps = [[p, s] for p, s in zip(position, speed)]
        ps.sort(key=lambda i:-i[0])
        stack = []
        
        for p, s in ps:

            time = (target - p) / s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)

        
        return len(stack)