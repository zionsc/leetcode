#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    std::string makeGood(std::string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        std::stack<char> st;
        for(char c : s) {
            if(!st.empty() && (std::toupper(st.top()) == std::toupper(c)) && (st.top() != c)) {
                st.pop();
            } else {
                st.push(c);
            }
        }

        std::string res = "";
        while(!st.empty()) {
            res = st.top() + res;
            st.pop();
        }
        return res;
    }
};
