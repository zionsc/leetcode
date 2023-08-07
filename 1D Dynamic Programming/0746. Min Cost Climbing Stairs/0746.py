class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # basically leave the last two values in cost, and iterate backwards to determine what 
        # the min cost would be 