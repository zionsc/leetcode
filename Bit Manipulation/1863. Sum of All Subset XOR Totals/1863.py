class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def dfs(curr,i):
            if i==n:
                return curr
            include = dfs(curr^nums[i],i+1)
            exclude = dfs(curr,i+1)
            return include + exclude
        return dfs(0,0)