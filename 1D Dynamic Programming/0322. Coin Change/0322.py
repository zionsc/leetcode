class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # we want amount + 1 to be our default value for all values from 0 - amount
        dp[0] = 0

        for a in range(1, amount + 1): # since it is inclusive, exclusive
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c]) # recurrence relation

        return dp[amount] if dp[amount] != amount + 1 else -1 
    # basically searching through all the coins and building up the solution from 0 -> amount for each dp[amount]