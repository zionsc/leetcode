#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    int maxDepth(string s) {
        ios_base::sync_with_stdio(0);
        cout.tie(0);
        cin.tie(0);

        int res=0;
        int curr=0;
        for(char c : s){
            if(c=='(') curr++;
            else if(c==')') curr--;
            res=max(res, curr);
        }
        return res;
    }
};