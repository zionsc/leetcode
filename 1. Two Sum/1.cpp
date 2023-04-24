class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> myMap;
        vector<int> myVec;

        for (int i = 0; i < nums.size(); ++i) {
            myMap.insert({nums[i], i});
        }

        for (int i = 0; i < nums.size(); ++i) {
            if (myMap.find(target - nums[i]) != myMap.end()
             && myMap.find(target - nums[i])->second != i) {
                myVec.push_back(i);
                myVec.push_back(myMap.find(target - nums[i])->second);
                return myVec;
            }
        }
    return myVec;
    }
};
