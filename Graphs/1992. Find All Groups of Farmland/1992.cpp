#pragma GCC optimize('03','unroll-loops')

struct hash_pair {
    template<class T1, class T2>
    std::size_t operator() (const std::pair<T1,T2>& pair) const {
        auto hash1=std::hash<T1>{}(pair.first);
        auto hash2=std::hash<T2>{}(pair.second);
        return hash1^hash2;
    }
};


class Solution {
public:
    std::unordered_set<pair<int,int>, hash_pair>visited;
    int rows=0;
    int cols=0;

    pair<int,int> bfs(int row, int col, vector<vector<int>>& land) {
        deque<pair<int,int>>q{{row,col}};
        visited.insert({row,col});
        pair<int,int>br{row,col};
        vector<pair<int,int>> dir{{1,0},{0,1},{-1,0},{0,-1}};

        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop_front();
            for(auto d : dir){
                int nr=r+d.first;
                int nc=c+d.second;
                if(nr>=0 && nr<rows && nc>=0 && nc<cols && visited.find({nr,nc})==visited.end() && land[nr][nc]==1){
                    visited.insert({nr,nc});
                    q.push_back({nr,nc});
                    if(nr>br.first)br={nr,nc};
                    else if(nr==br.first && nc>br.second)br={nr,nc};
                }
            }
        }
        return br;
    }

    vector<vector<int>> findFarmland(vector<vector<int>>& land) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        if (land.empty())return {};
        rows=land.size();
        cols=land[0].size();
        vector<vector<int>>res;

        for(int r=0; r<rows; ++r){
            for(int c=0; c<cols; ++c){
                if(visited.find({r,c})==visited.end() && land[r][c]==1){
                    pair<int,int>br=bfs(r,c,land);
                    res.push_back({r,c,br.first,br.second});
                }
            }
        }

        return res;
    }
};