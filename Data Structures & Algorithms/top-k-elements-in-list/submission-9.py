class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        freq = Counter(nums)
        
        for i in range(len(nums) + 1):
            buckets.append([])

        for key, value in freq.items():
            buckets[value].append(key)

        end = []
        t = k
        for bucket in reversed(buckets):
            for items in bucket:
                if t > 0:
                    end.append(items)
                    t = t - 1
                

        return end
