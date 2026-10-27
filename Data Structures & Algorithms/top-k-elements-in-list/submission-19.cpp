class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> buckets(nums.size() + 1);

        unordered_map<int, int> nMap;
        for (int n : nums) {
            nMap[n]++;
        }

        for (auto& [key, val] : nMap) {
            buckets[val].push_back(key);
        }

        int cur = 0;
        vector<int> res;

        for (int i = buckets.size() - 1; i >= 0; i--) {
            for (int val : buckets[i]) {
                res.push_back(val);
                cur++;
            }
            if (cur >= k) return res;
        }
        return res;
    }
};
