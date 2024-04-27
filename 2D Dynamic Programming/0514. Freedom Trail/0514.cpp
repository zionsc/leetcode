#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int findRotateSteps(string ring, string key) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n=ring.size();

        unordered_map<char,vector<int>>idxMap;
        for(int i=0; i<ring.size(); ++i){
            idxMap[ring[i]].push_back(i);
        }

        vector<vector<int>>dp(key.size(), vector<int>(n,INT_MAX));
        for(auto& idx : idxMap[key[0]]){
            dp[0][idx]=min(idx,n-idx)+1;
        }

        for(int i=1; i<key.size(); ++i){
            for(auto& j : idxMap[key[i]]){
                for(auto& k : idxMap[key[i-1]]){
                    int dist=abs(j-k);
                    int minSteps=min(dist, n-dist);
                    dp[i][j]=min(dp[i][j],dp[i-1][k]+minSteps+1);
                }
            }
        }
        return *min_element(dp[key.size()-1].begin(),dp[key.size()-1].end());
    }
};