// #pragma GCC optimize('03','unroll-loops')

// class Solution {
// public:
//     bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
//         ios_base::sync_with_stdio(0);
//         cin.tie(0);
//         cout.tie(0);

//         if(source==destination) return true;

//         unordered_map<int,vector<int>>adjList;
//         for(auto& edge : edges){
//             adjList[edge[0]].push_back(edge[1]);
//             adjList[edge[1]].push_back(edge[0]);
//         }

//         deque<int>q;
//         unordered_set<int>visited;
//         visited.insert(source);
//         q.push_back(source);

//         while(!q.empty()){
//             int curr=q.front();
//             q.pop_front();
//             for(int nei : adjList[curr]){
//                 if(nei==destination){
//                     return true;
//                 }
//                 if(visited.find(nei)==visited.end()){
//                     q.push_back(nei);
//                     visited.insert(nei);
//                 }
//             }
//         }
//         return false;
//     }
// };


#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int _find(int node, vector<int>& par) {
        int p=par[node];
        while(p!=par[p]){
            par[p]=par[par[p]];
            p=par[p];
        }
        return p;
    }

    void _union(int n1, int n2, vector<int>& par, vector<int>& rank) {
        int p1=_find(n1,par);
        int p2=_find(n2,par);

        if(p1==p2){
            return;
        }
        if(rank[p1]>rank[p2]){
            par[p2]=p1;
            rank[p1]+=rank[p2];
        } else{
            par[p1]=p2;
            rank[p2]+=rank[p1];
        }
    }

    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<int>par(n);
        vector<int>rank(n,1);

        for(int i=0; i<n; ++i){
            par[i]=i;
        }

        for(auto& edge : edges){
            _union(edge[0],edge[1],par,rank);
        }
        
        return _find(source,par)==_find(destination,par);
    }
};