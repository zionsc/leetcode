class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> mySet;
        
        for (size_t i = 0; i < nums.size(); ++i) {
            if (mySet.find(nums[i]) != mySet.end()) {
                return true;
            }
            mySet.insert(nums[i]);
        }
        
        return false;
    }
};