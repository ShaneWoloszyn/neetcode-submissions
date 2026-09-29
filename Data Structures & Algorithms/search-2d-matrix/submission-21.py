class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        row = 0

        while l <= r:
            m = (l + r) // 2
            lo, hi = matrix[m][0], matrix[m][len(matrix[0]) - 1]

            if lo <= target <= hi:
                row = m
                break
            elif target < lo:
                r = m - 1
            else:
                l = m + 1
        
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False