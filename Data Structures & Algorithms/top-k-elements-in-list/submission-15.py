class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for _ in range(len(nums) + 1)]

        nums = Counter(nums)

        for key, frq in nums.items():
            count[frq].append(key)

        res = []

        for i in range(len(count) - 1, -1, -1):
            if k == 0:
                return res
            
            while k > 0 and len(count[i]) != 0:
                res.append(count[i][0])
                count[i].pop(0)
                k -= 1
        
        return res