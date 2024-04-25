#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int longestIdealString(string s, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<int>dp(26,0);
        int n=s.size();
        int res=0;

        for(int i=0; i<n; ++i){
            int curr=s[i]-'a';
            int best=0;
            for(int prev=0; prev<26; ++prev){
                if(abs(curr-prev)<=k){
                    best=max(best,dp[prev]);
                }
            }
            dp[curr]=max(dp[curr],best+1);
            res=max(res,dp[curr]);
        }
        return res;

    }
};