class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # using a minheap to make faster runtime (nlogn to make at the worst case)
        self.minHeap, self.k = nums, k # we keep k in order to make the minheap size of k later

        
    def add(self, val: int) -> int:


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)