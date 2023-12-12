class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        # heap = [-num for num in nums]
        # heapq.heapify(heap)

        # return (-(heapq.heappop(heap)) - 1) * (-(heapq.heappop(heap)) - 1)        