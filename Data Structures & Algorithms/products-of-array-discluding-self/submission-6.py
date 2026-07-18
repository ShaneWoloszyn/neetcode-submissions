class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProd = []
        cur = 1
        for n in nums:
            lProd.append(cur)
            cur *= n
        
        rProd = []
        cur = 1
        for n in nums[::-1]:
            rProd.append(cur)
            cur *= n
        
        rProd = rProd[::-1]

        res = []

        for i in range(len(nums)):
            res.append(rProd[i] * lProd[i])


        return res