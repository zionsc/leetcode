class Solution:
    def rob(self, nums: List[int]) -> int:  
        # basically run house robber I twice on the nums[1:] and nums[:-1] (because we can't have the last and first values together selected)


    def helper(self, nums):
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...] -> logic works because no numbers are negative
        for n in nums:
            temp = max(rob1 + n, rob2)
            # now iterate to the next numbers -> update pointers
            rob1 = rob2
            rob2 = temp
        return rob2

            
