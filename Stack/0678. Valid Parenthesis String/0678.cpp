#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    bool checkValidString(string s) {
        ios_base::sync_with_stdio(0);
        cout.tie(0);
        cin.tie(0);

        int low=0;
        int high=0;

        for(char c : s){
            if(c=='('){
                low++;
                high++;
            } else if(c==')'){
                low--;
                high--;
            } else if(c=='*'){
                low--;
                high++;
            }
            if(high<0) return false;
            low=max(0,low);
        }
        return low==0;
    }
};