#pragma GCC optimize("Ofast","Os","unroll-loops","lto","fast-math","march=native","omit-frame-pointer","inline-functions")
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        sort(happiness.begin(),happiness.end());
        long long res=0;
        long long rounds=0;
        int i=happiness.size()-1;

        while(k>0 && i>=0){
            res+=happiness[i]-rounds>=0 ? happiness[i]-rounds : 0;
            rounds++;
            i--;
            k--;
        }
        return res;
    }
};