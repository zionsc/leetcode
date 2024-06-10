#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int heightChecker(vector<int>& heights) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<int> sortedHeights(heights.begin(), heights.end());
        sort(heights.begin(), heights.end());

        uint32_t res = 0;
        for (int32_t i = 0; i < heights.size(); i++) {
            if (heights[i] != sortedHeights[i]) res++;
        }
        
        return res;
    }
};