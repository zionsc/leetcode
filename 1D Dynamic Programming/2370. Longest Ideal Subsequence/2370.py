class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0]*26
        res=0

        for i in range(len(s)):
            curr=ord(s[i])-ord('a')
            best=0
            for prev in range(26):
                if abs(curr-prev)<=k:
                    best=max(best,dp[prev])
                
            dp[curr]=max(dp[curr],best+1)
            res=max(res,dp[curr])
        return res