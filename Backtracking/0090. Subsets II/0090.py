class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        # must be sorted in order to skip duplicate numbers -> to skip duplicate replicate recursive trees
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
        
            # decision to INCLUDE nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # decision to NOT include nums[i]
            # must iterate i until it is not a number that has already been done -> because duplicate numbers 
            # will cause duplicate recursive trees
