class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(len(prices))):
            if prices[i] > prices[i - 1]:
                profit += profit[i] - profit[i - 1]
        return profit

        ######
        dp = [[0] * 2 for i in range(len(profit))]
        dp[0][0] = 0
        dp[0][1] = -profit[0]

        for i in range(1, len(profit)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + profit[i]) # maintain state or sell 
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - profit[i])
        
        return dp[len(profit) - 1][0]