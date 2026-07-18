class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(nums):
            nMap = {}
            for n in nums:
                if n != "." and n in nMap:
                    return False
                nMap[n] = 1
            return True
        
        for row in board:
            if not check(row):
                return False
        
        for i in range(9):
            col = []
            for j in range(9):
                col.append(board[j][i])
            if not check(col):
                return False
        
        for i in range(3):
            for j in range(3):
                square = []
                for k in range(3):
                    for l in range(3):
                        square.append(board[i * 3 + k][j * 3 + l])
                if not check(square):
                    return False
        
        return True