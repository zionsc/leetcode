#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int32_t prefix = 0;
        for (auto& num : nums) {
            prefix ^= num;
        }
        
        int32_t diffBit = 1;
        while (!(diffBit & prefix)) {
            diffBit <<= 1;
        }

        int a = 0;
        int b = 0;
        for (auto& num : nums) {
            if (num & diffBit) {
                a ^= num;
            } else {
                b ^= num;
            }
        }

        return {a, b};
    }
};