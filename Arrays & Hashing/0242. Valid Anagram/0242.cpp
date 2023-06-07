class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        std::unordered_map<char, int> myMap;

        for (char c : s) {
            myMap[c]++;
        }
        for (char c : t) {
            myMap[c]--;
            if (myMap[c] < 0) {
                return false;
            }
        }
        return true;
    }
};
