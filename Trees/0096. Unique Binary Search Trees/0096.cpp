#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    int numTrees(int n) {
        ios_base::sync_with_stdio(0);
        cout.tie(0);
        cin.tie(0);

        vector<int> dp(n+1,0);
        dp[0]=1;
        dp[1]=1;

        for(int i=2; i<n+1; ++i){
            for(int j=1; j<i+1; ++j){
                dp[i]+=dp[j-1]*dp[i-j];
            }
        }
        
        return dp[n];
    }
};