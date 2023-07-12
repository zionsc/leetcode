class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            # profit
            if prices[l] < prices[r]:
                # update maxProfit if necessary
                maxProfit = max(maxProfit, prices[r] - prices[l])

            # negative value --> no profit
            else:
                # change l to r --> r that was found was the smallest value!
                l = r
            
            # update r pointer to check next profit
            r += 1

        return maxProfit