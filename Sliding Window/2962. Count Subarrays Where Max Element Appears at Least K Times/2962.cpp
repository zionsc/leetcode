class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        long long res=0;
        auto maxItr=max_element(nums.begin(),nums.end());
        int maxNum=*maxItr;
        int currCount=0;
        int l=0;

        for(int r=0; r<nums.size(); ++r){
            if(nums[r]==maxNum){
                currCount++;
            } 
            while(currCount>k || (currCount==k && nums[l]!=maxNum)){
                if(nums[l]==maxNum){
                    currCount--;
                }
                l++;
            }
            if(currCount==k){
                res+=l+1;
            }
        }
        return res;
    }
};