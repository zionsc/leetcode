class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        currVal = max(nums)
        # must negate values in order to create a maxHeap
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)

        while k > 0:
            currVal = -(heapq.heappop(maxHeap))
            k -= 1
        
        return currVal

