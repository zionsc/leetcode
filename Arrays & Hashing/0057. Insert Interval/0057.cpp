class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> newIntervals;
        vector<vector<int>> res;
        for (auto interval : intervals) {
            newIntervals.push_back(interval);
        } newIntervals.push_back(newInterval);

        sort(newIntervals.begin(), newIntervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        int start = newIntervals[0][0];
        int end = newIntervals[0][1];

        for (int i=1; i<newIntervals.size(); ++i) {
            if (newIntervals[i][0] > end) {
                res.push_back({start,end});
                start = newIntervals[i][0];
                end = newIntervals[i][1];
            } else {
                end = max(end, newIntervals[i][1]);
            }
        }
        res.push_back({start,end});
        return res;
    }
};