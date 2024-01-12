class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        vowels = 0
        for i in range(n//2):
            if s[i] in "aeiou":
                vowels += 1
        
        for i in range(n//2, n):
            if s[i] in "aeiou":
                vowels -= 1

        return True if vowels == 0 else False