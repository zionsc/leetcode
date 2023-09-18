class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can simply just use a minheap, the first value in each list element is the comparator
        minHeap = []
        res = []

        