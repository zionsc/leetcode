class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        map<int,int> freq;
        int maxFreq = 0;
        int res = 0;
        for (int i=0; i<nums.size(); ++i) {
            freq[nums[i]]++;
            maxFreq = std::max(maxFreq, freq[nums[i]]);
        } 
        for (auto itr : freq) {
            if (itr.second == maxFreq) {
                res += maxFreq;
            }
        } return res;
    }
};