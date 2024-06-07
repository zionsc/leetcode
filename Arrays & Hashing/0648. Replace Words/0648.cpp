#pragma GCC optimize("O3","Oz","unroll-loops","inline-functions","fast-math","march=native","lto","omit-frame-pointer")
class Solution {
public:
    std::string replaceWords(std::vector<std::string>& dictionary, std::string sentence) {
        ios_base::sync_with_stdio(0);
        cin.tie(0);
        cout.tie(0);

        std::unordered_set<std::string> wordDict(dictionary.begin(), dictionary.end());
        std::vector<std::string> sentenceList;
        std::istringstream iss(sentence);
        std::string word;

        while (iss >> word) {
            for (int32_t i = 1; i < word.size(); i++) {
                if (wordDict.find(word.substr(0, i)) != wordDict.end()) {
                    word = word.substr(0, i);
                    break;
                }
            }
            sentenceList.push_back(word);
        }

        std::string res = join(sentenceList);
        return res.substr(0, res.size() - 1);
    }

private:
    std::string join(const std::vector<std::string> sentenceList) {
        std::stringstream ss;
        for (const auto& word : sentenceList) ss << word << " ";
        return ss.str();
    }
};