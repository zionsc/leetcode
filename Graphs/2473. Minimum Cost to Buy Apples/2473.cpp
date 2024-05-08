#pragma GCC optimize("03","unroll-loops")
class Solution {
public:
    inline vector<long long> minCost(int n, vector<vector<int>>& roads, vector<int>& appleCost, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);

        vector<vector<pair<int,int>>>adjList(n);
        for(auto& path : roads){
            int u=path[0];
            int v=path[1];
            int w=path[2];
            adjList[u-1].push_back({v-1,w});
            adjList[v-1].push_back({u-1,w});
        }

        vector<long long>res(n,LLONG_MAX);
        for(int i=0; i<n; ++i){
            vector<long long>dist(n,LLONG_MAX);
            dist[i]=0;
            priority_queue<pair<long long,int>,vector<pair<long long,int>>,greater<pair<long long,int>>>pq;
            pq.push({0,i});
            while(!pq.empty()){
                long long nodeCost=pq.top().first;
                int node=pq.top().second;
                pq.pop();
                res[i]=min(res[i], appleCost[node]+(k+1)*nodeCost);
                for(auto& nei : adjList[node]){
                    int neiNode=nei.first;
                    long long neiCost=nodeCost+nei.second;
                    if(neiCost<dist[neiNode]){
                        dist[neiNode]=neiCost;
                        pq.push({neiCost,neiNode});
                    }
                }
            }
        }
        return res;
    }
};