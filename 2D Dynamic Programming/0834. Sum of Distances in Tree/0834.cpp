#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);


        unordered_map<int,vector<int>>adjList;
        for(auto& edge : edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        vector<int>res(n,0);
        vector<int>count(n,1);

        dfs1(0,-1,adjList,res,count);
        dfs2(0,-1,adjList,n,res,count);
        return res;
    }
private:


    void dfs1(int node, int parent, auto& adjList, auto& res, auto& count) {
        for(auto& child : adjList[node]){
            if(child!=parent){
                dfs1(child,node,adjList,res,count);
                count[node]+=count[child];
                res[node]+=res[child]+count[child];
            }
        }
    }

    void dfs2(int node, int parent, auto& adjList, int& n, auto& res, auto& count) {
        for(auto& child : adjList[node]){
            if(child!=parent){
                res[child]=res[node]-count[child]+(n-count[child]);
                dfs2(child,node,adjList,n,res,count);
            }
        }
    }
};