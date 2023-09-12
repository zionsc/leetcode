class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # using a minheap to make faster runtime (nlogn to make at the worst case)
        self.minHeap, self.k = nums, k # we keep k in order to make the minheap size of k later
        heapq.heapify(self.minHeap) # heapq.heapify(self.minHeap) is how to heapify in python
        
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # this is how to heapq.heappop in python

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # this is how to add to a heap in python
        if len(self.minHeap) > self.k: # in order to preserve the size of the minHeap as k, we must check if now the minHeap has gone over the size limit
            heapq.heappop(self.minHeap) 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)