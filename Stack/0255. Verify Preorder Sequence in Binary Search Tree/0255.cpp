#pragma GCC optimize('0fast', 'unroll-loops')

class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        stack<int>st;
        int currRoot=-1;

        for(int currNode : preorder){
            while(!st.empty() && currNode>st.top()){
                currRoot=st.top();
                st.pop();
            }
            if(currNode<=currRoot) return false;

            st.push(currNode);
        }
        return true;

    }
};