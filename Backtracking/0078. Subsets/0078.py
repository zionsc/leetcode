class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # result list 

        subset = [] # global subset so we can keep track of the current recursive step

        def dfs(i): # i keeps track of the index that we are currently at in nums[i]
