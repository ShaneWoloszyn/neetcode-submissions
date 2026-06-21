class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            print(m)
            if matrix[m][0] <= target and matrix[m][len(matrix[m]) - 1] >= target:
                break
            elif matrix[m][0] < target:
                l = m + 1
            else:
                r = m - 1
        row = m
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

        return False