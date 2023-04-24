class Solution {
public:
    int lengthOfLastWord(string s) {
        stack<char> myStack;
        int cnt = 0;

        for (int i = 0; i < s.length(); ++i) {
            myStack.push(s[i]);
        }

        while (myStack.top() == ' ') {
            myStack.pop();
        }

        while (!myStack.empty() && myStack.top() != ' ') {
            myStack.pop();
            cnt++;
        }
        return cnt;
    }
};