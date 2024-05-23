#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")

class Solution {
public:
    bool wordPatternMatch(string pattern, string s) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);
        unordered_map<char, string> pattern_to_s;
        unordered_map<string, char> s_to_pattern;
        return backtrack(pattern, s, 0, 0, pattern_to_s, s_to_pattern);
    }
private:
    bool backtrack(const string& pattern, const string& s, int p_idx, int s_idx, unordered_map<char, string>& pattern_to_s, unordered_map<string, char>& s_to_pattern) {
        if (p_idx == pattern.size()) return s_idx == s.size();

        char p = pattern[p_idx];
        if (pattern_to_s.find(p) != pattern_to_s.end()) {
            const string& word = pattern_to_s[p];
            if (s.substr(s_idx, word.size()) != word) return false;
            return backtrack(pattern, s, p_idx + 1, s_idx + word.size(), pattern_to_s, s_to_pattern);
        } else {
            for (int i = 1; i <= s.size() - s_idx; ++i) {
                string word = s.substr(s_idx, i);
                if (s_to_pattern.find(word) != s_to_pattern.end()) continue;
                pattern_to_s[p] = word;
                s_to_pattern[word] = p;
                if (backtrack(pattern, s, p_idx + 1, s_idx + i, pattern_to_s, s_to_pattern)) return true;
                pattern_to_s.erase(p);
                s_to_pattern.erase(word);
            }
        }
        return false;
    }
};