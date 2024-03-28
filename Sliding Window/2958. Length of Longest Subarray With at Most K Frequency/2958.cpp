class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        unordered_map<int,int> freq;
        int l=0;
        int res=0;

        for(int r=0; r<nums.size(); ++r) {
            freq[nums[r]]++;
            while(freq[nums[r]]>k) {
                freq[nums[l]]--;
                l++;
            }
            res=max(res,r-l+1);
        }
        return res;
    }
};