class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n=nums.size();
        
        for (int i=0; i<n; ++i) {
            int x=nums[i];
            while (x>=1 && x<=n && x-1!=i && nums[x-1]!=x) {
                swap(nums[i], nums[x-1]);
                x=nums[i];
            }
        }

        for (int i=0; i<n; ++i) {
            if (nums[i]!=i+1) {
                return i+1;
            }
        }
        return n+1;

    }
}