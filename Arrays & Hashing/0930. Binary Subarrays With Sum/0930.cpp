class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        unordered_map<int,int> prefixSum;
        prefixSum[0] = 1;
        int res = 0;
        int currSum = 0;

        for (auto& num : nums) {
            currSum += num;
            if (prefixSum.find(currSum - goal) != prefixSum.end()) {
                res += prefixSum[currSum - goal];
            }
            prefixSum[currSum]++;
        }
        return res;
    }
};