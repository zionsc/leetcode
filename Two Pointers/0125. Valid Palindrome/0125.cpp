class Solution {
public:
    bool isPalindrome(string s) {
        std::stack<char> forwardStack;
        std::stack<char> backwardStack;

        for (int i = 0; i < s.length(); ++i) {
            if (isalpha(s[i]) || isdigit(s[i])) {
                forwardStack.push(tolower(s[i]));
            }
        }

        for (int i = s.length() - 1; i >= 0; --i) {
            if (isalpha(s[i]) || isdigit(s[i])) {
                backwardStack.push(tolower(s[i]));
            }
        }


        while (!forwardStack.empty()) {
            if (forwardStack.top() != backwardStack.top()) {
                return false;
            }
            else {
                forwardStack.pop();
                backwardStack.pop();
            }
        }
        
        return true;

    }
};