#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    long long subsequenceSumOr(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        long long res=0;
        long long prefix=0;
        for(auto& num : nums){
            prefix+=num;
            res|=num;
            res|=prefix;
        }
        return res;
    }
};