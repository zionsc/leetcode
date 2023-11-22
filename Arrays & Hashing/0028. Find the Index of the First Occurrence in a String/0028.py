class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for l in range(len(haystack)):
            # not possible to form needle anymore
            if len(haystack) - l < len(needle):
                return -1
            
            if haystack[l] == needle[0]:
                for r in range(len(needle)):
                    if haystack[l + r] != needle[r]:
                        break
                    if r == len(needle) - 1:
                        return l
                    
        return -1
