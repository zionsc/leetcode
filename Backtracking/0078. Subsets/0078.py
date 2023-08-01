class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # result list 

        subset = [] # global subset so we can keep track of the current recursive step

        def dfs(i): # i keeps track of the index that we are currently at in nums[i]
            # if i has gone out of bounds, we must add it to res since we went through all possible steps
            if i >= len(nums):
                res.append(subset)
                return
        
            # decision to add current nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to NOT add current nums[i]
            subset.pop() # must remove the one that we just added 
            dfs(i + 1)
            
