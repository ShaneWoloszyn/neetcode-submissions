class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def search(x, y, cur):
            if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1 or grid[y][x] == 0 or grid[y][x] == -1 or grid[y][x] < cur:
                return

            grid[y][x] = cur

            search(x + 1, y, cur + 1)
            search(x - 1, y, cur + 1)
            search(x, y + 1, cur + 1)
            search(x, y - 1, cur + 1)
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    search(x + 1, y, 1)
                    search(x - 1, y, 1)
                    search(x, y + 1, 1)
                    search(x, y - 1, 1)
            
            