class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        if (k<=1) {
            return 0;
        }

        int curr=1;
        int l=0;
        int res=0;

        for(int r=0; r<nums.size(); ++r) {
            curr*=nums[r];
            while(curr>=k && l<=r) {
                curr/=nums[l];
                l++;
            }
            res+=(r-l+1);
        }
        return res;

    }
};