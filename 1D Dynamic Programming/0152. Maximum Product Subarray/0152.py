class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(res) # [-1] -> then res would be -1. we can't set it to a default val like 1 or 0.
        currMin, currMax = 1, 1
        # reason we also keep track of currMin is due to consecutive negative values -> -1 * -2 = 2

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1 # re-update currMin and currMax to be 1, 1 because we are looking for
                                        # subarrays, meaning it must reset at that point again to start a new sequence