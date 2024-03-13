class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = 0
        prefix_sum = [i for i in range(n + 1)]
        for i in range(n + 1):
            prefix_sum[i] += prefix
            prefix += i
        
        prefix = 0
        for i in range(n, -1, -1):
            prefix += i
            if prefix_sum[i] == prefix:
                return i
        return -1

        