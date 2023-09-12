class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # in order to create a max heap in python, minheap values must be negated, thus flipping the minheap into a max heap.
        