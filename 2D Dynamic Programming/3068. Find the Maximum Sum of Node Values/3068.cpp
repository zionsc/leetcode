#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    long long maximumValueSum(vector<int>& nums, int k, vector<vector<int>>& edges) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n=nums.size();
        vector<vector<long long>>dp(n+1, vector<long long>(2,0));
        dp[n][0]=0;
        dp[n][1]=INT_MIN;

        for(int i=n-1; i>=0; --i){
            for(int j=0; j<2; ++j){
                long long change = dp[i+1][j^1]+(nums[i]^k);
                long long noChange = dp[i+1][j]+(nums[i]);
                dp[i][j] = max(change, noChange);
            }
        }
        return dp[0][0];
    }
};