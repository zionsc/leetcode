class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        # creates a list of customers unhappy at each minute
        unhappy_list = list(mul, customers, grumpy)

        # number of customers happy if we use the power at minute 0! --> operates until minutes
        ans = score = sum(customers) - sum(z[minutes:])

        # start at 0, end at len(grumpy) - minutes as we do not want to g out of range --> basically update the sliding window so that
        # we add the number of unhappy people that we are adding to the sliding window, and remove the ones that we are no longer considering (SLIDE the window to the right)
        for i in range(len(grumpy) - minutes):
            score -= unhappy_list[i]
            score += unhappy_list[i + minutes]
            ans = max(ans, score)

        return ans
