class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        nMap = Counter(nums)

        for key, freq in nMap.items():
            buckets[freq].append(key)
        
        res = []
        i = len(buckets) - 1
        while k > 0:
            res += buckets[i]
            k -= len(buckets[i])
            i -= 1
        
        return res
