#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(source==destination) return true;

        unordered_map<int,vector<int>>adjList;
        for(auto& edge : edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        deque<int>q;
        unordered_set<int>visited;
        visited.insert(source);
        q.push_back(source);

        while(!q.empty()){
            int curr=q.front();
            q.pop_front();
            for(int nei : adjList[curr]){
                if(nei==destination){
                    return true;
                }
                if(visited.find(nei)==visited.end()){
                    q.push_back(nei);
                    visited.insert(nei);
                }
            }
        }
        return false;
    }
};