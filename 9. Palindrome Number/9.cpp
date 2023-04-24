class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        std::string str = std::to_string(x);
        int i = 0;
        int j = str.size() - 1;
        while (i < j) {
            if (str[i] != str[j]) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
};
