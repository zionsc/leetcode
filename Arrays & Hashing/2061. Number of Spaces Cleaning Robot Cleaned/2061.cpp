#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","omit-frame-pointer","march=native","lto")

struct hash_tuple {
    template<class T1, class T2, class T3>
    std::size_t operator() (const std::tuple<T1,T2,T3>& t) const {
        std::size_t h1 = std::hash<T1>{}(get<0>(t));
        std::size_t h2 = std::hash<T2>{}(get<1>(t));
        std::size_t h3 = std::hash<T3>{}(get<2>(t));
        return h1^h2^h3;
    }
};

class Solution {
public:
    int numberOfCleanRooms(vector<vector<int>>& room) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int res=0;
        int r=0;
        int c=0;
        int curr=0;
        int row=room.size();
        int col=room[0].size();
        std::array<pair<int,int>,4>direction({{0,1},{1,0},{0,-1},{-1,0}});
        std::unordered_set<std::tuple<int,int,int>,hash_tuple>visited;

        while (visited.find({r,c,curr})==visited.end()){
            visited.insert({r,c,curr});
            if(room[r][c]==0){
                room[r][c]=-1;
                res++;
            }
            if(r+direction[curr].first>=0 && r+direction[curr].first<row 
            && c+direction[curr].second>=0 && c+direction[curr].second<col
            && room[r+direction[curr].first][c+direction[curr].second]!=1)
            {
                r+=direction[curr].first;
                c+=direction[curr].second;
            } else {
                curr=(curr+1)%4;
            }
        }
        return res;
    }
};
