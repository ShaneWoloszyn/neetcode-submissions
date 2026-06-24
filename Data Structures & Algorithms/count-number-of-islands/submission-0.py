class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0

        def search(x, y):
            if x >= COLS or x < 0 or y >= ROWS or y < 0:
                return False
            
            if grid[y][x] != "1":
                return False
            
            grid[y][x] = "-1"

            search(x - 1, y)
            search(x + 1, y)
            search(x, y - 1)
            search(x, y + 1)

            return True
        
        for y in range(ROWS):
            for x in range(COLS):
                if search(x, y):
                    res += 1
        
        return res