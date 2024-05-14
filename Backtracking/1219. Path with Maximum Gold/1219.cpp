#pragma GCC optimize("O3","Oz","unroll-loops","fast-math","lto","omit-frame-pointer","march=native","inline-functions")

class Solution {
public:
    int row=0;
    int col=0;
    int res=0;
    int dfs(int r, int c, int currSum, vector<vector<int>>& grid) {
        if(r<0 || r>=row || c<0 || c>=col || grid[r][c]==0) {
            return 0;
        }

        int curr=grid[r][c];
        currSum+=grid[r][c];
        grid[r][c]=0;
        res=max(res,currSum);
        
        dfs(r+1,c,currSum,grid);
        dfs(r-1,c,currSum,grid);
        dfs(r,c+1,currSum,grid);
        dfs(r,c-1,currSum,grid);

        grid[r][c]=curr;
        return currSum;
    }

    int getMaximumGold(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        row=grid.size();
        col=grid[0].size();

        for(int r=0; r<row; ++r){
            for(int c=0; c<col; ++c){
                dfs(r,c,0,grid);
            }
        }
        return res;
    }
};