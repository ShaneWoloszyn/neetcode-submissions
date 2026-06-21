class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        
        nMap = {}
        for n in nums:
            if n in nMap:
                nMap[n] += 1
            else:
                nMap[n] = 1

        for key, tok in nMap.items():
            buckets[tok].append(key)
    
        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
    
        return [-1]