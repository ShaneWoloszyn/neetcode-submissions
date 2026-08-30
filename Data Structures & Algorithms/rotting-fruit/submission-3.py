class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque([])
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append([j, i])
                elif grid[i][j] == 1:
                    fresh += 1
        

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        time = 0
        while q and fresh != 0:
            time += 1
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS or grid[ny][nx] != 1:
                        continue
                    fresh -= 1
                    grid[ny][nx] = 2
                    q.append([nx, ny])
        
        return time if fresh == 0 else -1