class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def search(idx, x, y):
            if idx == len(word):
                return True
            if x >= COLS or x < 0 or y >= ROWS or y < 0 or word[idx] != board[y][x]:
                return False
            
            board[y][x] = "."

            res = (search(idx + 1, x - 1, y) or 
                   search(idx + 1, x + 1, y) or
                   search(idx + 1, x, y - 1) or
                   search(idx + 1, x, y + 1))
            board[y][x] = word[idx]
            return res
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if search(0, x, y):
                    return True
        
        return False