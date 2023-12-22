class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        # Exclude the last index to avoid an empty right part
        for i in range(1, len(s)):  # Start from 1 to avoid an empty left part
            res = max(res, s[:i].count('0') + s[i:].count('1'))
        return res
