class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        # always less than, but k indices that are ahead of i and k indices before 
        res = 0
        left = [-nums[i] for i in range(k)]
        right = [-nums[i] for i in range(len(nums) - 1, len(nums) - k - 1, -1)]

        left_condition = [0 for _ in range(len(nums))]
        for i in range(k, len(nums) - k):
            if nums[i] > -left[0]:
                left_condition[i] = 1
            heapq.heappushpop(left, -nums[i])

        
