class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # we want amount + 1 to be our default value for all values from 0 - amount