class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l=res=distinct=0

        for r in range(len(s)):
            freq[s[r]]+=1
            if freq[s[r]]==1:
                distinct+=1
            while distinct>k:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    distinct-=1
                l+=1
            if distinct<=k:
                res=max(res, r-l+1)
        return res
            