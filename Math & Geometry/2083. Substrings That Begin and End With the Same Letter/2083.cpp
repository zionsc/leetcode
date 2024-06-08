#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    long long numberOfSubstrings(string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        int n = s.size();
        long long answer = 0;
        vector<long long> prefixCount(26, 0);

        for (int i = 0; i < s.size(); i++) {
            prefixCount[s[i] - 'a']++;
            answer += prefixCount[s[i] - 'a'];
        }

        return answer;
    }
};