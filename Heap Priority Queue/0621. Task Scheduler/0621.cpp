class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        unordered_map<char,int> freq;
        priority_queue<int> maxHeap;

        for (char chr : tasks) {
            freq[chr]++;
        }
        for (auto& [chr,cnt] : freq) {
            maxHeap.push(cnt);
        }

        int time = 0;
        deque<pair<int,int>> queue;
        while (!maxHeap.empty() || !queue.empty()) {
            time++;
            if (!maxHeap.empty()) {
                int cnt = maxHeap.top() - 1;
                maxHeap.pop();
                if (cnt>0) {
                    queue.push_back(make_pair(cnt, time+n));
                }
            } 
            if (!queue.empty() && queue[0].second == time) {
                int temp = queue[0].first;
                queue.pop_front();
                maxHeap.push(temp);
            }
        }
        return time;
    }
};