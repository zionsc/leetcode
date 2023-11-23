class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")

        if len(s_list) != len(pattern):
            return False

        p_map, s_map = defaultdict(lambda: None), defaultdict(lambda: None)

        for i in range(len(pattern)):
            if p_map[pattern[i]] is None and s_map[s_list[i]] is None:
                p_map[pattern[i]] = s_list[i]
                s_map[s_list[i]] = pattern[i]
            elif p_map[pattern[i]] != s_list[i] or s_map[s_list[i]] != pattern[i]:
                return False
        return True
   