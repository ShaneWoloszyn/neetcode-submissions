class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we need to do ___
        # we can it with this __
        # watch out for ___


        # 1.) Make a deque to handle our current rotting oranges
        # 2.) I'm gonna count the number of fresh oranges, so at the end, i can compare it to how many rotted
        # 3.) go through the grid, add the rotting oranges to the deque
        # 4.) every time we start a new rotting cycle, we iterate through all the oranges that were there at the start, and we increment time by one. We add neighboring fresh oranges to the end of the q to be processed in the next step
        # 5.) Once our q is empty, we can compare how maany rotted to how many started fresh to see if it was completed, if it was our time is our return

        q = deque([])
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                # if its a 1 increment fresh
                # if its a 2 add to deque
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        # we now have the # of fresh fruits and our starting rotting oranges
        time = 0
        rotted = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # while we have something to rot, continue
        while q:
            time += 1
            # safe guard so we only process rotted oranges that started at this time
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # if oob or its not a fresh fruit continue
                    if not (0 <= nr < ROWS) or not (0 <= nc < COLS) or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    rotted += 1
                    q.append((nr, nc))
        

        return max(0, time - 1) if rotted == fresh else -1







