class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        count = {}
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
            
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        for n, frq in count.items():
            buckets[frq].append(n)
        
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        return [-1]