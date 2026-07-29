class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def search(x, y):
            if x < 0 or x > len(grid[0]) - 1 or y < 0 or y > len(grid) - 1:
                return
            
            if grid[y][x] == "1":
                grid[y][x] = "-1"
            else:
                return
            
            search(x + 1, y)
            search(x - 1, y)
            search(x, y + 1)
            search(x, y - 1)
        
        
        count = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    count += 1
                    search(x, y)
        
        return count