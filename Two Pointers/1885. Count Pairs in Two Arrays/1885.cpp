#pragma GCC optimize('0fast','unroll-loops')

class Solution {
public:
    long long countPairs(vector<int>& nums1, vector<int>& nums2) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        vector<int>nums3;
        for(int i=0; i<nums1.size(); ++i){
            nums3.push_back(nums1[i]-nums2[i]);
        }
        sort(nums3.begin(),nums3.end());

        int l=0;
        int r=nums3.size()-1;
        long long res=0;

        while(l<r){
            if(nums3[l]+nums3[r]>0){
                res+=r-l;
                r--;
            }else{
                l++;
            }
        }
        return res;
    }
};