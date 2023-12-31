class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        hashmap = {}
        
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = i
            else:
                res = max(res, i - hashmap[s[i]] - 1)

        return res
        
        