class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n=len(nums)
        dp=[[0]*2 for _ in range(n+1)]
        dp[n][1]=-float('inf') # odd number is invalid since edge operations are pairs
        dp[n][0]=0

        for i in range(n-1,-1,-1):
            for j in range(2):
                change = dp[i+1][j^1] + (nums[i]^k)
                noChange = dp[i+1][j] + nums[i]
                dp[i][j] = max(change, noChange)
        
        return dp[0][0] # at the end, we need even number of operations since edges are pairs
        