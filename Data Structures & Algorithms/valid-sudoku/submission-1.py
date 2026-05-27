class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.colsValid(board) and self.rowsValid(board) and self.squareValid(board)
    
    def rowsValid(self, board: List[List[str]]) -> bool:
        for rows in board:
            rowMap = {}
            for s in rows:
                if s != "." and s in rowMap:
                    return False
                else:
                    rowMap[s] = 1
        return True

    def colsValid(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            colMap = {}
            for j in range(len(board)):
                if board[j][i] != "." and board[j][i] in colMap:
                    return False
                else:
                    colMap[board[j][i]] = 1
            print(colMap)
        return True

    
    def squareValid(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                squareMap = {}
                for k in range(3):
                    for l in range(3):
                        if board[(i*3)+k][(j*3)+l] != "." and board[(i*3)+k][(j*3)+l] in squareMap:
                            return False
                        else:
                            squareMap[board[(i*3)+k][(j*3)+l]] = 1
        return True