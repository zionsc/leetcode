#pragma GCC optimize("0fast", "unroll-loops")

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if(s.size()!=t.size()){
            return false;
        }

        unordered_map<char, char> sMap;
        unordered_map<char, char> tMap;

        for(int i=0; i<s.size(); ++i){
            if(sMap[s[i]]=='\0' && tMap[t[i]]=='\0'){
                sMap[s[i]]=t[i];
                tMap[t[i]]=s[i];
            } else if(sMap[s[i]]!=t[i] || tMap[t[i]]!=s[i]){
                return false;
            }
        }
        return true;
    }
};