class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr = digits[::-1]    


        arr[0] += 1
        i = 0
        while arr[i] == 10:
            print(arr)
            arr[i] = 0
            if i >= len(arr) - 1:
                arr[i] = 0
                arr.append(1)
                i += 1
            else:
                arr[i + 1] += 1
                i += 1
        
        return arr[::-1]