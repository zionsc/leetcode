class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev = [0] * 3
        prev[0], prev[1], prev[2] = costs[0][0], costs[0][1], costs[0][2]

        for i in range(1, len(costs)):
            curr = [0] * 3
            c = costs[i]
            curr[0] = c[0] + min(prev[1], prev[2])
            curr[1] = c[1] + min(prev[0], prev[2])
            curr[2] = c[2] + min(prev[0], prev[1])
            prev = curr

        return min(prev)