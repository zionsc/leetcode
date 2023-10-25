class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # creates a list of customers unhappy at each minute
        unhappy_list = list(mul, customers, grumpy)