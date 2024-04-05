#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    string makeGood(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        string res="";
        for(char c : s){
            if(!res.empty() && toupper(res.back())==toupper(c) && c-res.back()!=0){
                res.pop_back();
            } else{
                res.push_back(c);
            }
        }
        return res;
    }
};
