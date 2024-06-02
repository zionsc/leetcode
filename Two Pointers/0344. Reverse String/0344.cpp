#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    void reverseString(vector<char>& s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            char temp = s[l];
            s[l] = s[r];
            s[r] = temp;
            l++;
            r--;
        }

    }
};