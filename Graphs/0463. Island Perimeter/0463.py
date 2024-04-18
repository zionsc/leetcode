#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int res=0;
        int rows=grid.size();
        int cols=grid[0].size();

        for(int r=0; r<rows; ++r){
            for(int c=0; c<cols; ++c){
                if(grid[r][c]==1){
                    if(r==0 || grid[r-1][c]==0)res++;
                    if(r==rows-1 || grid[r+1][c]==0)res++;
                    if(c==0 || grid[r][c-1]==0)res++;
                    if(c==cols-1 || grid[r][c+1]==0)res++;
                }
            }
        }
        return res;
        
    }
};