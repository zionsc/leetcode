class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.isPalindrome(s, i, i) # odd cases where an exact middle exists (where l = r = middle)
            res += self.isPalindrome(s, i, i + 1) # even cases where an exact middle does not exist

    
    def isPalindrome(self, s, l, r):
        numPalindromes = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            numPalindromes += 1
            l -= 1
            r += 1
        
        return numPalindromes