class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # checking if the free painter could have painted up to all the walls up to j while the paid painter was doing i.
        money = [float('inf')] * (len(cost) + 1)
        money[0] = [0]

        for i in range(len(cost)):
            for j in range(len(cost), -1, -1):
                