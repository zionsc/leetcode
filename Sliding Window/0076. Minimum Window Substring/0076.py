class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case of when t is empty
        if t == "":
            return ""

        countT, countS = {}, {}

        for i in t:
            # if countT[i] does not exist, countT[i] will be initialized to 0 then the 1 will be added. otherwise can use a defaultdict(int)
            countT = 1 + countT.get(i, 0)
        
        need, have = len(countT), 0
        res, resLen = [-1, -1], float("inf")
        l = 0