class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # lambda: None is bascially setting the value to default None if not initialized --> lambda: None is good when
        # you want to check the existence of something before initialized! Perfect for our use case!
        s_map, t_map = defaultdict(lambda: None), defaultdict(lambda: None) 

        for s_v, t_v in zip(s, t):
            if s_map[s_v] is None and t_map[t_v] is None:
                s_map[s_v] = t_v
                t_map[t_v] = s_v
            elif s_map[s_v] != t_v or t_map[t_v] != s_v:
                return False
            
        return True