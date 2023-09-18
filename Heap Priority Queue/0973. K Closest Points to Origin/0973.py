class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # can simply just use a minheap, the first value in each list element is the comparator
        minHeap = []
        res = []

        for x, y in points:
            distance = (x**2) + (y**2) # standardized comparison for each point 
            minHeap.append((distance, x, y))
        heapq.heapify(minHeap)

        for i in range(k):
            distance, x, y = heapq.heappop(minHeap) # we can get each value independently (this is some python syntax !! -> crazy good)
            res.append((x, y))
        return res