class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = 0
        s_map = Counter(s)
        t_map = Counter(t)

        for i,v in s_map.items():
            if v > t_map[i]:
                diff += abs(t_map[i] - v)
        return diff
        
        
        
