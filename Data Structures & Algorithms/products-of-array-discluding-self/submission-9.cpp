class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> rProd(nums.size(), 1);
        int curR = 1;

        for (int i = nums.size() - 1; i >= 0; i--) {
            rProd[i] = curR;
            curR *= nums[i];
        }

        vector<int> res;
        int curL = 1;

        for (int i = 0; i < nums.size(); i++) {
            res.push_back(curL * rProd[i]);
            curL *= nums[i];
        }

        return res;
    }
};
