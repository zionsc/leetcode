#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n=grid.size();
        int m=grid[0].size();
        vector<int>dp(grid[0].begin(),grid[0].end());

        for(int i=1; i<n; ++i){
            vector<int>temp(dp.begin(),dp.end());
            for(int j=0; j<m; ++j){
                int best=INT_MAX;
                for(int k=0; k<m; ++k){
                    if(k!=j) best=min(best,dp[k]);
                }
            temp[j]=best+grid[i][j];
            }
            dp=temp;
        }
        return *min_element(dp.begin(),dp.end());
    }
};