class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        zero = one = 0
        res = ""
        for i in range(len(s)):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
        
        while one != 1:
            res += "1"
            one -= 1
        while zero > 0:
            res += "0"
            zero -= 1
        if one:
            res += "1"
        return res