class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for n in nums:
            if n not in hashMap:
                hashMap[n] = 1
            else:
                hashMap[n] = hashMap[n] + 1
        
        end = []

        while k > 0:
            maxVal = -1
            maxN = -1
            for n in hashMap:
                if hashMap[n] > maxVal:
                    maxVal = hashMap[n]
                    maxN = n
            del hashMap[maxN]
            print(hashMap)
            end.append(maxN)
            k -= 1
        return end