#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    struct pair_hash{
        template<class T1, class T2>
        size_t operator() (const pair<T1,T2>& p) const {
            auto hash1=std::hash<T1>{}(p.first);
            auto hash2=std::hash<T2>{}(p.second);
            return hash1^hash2;
        }
    };

    unordered_map<pair<int,int>,pair<int,int>,pair_hash>par;
    unordered_map<pair<int,int>,int,pair_hash>rank;

    pair<int,int> _find(pair<int,int> node){
        pair<int,int>p=par[node];
        while(p!=par[p]){
            par[p]=par[par[p]];
            p=par[p];
        }
        return p;
    }

    bool _union(pair<int,int> n1, pair<int,int> n2){
        pair<int,int> p1=_find(n1);
        pair<int,int> p2=_find(n2);

        if(p1==p2) return false;
        if(rank[p1]>rank[p2]){
            par[p2]=p1;
            rank[p1]+=rank[p2];
        }
        else{
            par[p1]=p2;
            rank[p2]+=rank[p1];
        }
        return true;
    }


    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int cnt=0;
        vector<int>res;
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for(auto& position : positions){
            int r=position[0];
            int c=position[1];
            pair<int,int>node={position[0],position[1]};
            if(!par.count(node)){
                par[node]=node;
                rank[node]=1;
                cnt++;
                for(auto& dir : directions){
                    int nr=r+dir.first;
                    int nc=c+dir.second;
                    pair<int,int>nei{nr,nc};
                    if(nr>=0 && nr<m && nc>=0 && nc<n && par.count(nei)){
                        if(_union(node,nei))cnt--;
                    }
                }
            }
            res.push_back(cnt);
        }
        return res;
    }
};