class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        vector<int> res;
        int minCost = 0;
        for (int i=0; i<costs.size(); ++i) {
            res.push_back(costs[i][1] - costs[i][0]);
            minCost += costs[i][0];
        }
        sort(res.begin(),res.end());

        for (int i=0; i<costs.size()/2; ++i) {
            minCost += res[i];
        }

        return minCost;
    }
};