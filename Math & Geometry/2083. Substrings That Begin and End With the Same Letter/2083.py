class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        answer = 0
        prefix_count = [0] * 26

        for i in range(len(s)):
            prefix_count[ord(s[i]) - ord("a")] += 1
            answer += prefix_count[ord(s[i]) - ord("a")]

        return answer