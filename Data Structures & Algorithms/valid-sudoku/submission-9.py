class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def search(items):
            check = {}
            for n in items:
                if n != "." and n in check:
                    return False
                check[n] = 1
            
            return True
        
        for row in board:
            if not search(row):
                return False
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not search(col):
                return False

        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[(i * 3) + k][(j * 3) + l])
                if not search(square):
                    return False
        
        return True