class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefixSum((n*2)+1,-2);
        prefixSum[n] = -1;
        int prefix = 0;
        int res = 0;

        for (int i=0; i<nums.size(); ++i) {
            prefix += nums[i] > 0 ? 1:-1;
            if (prefixSum[prefix+n]==-2) {
                prefixSum[prefix+n] = i;
            } else {
                res = max(res, i - prefixSum[prefix+n]);
            }
        } return res;
    }
};