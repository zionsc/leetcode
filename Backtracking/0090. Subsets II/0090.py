class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        # must be sorted in order to skip duplicate numbers -> to skip duplicate replicate recursive trees
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                
