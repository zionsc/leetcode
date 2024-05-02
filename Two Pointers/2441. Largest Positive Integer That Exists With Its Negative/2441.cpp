#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    int findMaxK(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int l=0;
        int r=nums.size()-1;
        sort(nums.begin(),nums.end());

        while(l<r && nums[l]<0 && nums[r]>0){
            if(abs(nums[l])==abs(nums[r])) return nums[r];
            if(abs(nums[l])>nums[r]) l++;
            else r--;
        }
        return -1;
    }
};