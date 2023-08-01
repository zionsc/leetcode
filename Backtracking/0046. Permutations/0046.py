class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # basically recursively swap vals
        def backtrack(i):
            if i >= len(nums):
                res.append(nums.copy())
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

            
        backtrack(0)
        return res