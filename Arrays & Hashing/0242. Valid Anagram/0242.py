class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hashmap = defaultdict(int)
        
        for i in s:
            hashmap[i] += 1

        for i in t:
            hashmap[i] -= 1
            if hashmap[i] < 0:
                return False
        
        return True
        
        
