class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def dfs(x, y):
            if x < 0 or x > len(board[0]) - 1 or y < 0 or y > len(board) - 1 or board[y][x] == "X" or board[y][x] == "T":
                return
            
            board[y][x] = "T"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for x in range(len(board[0])):
            dfs(x, 0)
            dfs(x, len(board) - 1)
        
        for y in range(len(board)):
            dfs(0, y)
            dfs(len(board[0]) - 1, y)
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "T":
                    board[y][x] = "O"
        