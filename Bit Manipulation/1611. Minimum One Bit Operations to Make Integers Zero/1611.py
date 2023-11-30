class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        total_operations = 0
        sign = -1

        for i in range(n.bit_length(), 0, -1):
            if n & (1 << (i - 1)):
                operations = 2 ** i - 1
                total_operations += sign * operations
                sign *= -1
        return abs(total_operations) 