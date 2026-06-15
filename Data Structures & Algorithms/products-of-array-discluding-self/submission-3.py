class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lProd = []
        l = 1
        for n in nums:
            lProd.append(l)
            l *= n
        
        rProd = [1] * len(nums)
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            rProd[i] = r
            r *= nums[i]
        print(rProd)
        print(lProd)
        ans = []
        for i in range(len(rProd)):
            ans.append(rProd[i] * lProd[i])

        return ans