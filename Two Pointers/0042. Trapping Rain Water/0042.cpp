#pragma GCC optimize('03','unroll-loops')

class Solution {
public:
    int trap(vector<int>& height) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int l=0;
        int r=height.size()-1;
        int leftMax=height[0];
        int rightMax=height[r];
        int res=0;

        while(l<r){
            if(leftMax<rightMax){
                l++;
                leftMax=max(leftMax,height[l]);
                res+=leftMax-height[l];
            } else{
                r--;
                rightMax=max(rightMax,height[r]);
                res+=rightMax-height[r];
            }
        }
        return res;
    }
};