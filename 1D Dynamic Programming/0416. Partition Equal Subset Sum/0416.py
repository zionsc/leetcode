class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # basically the sum must be divisble by two in order for the two subsets to have the same sum!
        if sum(nums) % 2: # if it is 1
            return False
        
        dp = set()
        dp.add(0) # base case: what if we add no value so far 
        target = sum(nums) // 2 # for two partitions to have the same sum, it must be an equal sum of sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            newDP = dp.copy()
            for t in dp: # if at any point, the target comes up, it is possible to partition them!
                newDP.add(i + t)
            dp = newDP
        
        return 
