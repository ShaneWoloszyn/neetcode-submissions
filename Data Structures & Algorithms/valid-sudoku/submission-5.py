class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            # check rows
            for i in range(9):
                if not self.isValidSet(board[i]):
                    print(board[i])
                    return False
            print("here")
            
            # check cols

            for i in range(9):
                col = []
                for j in range(9):
                    col.append(board[j][i])
                if not self.isValidSet(col):
                    return False
            
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    square = []
                    for k in range(3):
                        for l in range(3):
                            print([i+k, j+l])
                            print(square)
                            square.append(board[i + k][j + l])
                    if not self.isValidSet(square):
                        return False
            return True


    def isValidSet(self, vals: List[str]) -> bool:
        vMap = {}
        for v in vals:
            if v in vMap and v != ".":
                return False
            vMap[v] = 1
            
        return True