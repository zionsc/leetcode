class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res |= n & 1
            res <<= 1
            n >>= 1
        res >>= 1 # since it is shifted left once more at the end (so 33 times), thus shift it back
        return res
        
        # bits = bin(n)[2:]
        # bits = bits.zfill(32)
        # bits = bits[::-1]

        # return int(bits, 2)

