#pragma GCC optimize("O3","Oz","unroll-loops","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<vector<int>>res;
    vector<vector<int>> subsets(vector<int>& nums) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        
        int n=nums.size();
        dfs({},0,n,nums);
        return res;
        
    }
private:
    void dfs(vector<int>currSubstr, int idx, int& n, vector<int>& nums) {
        if(idx==n) {
           res.push_back(currSubstr);
            return;
        }
        currSubstr.push_back(nums[idx]);
        dfs(currSubstr, idx+1, n, nums);
        currSubstr.pop_back();
            dfs(currSubstr, idx+1, n, nums);
        
    }
};