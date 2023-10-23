class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1. check if positive
        # 2. check if it is a power of 2.
        # 3. check if it is a power of 4. -> reason we check for power of 2 first is because power of 4 has 1 bit set only in even places, but power of 2 needs
        # to be checked in order to ensure that there is only 1 bit set to 1. (1000, 0100, 0010)

        mask = 0x55555555
        return True if n > 0 and (n & (n - 1)) == 0 and (n & mask) == n else False