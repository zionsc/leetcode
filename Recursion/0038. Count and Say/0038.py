class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return 1
        res = "1"

        def recursion(numStr):
            nonlocal res
            i = 0
            ret = ""
            while i < len(numStr):
                count = 1
                curr = numStr[i]
                while i + 1 < len(numStr) and curr == numStr[i + 1]:
                    i += 1
                    count += 1
                ret += str(count)
                ret += curr
                i += 1
            res = ret


        for i in range(n - 1):
            recursion(res)
        return res