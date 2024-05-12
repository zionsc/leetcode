#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","omit-frame-pointer","lto")
class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n=grid.size();
        std::vector<std::vector<int>>maxLocal(n-2,std::vector<int>(n-2,0));

        for(int i=0; i<n-2; ++i){
            for(int j=0; j<n-2; ++j){
                int val=-1;
                for(int k=i; k<i+3; ++k){
                    for(int l=j; l<j+3; ++l){
                        val=std::max(val,grid[k][l]);
                    }
                }
                maxLocal[i][j]=val;
            }
        }
        return maxLocal;
    }
};