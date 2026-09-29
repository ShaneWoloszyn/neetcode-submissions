class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # pair [h, i]
        stack = []
        # go through heights
        # when our current height is < our top height
        # we pop until we get a >, with the pops being the width
        # increasing monotonic
        res = 0

        for i, h in enumerate(heights):
            hold = i
            while stack and stack[-1][0] > h:
                prevH, prevI = stack.pop()
                hold = prevI
                res = max(res, prevH * (i - prevI))
            
            if not stack or stack[-1][0] != h:
                stack.append([h, hold])
        
        r = len(heights) - 1

        for h, l in stack:
            res = max(res, h * (r - l + 1))

        return res