class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
            
        return ""

    #     for word in words:
    #         if self.isPalindrome(word):
    #             return word
    #     return ""
        
    # def isPalindrome(self, word: str) -> bool:
    #     l,r = 0, len(word) - 1
        
    #     while l < r:
    #         if word[l] == word[r]:
    #             l += 1
    #             r -= 1
    #         else:
    #             return False
    #     return True
