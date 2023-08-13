class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }
        # you aren't adding the different ways up until it gets to dp[0], one way is simply one way to decode it.

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                return 0
            else:
                dp[i] = dp[i + 1]
            
            if 