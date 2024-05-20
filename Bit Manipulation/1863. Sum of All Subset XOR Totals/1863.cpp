#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
       ios_base::sync_with_stdio(0);
       cin.tie(0);
       cout.tie(0);

       return dfs(0,0,nums.size(), nums);
    }
private:
    int dfs(int current, int idx, int numsLength, vector<int>& nums) {
        if(idx==numsLength){
            return current;
        }
        int include=dfs(current^nums[idx],idx+1,numsLength,nums);
        int exclude=dfs(current,idx+1,numsLength,nums);
        return include+exclude;
    }
};