class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            print(matrix[m])
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[m]) - 1]:
                break
            elif target < matrix[m][0] and target < matrix[m][len(matrix[m]) - 1]:
                r = m - 1
            else:
                l = m + 1
            
        row = matrix[m]

        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2
            print(row)
            if target > row[m]:
                l = m + 1
            elif target < row[m]:
                r = m - 1
            else:
                return True
        
        return False