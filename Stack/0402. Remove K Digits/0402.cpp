#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    string removeKdigits(string num, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        string stk;
        
        for(char &digit : num){
            while(k && !stk.empty() && stk.back()>digit){
                stk.pop_back();
                k--;
            }
            if(stk.size() || digit!='0') stk.push_back(digit); // to avoid leading zeros
        }
        while(k && !stk.empty()){
            stk.pop_back();
            k--;
        }

        return stk.empty() ? "0" : stk;
    }
};