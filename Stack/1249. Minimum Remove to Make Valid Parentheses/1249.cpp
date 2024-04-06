#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        ios_base::sync_with_stdio(0);
        cout.tie(0);
        cin.tie(0);

        stack<int> stk;
        string res="";

        for(int i=0; i<s.size(); ++i){
            if(s[i]=='('){
                stk.push(i);
            } else if(s[i]==')'){
                if(!stk.empty()){
                    stk.pop();
                } else{
                    s[i]='&';
                }
            }
        }
        while(!stk.empty()){
            s[stk.top()]='&';
            stk.pop();
        }
        for(char c : s){
            if(c!='&'){
                res+=c;
            }
        }
        return res;
    }
};