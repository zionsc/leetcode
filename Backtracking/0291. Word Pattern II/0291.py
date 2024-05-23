class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pattern_to_s=defaultdict(lambda:None)
        s_to_pattern=defaultdict(lambda:None)
        
        def backtrack(p_idx: int, s_idx: int) -> bool:
            if p_idx == len(pattern):
                return s_idx == len(s)
            
            p=pattern[p_idx]
            if pattern_to_s[p]:
                word = pattern_to_s[p]
                if s[s_idx : s_idx+len(word)] != word:
                    return False
                return backtrack(p_idx+1, s_idx+len(word))
            else:
                for i in range(1, len(s)-s_idx+1):
                    word = s[s_idx : s_idx+i]
                    if s_to_pattern[word]:
                        continue
                    pattern_to_s[p] = word
                    s_to_pattern[word] = p
                    if backtrack(p_idx+1, s_idx+len(word)):
                        return True
                    pattern_to_s[p] = None
                    s_to_pattern[word] = None
            return False
        
        return backtrack(0,0)