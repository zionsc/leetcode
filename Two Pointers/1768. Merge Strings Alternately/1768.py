class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        res = ""
        i,j = 0,0
        while i < n or j < m:
            if i < n:
                res += word1[i]
                i += 1
            if j < m:
                res += word2[j]
                j += 1
            
        return res