class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid(nums):
            nMap = set()

            for n in nums:
                if n in nMap:
                    return False
                if n != ".":
                    nMap.add(n)

            return True
        for r in range(len(board)):
            row = []
            col = []
            for c in range(len(board[0])):
                row.append(board[r][c])
                col.append(board[c][r])
            if not valid(row) or not valid(col):
                return False
        
        for r in range(3):
            for c in range(3):
                square = []
                for dr in range(3):
                    for dc in range(3):
                        square.append(board[r * 3 + dr][c * 3 + dc])
                if not valid(square):
                    return False
        
        return True