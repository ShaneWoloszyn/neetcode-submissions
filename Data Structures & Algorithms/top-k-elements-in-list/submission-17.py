class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]

        nMap = Counter(nums)

        for key, frq in nMap.items():
            buckets[frq].append(key)
        
        res = []

        print(buckets)
        i = len(buckets) - 1

        while k > 0:
            if buckets[i]:
                for val in buckets[i]:
                    k -= 1
                    res.append(val)
            i -= 1
        return res    