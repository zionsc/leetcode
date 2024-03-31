#pragma GCC optimize("03", "unroll-loops")

class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        long long res=0;
        int l=0;
        int lastMin=-1;
        int lastMax=-1;

        for(int r=0; r<nums.size(); ++r){
            if(nums[r]<minK || nums[r]>maxK){
                l=r+1;
                lastMin=-1;
                lastMax=-1;
            }
            if(nums[r]==minK){
                lastMin=r;
            }
            if(nums[r]==maxK){
                lastMax=r;
            }
            if(lastMin!=-1 && lastMax!=-1){
                res+=min(lastMin,lastMax)-l+1;
            }
        }
        return res;
    }
};