#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int curr=0;
        for(auto& num : nums){
            curr^=num;
        }
        curr^=k;

        int res=0;
        while(curr){
            curr&=(curr-1);
            res++;
        }
        return res;
    }
}