#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int maxDistance(vector<int>& position, int m) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        std::sort(position.begin(), position.end());
        int res = 0;
        int n = position.size();
        int l = 1, r = position[n - 1] - position[0];

        while (l <= r) {
            int mid = (l + r) / 2;
            int count = 1;
            int last = position[0];

            for (int i = 1; i < n; i++) {
                if (position[i] - last >= mid) {
                    count++;
                    last = position[i];
                }
            }
            if (count >= m) {
                res = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return res;
    }
};