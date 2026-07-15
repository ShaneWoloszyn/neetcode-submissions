class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], cur = cur, max(cur, arr[i])
            
        return arr