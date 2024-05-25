#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    vector<string> wordBreak(string st, vector<string>& wordDict) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        n=st.size();
        for (auto& word : wordDict) wordSet.insert(word);
        string sentence="";
        s=st;
        sentenceBacktrack(sentence,0);

        return res;
    }
private:
    int n=0;
    string s="";
    unordered_set<string>wordSet;
    vector<string>res;

    void sentenceBacktrack(string& sentence, int start_idx) {
        if (start_idx==n) {
            res.push_back(sentence.substr(0,sentence.size()-1));
            return;
        }

        for (int end_idx=start_idx; end_idx<n; end_idx++) {
            const string word=s.substr(start_idx, end_idx-start_idx+1);
            if (wordSet.find(word)!=wordSet.end()) {
                sentence+=word+" ";
                sentenceBacktrack(sentence, end_idx+1);
                sentence=sentence.substr(0,sentence.size()-word.size()-1);
            }
        }
    }
};