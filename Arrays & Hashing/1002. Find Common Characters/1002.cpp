#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        vector<int> char_array(26, INT_MAX);  
        vector<string> res;

        for (const string& word : words) {
            vector<int> word_freq(26, 0); 
            for (char c : word) {
                word_freq[c - 'a']++;
            }
            for (int i = 0; i < 26; ++i) {
                char_array[i] = min(char_array[i], word_freq[i]);
            }
        }

        for (int i = 0; i < 26; ++i) {
            if (char_array[i] != INT_MAX && char_array[i] != 0) {
                for (int j = 0; j < char_array[i]; ++j) {
                    res.push_back(string(1, 'a' + i));
                }
            }
        }
        return res;
    }
};