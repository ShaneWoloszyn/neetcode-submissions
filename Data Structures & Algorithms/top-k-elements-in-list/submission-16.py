class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nMap = Counter(nums)

        buckets = [[] for i in range(len(nums) + 1)]
        for key, frq in nMap.items():
            buckets[frq].append(key)
        
        res = []
        for bucket in buckets[::-1]:
            while k != 0 and len(bucket) > 0:
                res.append(bucket.pop())
                k -= 1
            if k == 0:
                return res

        return res
