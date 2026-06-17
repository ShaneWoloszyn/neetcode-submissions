class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k

        countW = float('inf')

        while r <= len(blocks):
            cur = 0
            for i in range(l, r):
                if blocks[i] == "W":
                    cur += 1
            countW = min(cur, countW)
            l += 1
            r += 1
        
        return countW