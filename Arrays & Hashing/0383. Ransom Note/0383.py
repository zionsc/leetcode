class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # my_map = defaultdict(int)
        # for i,v in enumerate(magazine):
        #     my_map[v] += 1
        
        # for i,v in enumerate(ransomNote):
        #     my_map[v] -= 1
        #     if my_map[v] < 0:
        #         return False
        # return True

        for v in set(ransomNote):
            if magazine.count(v) < ransomNote.count(v):
                return False
        return True