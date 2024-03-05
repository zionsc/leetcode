class Solution:
    def minimumLength(self, s: str) -> int:
        l,r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            curr_char = s[l]
            while l <= r and s[l] == curr_char:
                l += 1
            while l <= r and s[r] == curr_char:
                r -= 1
        
        return max(0, r - l + 1)