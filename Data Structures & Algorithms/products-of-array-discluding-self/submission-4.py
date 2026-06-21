class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProd = []
        prod = 1

        for n in nums:
            lProd.append(prod)
            prod *= n
        
        rProd = [1] * len(nums)
        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            rProd[i] = prod
            prod *= nums[i]

        res = []
        for i in range(len(rProd)):
            res.append(rProd[i] * lProd[i])

        return res
