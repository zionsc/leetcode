class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # in order to create a max heap in python, minheap values must be negated, thus flipping the minheap into a max heap.
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones) # x is the first value popped from our max heap, thus it is the larger value.
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, -(first - second)) # must negate it again to maintain max_heap property

        return abs(stones[0]) if stones else 0