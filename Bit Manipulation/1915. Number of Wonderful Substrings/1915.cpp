#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    long long wonderfulSubstrings(string word) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        long long res=0;
        int mask=0;
        vector<int>count(1024,0);
        count[0]++;

        for(auto& c : word){
            mask^=1<<c-97;
            res+=count[mask];
            for(int i=0; i<10; ++i){
                res+=count[mask^1<<i];
            }
            count[mask]++;
        }
        return res;
    }
};