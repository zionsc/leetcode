class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }
        # you aren't adding the different ways up until it gets to dp[0], one way is simply one way to decode it.