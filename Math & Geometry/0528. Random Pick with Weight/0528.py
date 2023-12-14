class Solution:

    def __init__(self, weights: List[int]):
        self.prefixSums = []
        prefix_sum = 0
        for weight in weights :
            prefix_sum += weight
            self.prefixSums.append(prefix_sum)
        self.totalSum = self.prefixSums[-1]

    def pickIndex(self) -> int:
        target = self.totalSum*random.random()

        # run a binary search to find the target zone
        low, high = 0, len(self.prefixSums)
        while low < high:
            mid = (low + high) // 2
            if self.prefixSums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()