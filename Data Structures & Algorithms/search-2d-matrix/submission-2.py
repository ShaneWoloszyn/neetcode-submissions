class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1

        while t <= b:
            m = (t + b) // 2
            first = matrix[m][0]
            last = matrix[m][len(matrix[m]) - 1]
            if first <= target and last >= target:
                break
            elif target > first and target > last:
                t = m + 1
            else:
                b = m - 1
        
        l = 0
        r = len(matrix[m]) - 1

        while l <= r:
            k = (l + r) // 2
            print(matrix[m][k])
            if matrix[m][k] > target:
                r = k - 1
            elif matrix[m][k] < target:
                l = k + 1
            else:
                return True
        return False
        
