#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int appendCharacters(string s, string t) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int32_t s_idx = 0, t_idx = 0;
        int32_t s_n = s.size();
        int32_t t_n = t.size();

        while (s_idx < s_n && t_idx < t_n) {
            if (s[s_idx] == t[t_idx]) {
                s_idx++;
                t_idx++;
            } else {
                s_idx++;
            }
        }
        return t_n - t_idx;
    }
};