class Solution {
public:
    string removeVowels(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        string res = "";
        
        for (char c : s) {
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
                res += c;
            }
        }
        return res;
    }
};