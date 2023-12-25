class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct_map = defaultdict(int)
        num_distinct = 0
        res = 0
        l,r = 0,0
        while r < len(s):
            distinct_map[s[r]] += 1
            if distinct_map[s[r]] == 1:
                num_distinct += 1
            while num_distinct > 2:
                distinct_map[s[l]] -= 1
                if distinct_map[s[l]] == 0:
                    num_distinct -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
