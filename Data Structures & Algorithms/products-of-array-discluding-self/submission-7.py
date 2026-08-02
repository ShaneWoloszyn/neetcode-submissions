import operator
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProd = []
        cur = 1
        for n in nums:
            lProd.append(cur)
            cur *= n
        
        rProd = [0 for _ in range(len(nums))]
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            rProd[i] = cur
            cur *= nums[i]
        
        print(lProd, rProd)

        res = []
        for i in range(len(nums)):
            res.append(lProd[i] * rProd[i])

        return res