class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         
         
        def search(x, y, i):
            if i == len(word):
                return True

            if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
                return False
                
            if board[y][x] != word[i]:
                return False
            
            temp = board[y][x]
            board[y][x] = "#"

            if search(x + 1, y, i + 1) or search(x, y + 1, i + 1) or search(x - 1, y, i + 1) or search(x, y - 1, i + 1):
                return True
            
            board[y][x] = temp
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if search(x, y, 0):
                    return True
        
        return False