class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # must negate values in order to create a maxHeap
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)

