class Solution {
public:
    int pivotInteger(int n) {
        int prefix = 0;
        vector<int> prefixSum;
        for (int i=0; i<n+1; ++i) {
            prefix += i;
            prefixSum.push_back(prefix);
        } prefix = 0;
        
        for (int i=n; i>-1; --i) {
            prefix += i;
            if (prefix==prefixSum[i]) {
                return i;
            }
        } return -1;
    }
};