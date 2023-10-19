class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_backspace, t_backspace = [], []

        for i in range(len(s)):
            if s[i] == "#":
                if s_backspace:
                    s_backspace.pop()
            else:
                s_backspace.append(s[i])

        for i in range(len(t)):
            if t[i] == "#":
                if t_backspace:
                    t_backspace.pop()
            else:
                t_backspace.append(t[i])

        return s_backspace == t_backspace