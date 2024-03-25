class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);

        vector<int> res;
        for (int& num : nums) {
            int idx = abs(nums) - 1;
            if (nums[idx] < 0) {
                res.push_back(abs(num));
            }
            nums[idx] *= -1;
        }
        return res;
    }
};