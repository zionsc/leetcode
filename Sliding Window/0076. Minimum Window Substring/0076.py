class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base case of when t is empty
        if t == "":
            return ""

        countT, countS = {}, {}

        for i in t:
            # if countT[i] does not exist, countT[i] will be initialized to 0 then the 1 will be added. otherwise can use a defaultdict(int)
            countT = 1 + countT.get(i, 0)
        
        # need should equal the unique values of T that I need my result to have, and have should = 0 because I have nothing within my sliding window yet. 
        need, have = len(countT), 0
        # res is initially set to -1, -1 because the left and right pointers have not been set yet for the min substring, 
        # and resLen should be infinity as we look for the minvalue.
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            countS = 1 + countS.get(s[r], 0)
            # need to check if s[r] is even in T first because otherwise it will not be able to check if it is just nullptr
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1

            while need == have:
                # check if the current window is smallest 
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)

                # decrement the number of times the character appears in the window
                countS[s[l]] -= 1 
                
                # also need to update have -> check if it was a duplicate, then have does not need to be updated.
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
            