#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        n = nums.size();
        vector<int> currSubset;
        backtrack(0, currSubset, nums, k);
        return res - 1;
    }

private:
    int res = 0;
    unordered_map<int, int> used;
    int n = 0;

    void backtrack(const int idx, vector<int>& currSubset, const vector<int>& nums, const int& k) {
        if (idx == n) {
            res++;
            return;
        }

        if (used.find(nums[idx] - k) == 0 && used.find(nums[idx] + k) == 0) {
            used[nums[idx]]++;
            currSubset.push_back(nums[idx]);
            backtrack(idx + 1, currSubset, nums, k);
            used[nums[idx]]--;
            currSubset.pop_back();
        }
        backtrack(idx + 1, currSubset, nums, k);
    }
};