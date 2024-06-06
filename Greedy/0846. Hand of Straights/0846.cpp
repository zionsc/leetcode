#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-nath","march=native","lto","omit-frame-pointer")
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int32_t n = hand.size();
        if (n % groupSize != 0) return false;

        std::unordered_map<int, int> freq;
        for (const auto& num : hand) freq[num]++;

        std::vector<int> sortedKeys;
        for (const auto& kv : freq) sortedKeys.push_back(kv.first);
        sort(sortedKeys.begin(), sortedKeys.end());

        for (auto& key : sortedKeys) {
            if (freq[key] > 0) {
                int32_t startCount = freq[key];
                for (int32_t i = key; i < key + groupSize; i++) {
                    if (freq[i] < startCount) return false;
                    freq[i] -= startCount;
                }
            }
        }
        return true;
    }
};