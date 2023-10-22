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
                while 


        for i in range(n - 1):
            recursion(res)
        return res