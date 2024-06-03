class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_itr = iter(s)
        for i,c in enumerate(t):
            if c not in s_itr:
                return len(t) - i
        return 0