#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        n=words.size();
        freq=vector<int>(26,0);
        for (auto& c : letters) freq[c-'a']++;
        value=score;
        word_list=words;

        word_backtrack(0,0);
        return res;
    }
private:
    int res=0;
    int n=0;
    vector<int> freq;
    vector<int> value;
    vector<string> word_list;

    void word_backtrack(int w_idx, int currMax) {
        if (w_idx==n) {
            res = max(res, currMax);
            return;
        }
        char check = '1';
        unordered_map<char,int> count;
        for (auto& c : word_list[w_idx]) {
            count[c]++;
        }
        for (auto& p : count) {
            if (p.second > freq[p.first - 'a']) {
                check='0';
            }
        }
        if (check=='1' && letter_backtrack(word_list[w_idx],0)) {
            auto temp=0;
            for (auto& c : word_list[w_idx]) {
                temp+=value[c-'a'];
            }
            for (auto& c : word_list[w_idx]) {
                freq[c-'a']--;
            }
            word_backtrack(w_idx+1, temp+currMax);
            for (auto& c : word_list[w_idx]) {
                freq[c-'a']++;
            }
        }
        word_backtrack(w_idx+1, currMax);
    }

    bool letter_backtrack(const string& word, int idx) {
        if (idx == word.size()) return true;
        if (freq[word[idx]-'a']==0) return false;
        return letter_backtrack(word, idx+1);
    }
    
};