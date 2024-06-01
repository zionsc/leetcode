#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int scoreOfString(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int32_t res = 0;
        for (int32_t i = 0; i < s.size()-1; i++) {
            res += abs(s[i] - s[i+1]);
        }
        return res;
    }
};