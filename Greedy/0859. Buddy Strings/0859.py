class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # len different
        if len(s) != len(goal):
            return False

        # same string
        if s == goal:
            freq = [0 for _ in range(26)]
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
                if freq[ord(s[i]) - ord('a')] == 2:
                    return True
            return False
        
        # different string
        left = right = -1
        if s != goal:
            for i in range(len(s)):
                if s[i] != goal[i]:
                    if left == -1:
                        left = i
                    elif right == -1:
                        right = i
                    else:
                        return False
        return s[left] == goal[right] and s[right] == goal[left]
