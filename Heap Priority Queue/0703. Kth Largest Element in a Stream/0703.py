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
        return self.minHeap[0] # minHeap keeps the minimum value at the root (self.minHeap[0])
        # the minimnum value in our minHeap is the kth largest value as we count down from the largest value down
        # to the kth largest value, it is the last value in our count --> kth value in our count. This is the smallest
        # value in our entire minHeap as our minHeap is kept as a size of k 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)