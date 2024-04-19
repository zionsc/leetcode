#pragma GCC optimize('03','unroll-loops')

struct pair_hash {
    template<class T1, class T2>
    std::size_t operator() (const std::pair<T1,T2>& pair) const {
        auto hash1=std::hash<T1>{}(pair.first);
        auto hash2=std::hash<T2>{}(pair.second);
        return hash1^hash2;
    }
};

class Solution {
public:
    std::unordered_set<pair<int,int>, pair_hash>visited;
    int rows=0;
    int cols=0;

    void bfs(int row, int col, vector<vector<char>>& grid) {
        deque<pair<int,int>>q;
        q.push_back({row,col});
        visited.insert({row,col});

        vector<pair<int,int>>dir = {{1,0},{-1,0},{0,1},{0,-1}};

        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop_front();
            for(auto d : dir){
                int dr=d.first;
                int dc=d.second;
                if(r+dr>=0 && r+dr<rows && c+dc>=0 && c+dc<cols && grid[r+dr][c+dc]=='1' && visited.find({r+dr,c+dc})==visited.end()){
                    q.push_back({r+dr,c+dc});
                    visited.insert({r+dr,c+dc});
                }
            }
        }

    }

    int numIslands(vector<vector<char>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int res=0;
        rows=grid.size();
        cols=grid[0].size();

        for(int r=0; r<rows; ++r){
            for(int c=0; c<cols; ++c){
                if(visited.find({r,c})==visited.end() && grid[r][c]=='1'){
                    bfs(r,c,grid);
                    ++res;
                }
            }
        }
        return res;
    }
};