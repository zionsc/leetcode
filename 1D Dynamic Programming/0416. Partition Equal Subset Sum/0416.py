class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # basically the sum must be divisble by two in order for the two subsets to have the same sum!
        if sum(nums) % 2: # if it is 1
            return False
        