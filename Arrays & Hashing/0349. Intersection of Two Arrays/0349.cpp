class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_set<int> visit;
        for (auto num : nums1) {
            visit.insert(num);
        }
        for (auto num : nums2) {
            if (visit.find(num) != visit.end()) {
                res.push_back(num);
                visit.erase(num);
            }
        } return res;
    }
};