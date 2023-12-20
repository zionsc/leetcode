class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # min1 = float('inf')
        # min2 = float('inf')
        # for price in prices:
        #     min1 = min(min1, price)
        
        # prices.remove(min1)
        # for price in prices:
        #     min2 = min(min2, price)
        
        # return money - min1 - min2 if min1 + min2 <= money else money
        prices.sort()
        return money - prices[0] - prices[1] if prices[0] + prices[1] <= money else money