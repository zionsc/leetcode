class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            # remove to update subset -> remove until there is no more duplicates
            while s[r] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.append(s[r])
            res = max(res, r - l + 1)

        return res