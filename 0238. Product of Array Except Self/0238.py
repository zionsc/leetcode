class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # every index is 1, there are len(nums) indexes

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1): #from end to -1, decrement
            res[i] *= postfix
            postfix *= nums[i]
        return res

