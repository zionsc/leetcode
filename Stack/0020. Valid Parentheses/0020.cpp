class Solution {
public:
    bool isValid(string s) {
        std::stack<char> myStack;
        
        for (size_t i = 0; i < s.length(); ++i) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                myStack.push(s[i]);
            }
                
            // s[i] == closing bracket or paraenthesis
            else {
                if (!myStack.empty()) {
                    if ((s[i] == ')' && myStack.top() == '(') 
                    || (s[i] == ']' && myStack.top() == '[') 
                    || (s[i] == '}' && myStack.top() == '{')) {
                        myStack.pop();
                    }
                    // s[i] does not match myStack.top() --> imbalanced string
                    else {
                        return false;
                    }
                }
                // stack is empty --> imbalanced string
                else {
                    return false;
                }
            }
        }

        if (myStack.empty()) {
            return true;
        }
        return false;
    }
};