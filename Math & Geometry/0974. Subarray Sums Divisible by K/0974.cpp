#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int32_t prefix = 0;
        int32_t res = 0;
        std::unordered_map<int32_t, int32_t> seenBefore;
        seenBefore[0] = 1;

        for (auto& num : nums) {
            prefix += num;
            prefix %= k;
            if (prefix < 0) prefix += k;
            res += seenBefore[prefix];
            seenBefore[prefix]++;
        }
        return res;
    }
};