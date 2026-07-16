class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        frqs = [[] for _ in range(len(nums) + 1)]
        print(count)
        for key, frq in count.items():
            print(frqs, frq)
            frqs[frq].append(key)
        
        res = []
        for frq in frqs[::-1]:
            while len(frq) > 0 and len(res) != k:
                res.append(frq[0])
                frq.pop(0)
        
        return res
            