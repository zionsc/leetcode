#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int equalSubstring(string s, string t, int maxCost) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int l=0;
        int res=0;
        int curr=0;
        vector<int>count(s.size());
        for (int i=0; i<s.size(); i++) {
            count[i] = abs(s[i] - t[i]);
        }

        for (int r=0; r<count.size(); r++) {
            maxCost-=count[r];
            curr++;
            if (maxCost>=0) {
                res=max(res,curr);
            }
            while (maxCost<0) {
                maxCost+=count[l];
                l++;
                curr--;
            }
        }
        return res;
    }
};