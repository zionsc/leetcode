class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for l in range(len(haystack)):
            # not possible to form needle anymore
            if len(haystack) - l < len(needle):
                return -1
            
