#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","march=native","lto","fast-math","omit-frame-pointer")
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0); 

        int n=grid.size();
        int m=grid[0].size();
        int res=0;

        for(int i=0; i<n; ++i){
            if(grid[i][0]==0){
                for(int j=0; j<m; ++j){
                    grid[i][j]=(grid[i][j]==1) ? 0 : 1;
                }
            }
        }
        for(int j=0; j<m; ++j){
            int count=0;
            for(int i=0; i<n; ++i){
                count+=(grid[i][j]==1) ? 1 : -1;
            }
            if(count<0){
                for(int i=0; i<n; ++i){
                    grid[i][j]=(grid[i][j]==1) ? 0 : 1;
                }
            }
        }
        for(int i=0; i<n; ++i){
            int rowNum=0;
            for(int j=0; j<m; ++j){
                rowNum=(rowNum<<1)|grid[i][j];
            }
            res+=rowNum;
        }
        
        return res;
    }
};