#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    string reversePrefix(string word, char ch) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int idx=word.find(ch);
        if(idx==-1)return word;
        reverse(word.begin(),word.begin()+idx+1);
        return word;
    }
};