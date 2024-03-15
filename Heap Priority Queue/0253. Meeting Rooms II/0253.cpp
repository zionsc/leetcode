class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const vector<int>&a, const vector<int>&b)
        {
            return a[0] < b[0];
        });

        priority_queue<int, vector<int>, greater<int>> pq;
        pq.push(intervals[0][1]);

        for (int i=0; i<intervals.size(); ++i) {
            if (intervals[i][0] >= pq.top()) {
                pq.pop();
            } pq.push(intervals[i][1]);
        } return pq.size();
    }
};