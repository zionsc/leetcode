#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    unordered_map<int,vector<int>>adjList;
    pair<int,unordered_map<int,int>> bfs(int node) {
        deque<int>q;
        unordered_set<int>visited;
        q.push_back(node);
        visited.insert(node);
        unordered_map<int,int>parent;
        int farthestNode=node;

        while(!q.empty()){
            int curr=q.front();
            q.pop_front();
            for(auto& nei : adjList[curr]){
                if(visited.find(nei)==visited.end()){
                    visited.insert(nei);
                    q.push_back(nei);
                    farthestNode=nei;
                    parent[nei]=curr;
                }
            }
        }
        return {farthestNode,parent};
    }

    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(n==1){
            return {0};
        }

        for(auto& edge : edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        pair<int,unordered_map<int,int>>p1=bfs(0);
        pair<int,unordered_map<int,int>>p2=bfs(p1.first);

        vector<int>path;
        int node=p2.first;
        while(node!=p1.first){
            path.push_back(node);
            node=(p2.second)[node];
        }
        path.push_back(p1.first);

        int mid=path.size()/2;
        if(path.size()%2==0){
            return {path[mid-1],path[mid]};
        } else{
            return {path[mid]};
        }
    }
};