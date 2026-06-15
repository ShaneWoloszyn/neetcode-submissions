class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValid(row):
                return False
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not self.isValid(col):
                return False

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                square = []
                for i in range(3):
                    for j in range(3):
                        square.append(board[row_start + i][col_start + j])
                
                if not self.isValid(square):
                    return False
        
        return True

    def isValid(self, check: List[str]) -> bool:
        nMap = {}
        for n in check:
            if n != "." and n in nMap:
                return False
            nMap[n] = 1
        return True
