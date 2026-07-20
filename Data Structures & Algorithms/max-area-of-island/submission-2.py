class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0

        def search(x, y):
            if grid[y][x] != 1:
                return 0
            if grid[y][x] == 1:
                area = 1
                grid[y][x] = -1

                if x > 0:
                    area += search(x - 1, y)
                if x < len(grid[0]) - 1:
                    area += search(x + 1, y)
                if y > 0:
                    area += search(x, y - 1)
                if y < len(grid) - 1:
                    area += search(x, y + 1)
            return area
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                res = max(res, search(x, y))
        
        return res