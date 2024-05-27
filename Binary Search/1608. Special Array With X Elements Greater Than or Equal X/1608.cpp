#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int specialArray(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        int n=nums.size();
        sort(nums.begin(),nums.end());

        int l=0;
        int r=n;

        while (l<=r) {
            int mid=(l+r)/2;
            auto itr=lower_bound(nums.begin(),nums.end(),mid);
            int count=n-distance(nums.begin(),itr);
            // int pos=binSearch(nums,n, mid);
            // int count=n-pos;
            
            if (count==mid) {
                return mid;
            }
            else if (count>mid) {
                l=mid+1;
            }
            else if (count<mid) {
                r=mid-1;
            }
        }
        return -1;
    }

private:
    const int binSearch(const vector<int>& nums, const int& n, const int& target) const {
        int l=0;
        int r=n;
        while (l<r) {
            int mid=(l+r)/2;
            if (nums[mid]>=target) r=mid;
            else if (nums[mid]<target) l=mid+1;
        }
        return l;
    }
};