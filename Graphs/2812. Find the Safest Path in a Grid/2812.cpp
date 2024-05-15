#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","march=native","fast-math","lto","omit-frame-pointer")
class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n = grid.size();
        vector<vector<int>> distance(n, vector<int>(n,-1));
        array<pair<int,int>,4> directions = {{{1,0}, {0,1}, {-1,0}, {0,-1}}};
        deque<array<int,3>> q;

        for(int i=0; i<n; ++i){
            for(int j=0; j<n; ++j){
                if(grid[i][j]==1){
                    q.push_back({i,j,0});    
                }
            }
        }

        while(!q.empty()){
            int r=q.front()[0];
            int c=q.front()[1];
            int dist=q.front()[2];
            q.pop_front();
            if(distance[r][c]!=-1) continue;
            distance[r][c]=dist;
            for(auto& p : directions){
                int dx=p.first;
                int dy=p.second;
                if(r+dx>=0 && r+dx<n && c+dy>=0 && c+dy<n){
                    q.push_back({r+dx,c+dy,dist+1});
                }
            }
        }

        priority_queue<array<int,3>> pq; // max heap by default in CPP
        vector<vector<int>> visited(n, vector<int>(n, -1));
        pq.push({distance[0][0],0,0});
        visited[0][0]=1;
        while(!pq.empty()){
            int dist=pq.top()[0];
            int r=pq.top()[1];
            int c=pq.top()[2];
            pq.pop();

            if(r==n-1 && c==n-1) return dist;
            for(auto& p : directions){
                int dx=p.first;
                int dy=p.second;
                if(r+dx>=0 && r+dx<n && c+dy>=0 && c+dy<n && grid[r+dx][c+dy]!=1 && visited[r+dx][c+dy]==-1){
                    int newDist=distance[r+dx][c+dy];
                    pq.push({min(dist,newDist),r+dx,c+dy});
                    visited[r+dx][c+dy]=1;
                }
            }            
        }
        return 0;
    }
};