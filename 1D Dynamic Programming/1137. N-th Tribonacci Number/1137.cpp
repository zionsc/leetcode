#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int tribonacci(int n) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(n==0)return 0;
        if(n==1)return 1;
        if(n==2)return 1;

        vector<int>dp(n+1);
        dp[0]=0;
        dp[1]=1;
        dp[2]=1;

        for(int i=3;i<n+1;++i){
            dp[i]=dp[i-3]+dp[i-2]+dp[i-1];
        }
        return dp[n];
    }
};