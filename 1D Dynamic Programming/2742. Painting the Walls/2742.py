class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # checking if the free painter could have painted up to all the walls up to j while the paid painter was doing i.
        money = [float('inf')] * (len(cost) + 1)
        money[0] = [0]

        for i in range(len(cost)):
            for j in range(len(cost), -1, -1):
                money[j] = min(money[j], money[max(j - time[i] - 1, 0)] + cost[i])
            
        return money[-1]