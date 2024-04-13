#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int maxHistogram(vector<int>& heights){
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int maxRectangle=0;
        int n=heights.size();
        stack<pair<int,int>> stk;

        for(int i=0; i<heights.size(); ++i){
            int start=i;
            while(!stk.empty() && stk.top().first>heights[i]){
                int height=stk.top().first;
                int idx=stk.top().second;
                stk.pop();
                maxRectangle=max(maxRectangle,height*(i-idx));
                start=idx;
            }
            stk.push({heights[i],start});
        }

        while(!stk.empty()){
            int height=stk.top().first;
            int idx=stk.top().second;
            maxRectangle=max(maxRectangle, height*(n-idx));
            stk.pop();
        }
        return maxRectangle;
    }

    int maximalRectangle(vector<vector<char>>& matrix) {
        int n=matrix.size();
        int m=matrix[0].size();
        vector<vector<int>> histogram(n, vector<int>(m,0));

        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                if(matrix[i][j]=='1'){
                    histogram[i][j] = (i==0) ? 1 : histogram[i-1][j]+1;
                }
            }
        }
        
        int res=0;
        for(int i=0; i<n; ++i){
            res=max(res, maxHistogram(histogram[i]));
        }
        return res;
    }
};