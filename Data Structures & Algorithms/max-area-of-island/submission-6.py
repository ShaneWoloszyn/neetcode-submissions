class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def search(x, y):
            if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1 or grid[y][x] != 1:
                return 0
            
            grid[y][x] = -1

            return 1 + search(x + 1, y) + search(x - 1, y) + search(x, y + 1) + search(x, y - 1)
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    res = max(res, search(x, y))
        
        return res