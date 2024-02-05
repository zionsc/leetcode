class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_map = defaultdict(list)
        for i,c in enumerate(s):
            if c not in my_map:
                my_map[c] = [1,i]
            else:
                freq, index = my_map[c]
                my_map[c] = [freq + 1, index]
        
        for i,lst in my_map.items():
            if lst[0] == 1:
                return lst[1]
        return -1