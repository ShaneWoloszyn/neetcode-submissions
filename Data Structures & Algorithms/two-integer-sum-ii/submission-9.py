class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nMap = {}

        for i, n in enumerate(numbers):
            if n in nMap:
                nMap[n].append(i)
            else:
                nMap[n] = [i]

        for key, token in nMap.items():
            if target - key in nMap:
                return [nMap[key][0] + 1, nMap[target - key][0] + 1]

        return nMap   
