class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = time = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    fresh += 1
                if grid[y][x] == 2:
                    q.append([x, y])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q and fresh != 0:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx > len(grid[0]) - 1 or ny < 0 or ny > len(grid) - 1:
                        continue
                    if grid[ny][nx] == 1:
                        q.append([nx, ny])
                        grid[ny][nx] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1