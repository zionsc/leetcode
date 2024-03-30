#pragma GCC optimize("03", "unroll-loops")

class Solution {
public:
    int atMostK(vector<int>& nums, int k) {
        vector<int> freq(nums.size()+1,0);
        int res=0;
        int l=0;

        for(int r=0; r<nums.size(); ++r){
            freq[nums[r]]++;
            if(freq[nums[r]]==1){
                k--;
            }
            while(k<0){
                freq[nums[l]]--;
                if(freq[nums[l]]==0){
                    k++;
                }
                l++;
            }
            res+=(r-l+1);
        } 
        return res;
    }

    int subarraysWithKDistinct(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        return atMostK(nums,k)-atMostK(nums,k-1);
    }
};