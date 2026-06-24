class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
    
        res = 0
    
        def search(x, y):
            if x >= COLS or x < 0 or y >= ROWS or y < 0:
                return 0
            
            if grid[y][x] != 1:
                return 0
            
            tot = 1
            grid[y][x] = -1

            tot += search(x - 1, y)
            tot += search(x + 1, y)
            tot += search(x, y - 1)
            tot += search(x, y + 1)

            return tot
        
        for y in range(ROWS):
            for x in range(COLS):
                res = max(res, search(x, y))

        return res