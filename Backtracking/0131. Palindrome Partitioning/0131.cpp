#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<vector<string>> partition(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        str=s;
        n=s.size();
        vector<string> currPartition;
        dfs(0,currPartition);
        return res;
    }

private:
    string str;
    int n;
    vector<vector<string>> res;

    void dfs(const int i, vector<string>& currPartition) {
        if(i==n){
            res.push_back(currPartition);
            return;
        }
        for(int j=i; j<n; ++j){
            if(isPalindrome(i,j)=='1'){
                currPartition.push_back(str.substr(i,j-i+1));
                dfs(j+1,currPartition);
                currPartition.pop_back();
            }
        }
    }

    const char isPalindrome(int l, int r) {
        while(l<r){
            if(str[l]!=str[r]) return '0';
            l++;
            r--;
        } return '1';
    }
};