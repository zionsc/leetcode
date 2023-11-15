class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)] #[s][p]
        dp[0][0] = True

        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1] # if true, continue to be true
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] # SKIP last one, and continue from j - 2
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j] # match up to that point!!! dp is 1 indexed while s and p are 0 indexed 
        return dp[len(s)][len(p)]



        