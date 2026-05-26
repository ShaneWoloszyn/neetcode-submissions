class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for n in nums:
            if n in numsMap:
                numsMap[n] = numsMap[n] + 1
            else:
                numsMap[n] = 1
        
        holdN = 0
        end = []
        for i in range(k):
            max = 0
            for n in nums:
                if numsMap[n] > max:
                    print(numsMap[n])
                    max = numsMap[n]
                    holdN = n
            end.append(holdN)
            numsMap[holdN] = 0
        return end
            