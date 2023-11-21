class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        if x < 0:
            x_rev = -(int((str(x)[::-1])[:len(str(x))-1]))
        if x > 0:
            x_rev = int(str(x)[::-1])
        if x_rev < -2**31 or x_rev > 2**31:
            return 0
        return x_rev