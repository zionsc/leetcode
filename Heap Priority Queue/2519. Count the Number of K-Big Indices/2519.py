class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # always less than, but k indices that are ahead of i and k indices before 
        n = len(nums)
        res = 0
        left = [-nums[i] for i in range(k)]
        right = [-nums[i] for i in range(n - 1, n - k - 1, -1)]
        