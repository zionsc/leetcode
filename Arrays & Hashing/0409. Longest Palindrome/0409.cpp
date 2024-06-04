#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int longestPalindrome(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        std::unordered_set<char> char_set;
        int32_t res = 0;

        for (auto& c : s) {
            if (char_set.find(c) != char_set.end()) {
                char_set.erase(c);
                res += 2;
            } else {
                char_set.insert(c);
            }
        }

        if (!char_set.empty()) res++;

        return res;
    }
};