#pragma GCC optimze("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","")
class Solution {
public:
    vector<int> longestCommonSubsequence(vector<vector<int>>& arrays) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int count[101]{};
        std::vector<int> res;
        
        for (int i = 0; i < arrays.size() - 1; i++) {
            for (auto& num : arrays[i]) {
                count[num]++;
            }
        }

        for (auto& num : arrays.back()) {
            if (count[num] == arrays.size() - 1) res.push_back(num);
        }

        return res;
    }
};