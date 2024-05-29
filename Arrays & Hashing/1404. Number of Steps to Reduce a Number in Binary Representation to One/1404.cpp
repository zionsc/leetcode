#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int numSteps(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<char>sList(s.begin(),s.end());
        int res=0;

        while (sList.size()>1) {
            if (sList[sList.size()-1]=='0') sList.pop_back();
            else {
                int i=sList.size()-1;
                while (i>=0 && sList[i]=='1') {
                    sList[i]='0';
                    i--;
                }
                if (i>=0) sList[i]='1';
                else sList.insert(sList.begin(),'1');
            }
            res++;
        }
        return res;
    }
};