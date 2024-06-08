#pragma GCC optimize("O3","Oz","inline-functions","unroll-loops","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        std::unordered_map<int, int> seenMod;
        seenMod[0] = -1;
        int32_t currMod = 0;

        for (int32_t i = 0; i < nums.size(); i++) {
            currMod = (currMod + nums[i]) % k;
            if (seenMod.find(currMod) != seenMod.end()) {
                if (i - seenMod[currMod] > 1) return true;
            } 
            else seenMod[currMod] = i;
        }
        return false;
    }
};